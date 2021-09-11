import bs4 as bs
import requests
import pickle
import os
import pandas as pd
import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []

    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text
        tickers.append(ticker.replace('\n', ''))

    if not os.path.exists('data'):
        os.makedirs('data')

    with open("data/sp500tickers.pickle", 'wb') as f:
        pickle.dump(tickers, f)

    return tickers

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('data/sp500tickers.pickle', 'rb') as  f:
            tickers = pickle.load(f)

    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker.replace('.','-'), 'yahoo', start, end)
            df.to_csv('stocks_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

def compile_data():
    with open('data/sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    stock_files = os.listdir('stocks_dfs')
    for f in stock_files:
        ticker = f.replace('.csv','')
        print(ticker)

        df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

    print(main_df.head())
    main_df.to_csv('data/sp500_joined_closes.csv')

def visualize_data():
    df = pd.read_csv('data/sp500_joined_closes.csv')
    df_corr = df.corr()

    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap =plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor = False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_lables = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_lables)
    ax.set_yticklabels(column_lables)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()

os.getcwd()
# os.chdir('sentdex_tutorial/')
# save_sp500_tickers()
# get_data_from_yahoo()
compile_data()
visualize_data()
