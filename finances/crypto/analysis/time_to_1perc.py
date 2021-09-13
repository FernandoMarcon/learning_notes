import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['figure.figsize']=15,10

period_name='hours'
pair='BTC/USDT'
fname='finances/crypto/data/ccxt_binance_BTC-USDT_1h_20210101-20210913.csv'

data = pd.read_csv(fname,index_col='Time')

def test_perc(high, low_ref, perc=1):
    temp = ((high/low_ref*100)-100) >= perc
    return next((i for i,e in enumerate(temp) if e), False)

def calc_perct(df,perc=1):
    return pd.Series(
                [test_perc(df.High[i:],value, perc) for i, value in enumerate(df['Low'])],
                dtype='int64',index=df.index)

perc=1
cname='tperc'+str(perc)
data[cname] = calc_perct(data,perc)

perc=2
cname='tperc'+str(perc)
data[cname] = calc_perct(data,perc)

perc=3
cname='tperc'+str(perc)
data[cname] = calc_perct(data,perc)

freq = data[cname].hist(bins=50)
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('How many {} usually takes for {} to go up {}%'.format(period_name,pair,perc))
plt.show()



data[cname].value_counts(ascending=True).tail(20).plot(kind='barh',xlabel=period_name,y='Num. of cases',
title='How long does it take until price increase in {}% after buy-order?'.format(perc))



tfreq =data[['tperc1','tperc2','tperc3']].apply(lambda x: x.value_counts())#.T.stack()

ax = tfreq.head(20).plot(kind='barh', xlabel=period_name, ylabel='Num. of cases',
                    title='How long does it take until price increase in {}% after buy-order?'.format(perc))
ax.invert_yaxis()
ax.legend(['1%','2%','3%'])
# ax.show()
