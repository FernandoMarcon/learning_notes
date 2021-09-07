'''
Trying to understand wheter any of the prices seem artificially high or low, over a particular period of time.

Ex: Maybe the stock seems to have an artifical level of exuberance around it: people have been very excited about it, and buying pressures have pushed the prices up a little too much, and vice versa.

The simplest way to convey this idea is through moving average: smooths out some inter-day fluctuations in the stock, and gives us a better idea of where the trend is over time.
'''

import pandas as pd

data = pd.read_excel('finances/data/02_01_Begin.xlsx')
data = data.drop(index=[6841,6842], axis=0)
data.head()

#--- Transform Date varible in datetime
data['Date'] = pd.to_datetime(data['Date'])

data['MA'] = data['Adj Close'].rolling(window=14).mean()

data['MA'].plot(title='VIX\nMoving Average of 2 Weeks')
