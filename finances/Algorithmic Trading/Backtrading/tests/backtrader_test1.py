import backtrader as bt
import backtrader.feeds as btfeed
from datetime import datetime

data = btfeed.GenericCSVData(
    dataname='finances/crypto/data/ccxt_binance_BTC-USDT_1h_20210101-20210913.csv',

    dtformat=('%Y-%m-%d %H:%M:%S'),
    datetime=0,
    time=-1,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    openinterest=-1
)

class PrintClose(bt.Strategy):

    def __init__(self):
        self.dataclose = self.datas[0].close

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date[0]
        print(f'{dt.isoformat()} {txt}')

    # def next(self):
    #     self.log('Close: ',self.dataclose[0])

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])

cerebro = bt.Cerebro()

# Create a data feed
# data = bt.feeds.YahooFinanceData(dataname='MSFT',fromdate=datetime(2011, 1, 1),todate=datetime(2012, 12, 31))
data = bt.feeds.YahooFinanceData(dataname='TSLA', fromdate=datetime(2021, 1, 1),todate=datetime(2021, 6, 1))
cerebro.adddata(data)

cerebro.addstrategy(PrintClose)

cerebro.run()
