import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 20,10

#--- Read and clean data
data = pd.read_excel('finances/data/04_02_Begin.xlsx')
data = data.drop(labels=['Unnamed: 4'], axis=1)

# Parse Date column
data[['Date', 'DoW']] = data.Date.str.split(expand = True)

# Clean Date column
dow = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dow = dict(zip(dow,set(range(1, len(dow) + 1))))
data['DoW'] = data['DoW'].map(dow, data['DoW'])
data.head()

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Rename columns
data.rename(columns = {'USD to JPY': 'USD-JPY', 'JPY to THB':'JPY-THB', 'USD to THB':'USD-THB'}, inplace = True)
data.head()

#--- Visualization
data['USD-JPY'].hist()

data['JPY-THB'].hist()

data['USD-THB'].hist()


#--- Triangular Arbitrage
def calc_triangleArb(c1, c2):
    return c1 * c2

def calc_arbDelta(original, arbitrage):
    return original - arbitrage

def calc_arbProfit(investent, arbProfit, trading_cost):
    return investiment*abs(arbProfit) - trading_cost

def set_exposureLimit(profit, limit = 50):
    '''
    will only gonna trade if the profit expected is > limit
    '''
    return [0 if x < limit else x for x in profit]

def buy(profit, limit = 50):
    '''
    buy if expected profit is > limit
    '''
    return [1 if x > limit else 0 for x in profit]

investment = 1000000
trading_cost = 9

data['triangleArb'] = calc_triangleArb(data['USD-JPY'],data['JPY-THB'])
data.head()
data[['USD-THB','triangleArb']].plot()

data['ArbProfit'] = calc_arbDelta(original=data['USD-THB'], arbitrage=data['triangleArb'])
data['profits'] = calc_arbProfit(investment, data['ArbProfit'], 9)
data['profits'] = set_exposureLimit(data['profits'])
data['BuyDecision'] = buy(data['profits'])

def plot_returns(data):
    data['profits'].plot(x=data['Date'])
    plt.title('Profits using Triangle Arbitrage')
    plt.show()



plot_returns(data)

type(data['Date'])
