import json
import random

def get_proportional_random(l, seed):
    """
    Params:
    `l` is a list of strictly positive numbers.

    Returns:
    Returns the index of the number chosen randomly.
    Let `S` be the sum of the elements of `l`, then
    any number `x` has a chance of winning equal to `x/S`.
    """
    random.seed(a=seed, version=2)

    hit = random.uniform(0, sum(l))
    for i, amount in enumerate(l):
        if hit < amount:
            return i
        hit -= amount


def get_winner(stakes_json, owner_address, seed):
    delegators = []
    amounts = []

    for stake in stakes_json:
        if stake['delegator'] == owner_address:
            continue
        delegators.append(stake['delegator'])
        amounts.append(int(stake['amount'])/(10**18))
        
    if delegators == []:
        winner = 'No delegators to win the lottery.'
    else:
        winner = delegators[get_proportional_random(amounts, seed=seed)]
    
    return winner


def main(seed, json_file):

    with open(json_file, 'r') as f:
        stakes_json = json.load(f)['result']['epochInfo']['current']['stakes']

    winner = get_winner(
        stakes_json,
        owner_address='rdx1qsphe3yjc89s2jqlkjcpr6hapee6hjvqn0kt57m4zyze92us8m9t2mcpeqdz2',
        seed=seed
    )

    print('Winner:', winner)
    print('Seed:', seed)
    print('Stakes json:', json_file)


if __name__ == '__main__':
    import sys
    main(int(sys.argv[1], base=16), sys.argv[2])