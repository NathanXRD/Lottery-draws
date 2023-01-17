# Lottery-draws
Lottery draws of [Candlestake.io](https://candlestake.io), staking service for Radix

## How to verify the results

The script determining the winner is `get-winner.py`.

It must be called like this: `python get-winner.py <seed> <path_to_candidates_csv> <n_winners>`.

`seed` is the random function seed, which will make the result reproducible and verifiable. Typically it will be the hash of the first Bitcoin block mined after the draw.

`path_to_candidates_json` is the path to a CSV extracted directly from the Radix API call named `account.get_info`.

A correct use would be:

```bash
python3 ./get-winner.py 0000000000000000000bb6435ae10d81d962a6714d9a6d1e8db3cee38303902f 'Draws\Sample\sample.csv' 2
```

Which displays:
```powershell
///// Candlestake Lottery Results /////

Seed: 1121783408069534878293918418128988563240585841701261359
Seed (hex): 0xbb6435ae10d81d962a6714d9a6d1e8db3cee38303902f
Stakes CSV: Draws\Sample\sample.csv

2 winners:
 - rdx1qspempdukh3fqk298r735g7m8g4c8luee8czndq63wp7k5j9qtvw5yqjvj8aw
 - rdx1qsptzay9m3de57du6yrspyxsyku09r5msr48ewuucpyp7eue6hc3scspcu6t9

///////////////////////////////////////
```

In this case, the addresses of the winners are `rdx1qspempdukh3fqk298r735g7m8g4c8luee8czndq63wp7k5j9qtvw5yqjvj8aw` and `rdx1qsptzay9m3de57du6yrspyxsyku09r5msr48ewuucpyp7eue6hc3scspcu6t9`. Congratulations to them for winning this 0 XRD lottery! 🎉🎉🎉

## Note

 - Lotteries from 1 to 9 (included) were performed using `Unused/get-winner-old-1.py`.
 - Lotteries from 10 to 19 (included) were performe using `Unused/get-winner-old-2.py`.
 - Lotteries from 20 to 37 (included) were performed using `Unused/get-winner-old-3.py`.

Starting from the 38th lottery, the script called `get-winner.py` is the one we will use.