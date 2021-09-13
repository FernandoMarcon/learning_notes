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

def plot_freq(df):
    tfreq =df[['tperc1','tperc2','tperc3']].apply(lambda x: x.value_counts())#.T.stack()
    ax = tfreq.head(20).plot(kind='barh', xlabel=period_name, ylabel='Num. of cases',
                        title='How long does it take until price increase in {}% after buy-order?'.format(perc))
    ax.invert_yaxis()
    ax.legend(['1%','2%','3%'])
    # ax.show()

pd.starts

a=1
dv = 0.02
c=1.1

def d(a):
    return (a + a*dv*c)
a=1
initial = a + a*dv
d(initial)
d(d(initial))
d(d(d(initial)))
d(d(d(d(initial))))
d(d(d(d(d(initial)))))
d(d(d(d(d(d(initial))))))
final = d(d(d(d(d(d(d(initial)))))))
(1- final)*100

final/initial




so=.02
so_scale=1.1
max_so=7
SOs=[]
prices=[]
so_flag=0
base = 1000
start = base -1

for i in reversed(range(500,base)):
    prices.append(i)
    deviation = (start - i)/start
    if deviation >= so:
        so*=so_scale
        if so_flag <= max_so:
            start=i
            SOs.append(start)
            so_flag+=1
        else:
            SOs.append(start)
    else:
        SOs.append(start)
df = pd.DataFrame({'price':prices,'SOs':SOs})

p = df.price.plot()
[p.axhline(y=l, linestyle='--',color='red') for l in df.SOs.unique()]





so=.02
so_scale=1.1
max_so=7
so_flag=0
data = pd.read_csv('finances/crypto/data/ccxt_binance_BTC-USDT_1h_20190101-20200831.csv',index_col='Time')
start, base = data.Close[0],data.Close[0]

SOs=[]
prices=[]

for i in reversed(data.Close):
    deviation = (start - i)/start
    if deviation >= so:
        so*=so_scale
        if so_flag <= max_so:
            start=i
            SOs.append(start)
            so_flag+=1
        else:
            SOs.append(start)
    else:
        SOs.append(start)
df = pd.DataFrame({'price':data.Close,'SOs':SOs})
p = df.price.plot()
[p.axhline(y=l, linestyle='--',color='red') for l in df.SOs.unique()]
