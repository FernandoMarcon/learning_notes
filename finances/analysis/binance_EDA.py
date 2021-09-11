import pandas as pd
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import sys
sys.path.insert(1, '/home/marcon/Documents/exchange/')
import config

# Authenticate
client = Client(config.API_KEY, config.API_SECRET)

# Get Tickers
tickers = client.get_all_tickers()
ticker_df = pd.DataFrame(tickers)
ticker_df.set_index('symbol', inplace=True)
ticker_df.head()
ticker_df.tail()

ticker_df.loc['BTCUSDT']
# Market Depth
depth = client.get_order_book(symbol='BTCUSDT')
depth_df = pd.DataFrame(depth['bids'])
depth_df.columns = ['Price', 'Volume']
depth_df.head()

# Get Historical Data
historical = client.get_historical_klines('BTCUSDT',Client.KLINE_INTERVAL_1DAY, '1 Jan 2011')
historical
hist_df = pd.DataFrame(historical)
hist_df.columns = ['Open Time','Open','High','Low','Close','Volume','Close Time','Quote Asset Volume',
                    'Number of Trades','TB Base Volume','TB Quote Volume','Ignore']
hist_df.head()

# Preprocess Historical Data
hist_df.dtypes
hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit = 's')
hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit = 's')
numeric_columns = ['Open','High','Low','Close','Volume','Quote Asset Volume','TB Base Volume','TB Quote Volume']
hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)
hist_df.head()
hist_df.tail()
hist_df.describe()
hist_df.info()

# Viz
import mplfinance as mpf
mpf.plot(hist_df.set_index('Close Time').tail(100))
mpf.plot(hist_df.set_index('Close Time').tail(100), type = 'candle',style='charles')
mpf.plot(hist_df.set_index('Close Time').tail(100), type = 'candle',style='charles',volume=True)
mpf.plot(hist_df.set_index('Close Time').tail(120), type = 'candle',style='charles',volume=True,
    title = 'BTCUSDT Last 120 Days', mav = (10,20,30))
    
