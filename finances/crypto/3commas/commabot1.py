import pandas as pd
import matplotlib.pyplot as plt

#########
def SO(max_so=7,start_so=1,last_so=0,so=.02, so_step=1.1):
    if start_so == 1:
        last_so = so
    else:
        last_so = so + last_so*so_step

    if start_so < max_so:
        start_so+=1
        return SO(max_so=max_so,start_so=start_so,last_so=last_so)
    else:
        return last_so

def getSOperc(max_so=7):
    return [SO(i) for i in range(1,max_so+1)]

#########
data = pd.read_csv('finances/crypto/data/ccxt_binance_BTC-USDT_1h_20190101-20200101.csv',index_col='Time')
data.head()

def getPriceLeves(base_order, percentages):
    return [(base_order - base_order*i) for i in percentages]


# prices = data['Close'].tolist()

order_size=100
position=0
take_profit=0.01
so_flag=0

final_price = base_order
bought=0

wallet=pd.DataFrame([{'USDT':800,'BTC':0}])
maxSO=int(wallet['USDT']/amount)

for i in range(len(data)):
    price = data.Close[i]

    base_order = prices[0]
    percentages = getSOperc()
    price_levels=getPriceLeves(base_order, percentages)


    if so_flag==0 and position == 0:
        print('buy: '+str(order_size))
        wallet['BTC']+=order_size/price
        wallet['USDT'] -= order_size

    if price > (final_price + final_price*take_profit):
        print('Sell')
        wallet['USDT']+=wallet['BTC']*price
        wallet['BTC']=0

    elif price <= price_levels[so_flag]:
        so_flag+=1
        print('SO [{}] - buy: '.format(so_flag,amount))
        final_price=(price + final_price)/2
    else:
        print('Hold!!!')
        pass
