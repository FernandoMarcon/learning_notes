'''
Data: VIX product from 2010-2017
The VIX is the market's fear gauge, is a stationary measure: over time, while it fluctuates up and down, it will always return to its' mean value. Even when it spikes, it ultimately returns, or reverts to it's mean value.
You can't buy and sell VIX directly.
Case: trade products that are associated with the VIX.
Goal: develop a trading strategy that tries to capitalize on this.
'''
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 20, 10

data = pd.read_excel('finances/data/03_02_Begin.xlsx', index_col='Date')
data.head()

#--- Desing an algorithm
data['Buy Column'] = data.apply(lambda x: 1 if x['Moving Avg. VIX'] > x['VIX'] else 0, axis=1)
data['L-5 Mean Reversion'] = data.apply(lambda x: x['Long Vol Ret'] if x['Buy Column'] == 1 else 0, axis=1)

#--- Test algorithm accuracy
data = pd.read_excel('finances/data/03_03_Begin.xlsx', index_col='Date')
data.head()

data['Stand Dev.'] = data['Adj Close'].std()
data['Moving Ave'] = data['Adj Close'].rolling(14).mean()

data[['Open','High','Low','Adj Close']].plot()


data[['Adj Close','Moving Ave']].plot(color={'Adj Close':'yellow', 'Moving Ave':'blue'},linewidth=2)


#--- One way to ensure that we're really buying the VIX at a time when it's particularly undervalued or overvalued, and thus, likely to revert to its mean, is to ensure that there is a significant portion away from its mean overtime.
# Only buy the VIX if it is at least one stardard deviation bellow its moving average, and sell if it's at least one standard deviation above its moving average.
data.apply(lambda x: 1 if (x['Adj Close'] + x['Adj Close']*x['Stand Dev.'] ) < 1 else 0 , axis=1)

def buy(data):
