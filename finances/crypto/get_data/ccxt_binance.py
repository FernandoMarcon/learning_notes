#!/usr/bin/python
import numpy as np
import pandas as pd
import ccxt
import calendar
from datetime import datetime, date, timedelta

binance = ccxt.binance()

def min_ohlcv(dt, pair, limit):
    # UTC native object
    since = calendar.timegm(dt.utctimetuple())*1000
    ohlcv1 = binance.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv2 = binance.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv = ohlcv1 + ohlcv2
    return ohlcv

def ohlcv(dt, pair, period='1d'):
    ohlcv = []
    limit = 1000
    if period == '1m':
        limit = 720
    elif period == '1d':
        limit = 365
    elif period == '1h':
        limit = 24
    elif period == '5m':
        limit = 288
    for i in dt:
        start_dt = datetime.strptime(i, "%Y%m%d")
        since = calendar.timegm(start_dt.utctimetuple())*1000
        if period == '1m':
            ohlcv.extend(min_ohlcv(start_dt, pair, limit))
        else:
            ohlcv.extend(binance.fetch_ohlcv(symbol=pair, timeframe=period, since=since, limit=limit))
    df = pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Time']]
    df['Open'] = df['Open'].astype(np.float64)
    df['High'] = df['High'].astype(np.float64)
    df['Low'] = df['Low'].astype(np.float64)
    df['Close'] = df['Close'].astype(np.float64)
    df['Volume'] = df['Volume'].astype(np.float64)
    df.set_index('Time', inplace=True)
    return df

# pair = 'BTC/USDT'
# period = '1h'
# start_date ='20190101'
# end_date = '20200101'
# df = ohlcv([start_date,end_date], pair, period)
# print(df.head())
# df.to_csv('data/ccxt_binance_'+pair.replace('/','-')+'_'+period+'_'+start_date+'-'+end_date+'.csv')

def get_datelist(start_day, end_day):
    start_dt = datetime.strptime(start_day, "%Y%m%d")
    end_dt = datetime.strptime(end_day, "%Y%m%d")
    days_num = (end_dt - start_dt).days + 1
    datelist = [start_dt + timedelta(days=x) for x in range(days_num)]
    datelist = [date.strftime("%Y%m%d") for date in datelist]
    return datelist


pair='BTC/USDT'
start_day = "20210101"
end_day = "20210913"
period='1h'

datelist = get_datelist(start_day, end_day)
df = ohlcv(datelist, 'BTC/USDT', '1h')
print(df.head())
print(df.tail())

fname='data/ccxt_binance_'+pair.replace('/','-')+'_'+period+'_'+start_day+'-'+end_day+'.csv'
df.to_csv(fname)
