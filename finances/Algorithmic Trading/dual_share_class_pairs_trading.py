'''
Dual share class pairs trading

Viacom Class A and B shares - both refers to the same company, and in fact they both give you ownership in the same underlying firm and in the same underlying firm and the same share of the profits.

Assumption:
    - In theory, these two stocks ought to have exacly the same value.
    - In practice, because Viacom B share have a larger float, that is there's more shares outstanding, they tend to trade more frequently then Viacon Class A.

So, theres a relationship between these two classes of shares, we might want to try and capitalize on that relationship.
'''

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 20,10

data = pd.read_excel('finances/data/02_03_Begin.xls', index_col='Date',usecols=['Date','VIA','VIA.B'])
data.head()

#--- Ratio between VIA and VIA.B
data['Ratio'] = data['VIA'] / data['VIA.B']

print('Average Ratio: ', round(data['Ratio'].mean(), 3))
print('Ratio Variation: ', round(data['Ratio'].var(), 3))

data['Ratio'].plot(title='Ratio between Viacon Class A and Class B')

data['MA'] = data['Ratio'].rolling(14).mean()

data['buyVIA'] = data.apply(lambda x: 1 if x['VIA'] < x['MA'] else 0,axis=1)
data['buyVIA.B'] = data.apply(lambda x: 1 if x['VIA.B'] > x['MA'] else 0, axis=1)

def calc_returnLongOnly(data):
    via = data['buyVIA'] * (data['VIA'].diff()/ data['VIA'])
    via_b = data['buyVIA.B'] * (data['VIA.B'].diff()/data['VIA.B'])
    return via + via_b

def calc_returnLongShort(data):
    via = data['buyVIA'] * ((data['VIA'].diff()/data['VIA']) - (data['VIA.B'].diff()/data['VIA.B']))
    via_b = data['buyVIA.B'] * ((data['VIA.B'].diff()/data['VIA.B']) - (data['VIA'].diff()/data['VIA']))
    return via + via_b

data['Return - Long Only'] = calc_returnLongOnly(data)
data['Return - Long/Short'] = calc_returnLongShort(data)

data.head()


# data['Profit - Long Only']
# data['Profit - Long/Short']
