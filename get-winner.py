import json
import pandas as pd
import random

NATHAN_ADDRESS = 'rdx1qsphe3yjc89s2jqlkjcpr6hapee6hjvqn0kt57m4zyze92us8m9t2mcpeqdz2'


def select_proportional_winners_indices(stakes: list[int], seed: int, n_winners: int) -> list[int]:
    """
    Returns a list of n_winners indices of the list stakes,
    where the probability of a stake being chosen is proportional to its value.

    Args:
        stakes (list[int]): List of stakes.
        seed (int): Seed for the random number generator.
        n_winners (int): Number of winners to return.

    Returns:
        list[int]: List of indices of the list stakes who won.
    """
    random.seed(a=seed, version=2)
    return random.choices(range(len(stakes)), weights=stakes, k=n_winners)


def get_winners(stakes_df: pd.DataFrame, owner_address: str, seed: int, n_winners: int) -> list[str]:
    """
    Returns the winner(s) of the lottery.

    Args:
        stakes_df (pd.DataFrame): DataFrame with the delegators and their stakes.
        owner_address (str): Address of the owner of Candlestake.io (Nathan).
        seed (int): Seed for the random number generator.
        n_winners (int): Number of winners to find.

    Returns:
        list[str]: List of winners.
    """
    delegators = []
    amounts = []

    for i, (delegator, stake) in stakes_df.iterrows():
        if delegator == owner_address:
            continue
        delegators.append(delegator)
        amounts.append(int(stake)/(10**18))
        
    if delegators == []:
        winners = ['No delegators to win the lottery.']
    else:
        winners = [delegators[i] for i in select_proportional_winners_indices(amounts, seed=seed, n_winners=n_winners)]
    
    return winners


def main(seed: int, csv_file_path: str, n_winners: int) -> None:

    stakes_df = pd.read_csv(csv_file_path)

    winners = get_winners(
        stakes_df,
        owner_address=NATHAN_ADDRESS,
        seed=seed,
        n_winners=n_winners
    )
    winners.sort()

    print(f'///// Candlestake Lottery Results /////')
    print()
    print('Seed:', seed)
    print('Stakes CSV:', csv_file_path)
    print()
    print(f'{n_winners} winner{"s" if n_winners > 1 else ""}:')
    for winner in winners:
        print(f' - {winner}')
    print()
    print(f'///////////////////////////////////////')


if __name__ == '__main__':
    import sys

    seed = int(sys.argv[1], base=16)
    csv_file_path = sys.argv[2]
    n_winners = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    assert n_winners >= 1, 'n_winners must be >= 1'

    main(seed, csv_file_path, n_winners)