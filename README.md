# Lottery-draws
Lottery draws of [Candlestake.io](https://candlestake.io), staking service for Radix

## How to verify the results

The script determining the winner is `get-winner.py`.

It must be called like this: `python get-winner.py <seed> <path_to_candidates_json>`.

`seed` is the random function seed, which will make the result reproducible and verifiable. Typically it will be the hash of the first Bitcoin block mined after the draw.

`path_to_candidates_json` is the path to a JSON extracted directly from the Radix API call named `account.get_info`.

A correct use would be:

```bash
python3 ./get-winner.py 0000000000000000000bb6435ae10d81d962a6714d9a6d1e8db3cee38303902f 'Draws\Sample\sample.csv'
```

Which displays:
```bash
Winner: rdx1qsptzay9m3de57du6yrspyxsyku09r5msr48ewuucpyp7eue6hc3scspcu6t9
Seed: 1121783408069534878293918418128988563240585841701261359
Stakes CSV: Draws\Sample\sample.csv
```

In this case, the winning address is `rdx1qsptzay9m3de57du6yrspyxsyku09r5msr48ewuucpyp7eue6hc3scspcu6t9`. Congratulations to them for winning this 0 XRD lottery! 🎉🎉🎉

## Note

The lotteries from 1 to 9 (included) were performed using `Unused/get-winner-old-1.py`.

Lotteries from 10 to 19 (included) were performe using `Unused/get-winner-old-2.py`.

Starting from the 20th lottery, the script called `get-winner.py` is the one we will use.