import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold

strategies = {
    'golden_cross':GoldenCross,
    'buy_hold':BuyHold
}

parser = argparse.ArgumentParser()
parser.add_argument('strategy', help='which strategy to run', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print('Invalid strategy, must be one of {}'.format(strategies.keys()))
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.setcash(800)

fname='data/spy_2000-2020.csv'
data = pd.read_csv(fname, index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(feed)

cerebro.addstrategy(strategies[args.strategy])
cerebro.run()
cerebro.plot()
