import ccxt
import ta
import config
import schedule
from ta.volatility import BollingerBands, AverageTrueRange
import pandas as pd

exchange = ccxt.binance({
    'apiKey':config.API_KEY,
    'secret':config.API_SECRET
})

# markets = exchange.load_markets()
bars = exchange.fetch_ohlcv('BTC/USDT',limit=100)

df = pd.DataFrame(bars[:-1], columns=['timestamp','open','high','low','close','volume'])
print(df)

bb_indicator=BollingerBands(df['close'])
df['upper_band'] = bb_indicator.bollinger_hband()
df['lower_band'] = bb_indicator.bollinger_lband()
df['moving_avg'] = bb_indicator.bollinger_mavg()

atr_indicator = AverageTrueRange(df['high'],df['low'],df['close'])
df['atr'] = atr_indicator.average_true_range()
df
