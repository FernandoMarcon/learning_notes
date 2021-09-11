import datetime as dt
import matplotlib.pyplot as plt
# from matplotlib.finance import candlestick_ohlc
import mplfinance as mpf
from mplfinance import candlestick_ohlc
from mplfinance import candlestick_ohlc
from matplotlib.finance import candlestick_ohlc

import matplotlib.dates as dates
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2000,1,1)
# end = dt.datetime(2016, 12, 31)
#U
# df = web.DataReader('TSLA','yahoo', start, end)
# df.to_csv('sentdex_tutorial/tsla.csv')

#--- Read data
df = pd.read_csv('sentdex_tutorial/tsla.csv', parse_dates=True, index_col = 0)
df.plot()

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.head()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.head()
df_ohlc.reset_index(inplace=True).values, width=2, colorup = 'g'
df_ohlc.head()
df_ohlc['Date'] = df_ohlc['Date'].map(dates.date2num)

mpf.plot(df.head(100), type='candle', style='charles',
            title='S&P 500, Nov 2019',
            ylabel='Price ($)',
            ylabel_lower='Shares \nTraded',
            volume=True,
            mav=(3,6,9))




# import required packages
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import matplotlib.dates as mpdates

plt.style.use('dark_background')

# extracting Data for plotting
df = pd.read_csv('sentdex_tutorial/tsla.csv')
df = df[['Date', 'Open', 'High', 'Low', 'Close']]
df['Date'] = pd.to_datetime(df['Date']) # convert into datetime object
df['Date'] = df['Date'].map(mpdates.date2num) # apply map function

mpf.plot(df)

# creating Subplots
fig, ax = plt.subplots()

# plotting the data
mpf.candlestick_ohlc(ax, df.values, width = 0.6,
                 colorup = 'green', colordown = 'red',
                 alpha = 0.8)

# allow grid
ax.grid(True)

# Setting labels
ax.set_xlabel('Date')
ax.set_ylabel('Price')

# setting title
plt.title('Prices For the Period 01-07-2020 to 15-07-2020')

# Formatting Date
date_format = mpdates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

# show the plot
plt.show()


len(df)

mpf.plot(df[1400:1640], type='candle', volume = True, mav=(20,40))
