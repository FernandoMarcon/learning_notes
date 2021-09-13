import os

closing_price_sum=0
window = 200
with open('finances/Algorithmic Trading/golden_cross_and_backtrader/data/spy_2000-2020.csv') as f:
    content = f.readlines()[-window:]
    for line in content:
        print(line)
        tokens = line.split(',')
        close = tokens[4]

        closing_price_sum += float(close)

print(closing_price_sum / window)
