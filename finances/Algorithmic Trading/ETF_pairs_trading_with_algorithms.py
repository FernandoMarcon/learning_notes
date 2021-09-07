'''
ETF Pairs Trading
OIH: ETF that's focused on oil producers
XOP: Also an oil company-based ETF
USO: The price of oil

Assumption: These two ETFs should move in sync with one another.
'''
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 20,10

data = pd.read_excel('finances/data/02_02_Begin.xlsx',index_col='Date',usecols=[0,1,2,3])
data.head()

#--- Visualize ETFs
data[['OIH','XOP']].plot(title='Oil Company-based ETFs')

#--- Visualize ETFs with Oil prices
data[['OIH','USO']].plot(title='OIH ETF and Oil Price (USO)')

data[['XOP','USO']].plot(title='XOP (ETF) and Oil Price (USO)')

#--- Correlations
cor_matrix = data[['OIH','XOP','USO']].corr()
cor_matrix.style.background_gradient(cmap='coolwarm')

print('Correlations ( OIH & XOP ): ', round(cor_matrix.loc['OIH','XOP'], 3))
print('Correlations ( OIH & USO ): ', round(cor_matrix.loc['OIH','USO'], 3))
print('Correlations ( XOP & USO ): ', round(cor_matrix.loc['XOP','USO'], 3))

# Correlations between ETFs are higher than correlations between ETFs and oil prices: while OIH and XOP do tend to move in sync with one another, other factors probably drive the price.

# How to capitalize on this?
# - look at the ratio between OIH and XOP

#--- OIH/XOP Ratio
data['Ratio'] = data['OIH'] / data['XOP']
data['Ratio'].plot(title = 'Ratio between OIH and XOP')

print('Average Ratio: ', round(data['Ratio'].mean(), 3))
print('Ratio Variation:', round(data['Ratio'].var(),3))

# Is there some way we could determine if we should buy OIH or XOP?
# - Buy OIH when the ratio is relatively low, and XOP and its relatively high.
def buy(ratio):
    if ratio < 0.65: return 'OIH'
    elif ratio > 0.8: return 'XOP'
    else: return None

data['Buy'] = data['Ratio'].apply(lambda x: buy(x))

data.Buy.value_counts()
