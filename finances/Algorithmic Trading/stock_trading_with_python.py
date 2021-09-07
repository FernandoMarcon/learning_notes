'''
Stock Trading with Python
source: Algorithmic Trading and Finance Models with Python, R, and Stata Essential Training (LinkedIn Course)
'''
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data

#### --------------- Data Retrieval --------------- ####
#--- Yahoo Finances
df = data.get_data_yahoo('MSFT', '2018-01-01', '2019-01-01')
df.head()

#--- Quandl
# !pip install quandl
import quandl
aapl = quandl.get('WIKI/AAPL',start_date='2014-01-01', end_date='2016-01-01')
aapl.describe()

#--- Financial Data Manipulation, Storage and Visualization
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 20,10
import pandas_datareader as reader
import datetime

# Store data as CSV file
aapl=reader.get_data_yahoo('AAPL', start=datetime.datetime(2008,1,1), end=datetime.datetime(2012,1,1))
aapl.describe()

aapl.to_csv('finances/data/aapl_02_04.csv')
download_aapl='02_04CSV.csv'

# Create new variables
aapl['Change'] = aapl.Open - aapl.Close
aapl['Pct_Chg'] = aapl.Change/aapl.Open

# Plot Percent Change
aapl['Pct_Chg'].plot(grid=True)

#--- Building financial databases
def get(tickers, startdate, enddate):
    def data(ticker):
        return(reader.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas=map(data, tickers)
    return pd.concat(datas, keys=tickers, names=['Ticker', 'Date'])

tickers = ['MSFT', 'CRM','GE','MMM']
all_data = get(tickers, datetime.datetime(2015,1,1), datetime.datetime(2019,1,1))
all_data
all_data.to_csv('finances/data/alldata_02_06.csv')
