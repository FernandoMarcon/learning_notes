# https://towardsdatascience.com/cryptocurrencies-the-new-frontier-part-1-940e787c7ab9
# https://towardsdatascience.com/cryptocurrencies-the-new-frontier-part-2-7218c6a489f9
# https://github.com/JoBe10/Mean_Variance_Portfolio_Optimisation/blob/master/Efficient_Frontiers_Cryptos.ipynb

# Measures in finance
## return: the % change in the stock price over a given ime interval
### - rate of return
### - logarithmic return

## rate of return vs. logarithmic return: https://chandlerfang.com/2017/01/09/arithmetic-vs-logarithmic-rates-of-return/

## volatility: standard deviation of the return

## expected return of the total portfolio is the weighted average of the expected returns of the individual stocks in the portfolio.

## expected variance of the portifolio is a product of the variance of the individual stocks, their respective weights in the overall portfolio and the correlation between each pair of stocks.

# Mean-Variance Analysis
## aka, Modern Portfolio Theory (MPT)
## Harry Markowitz, 1952
## main ideia: by tweaking the weights of individual assets in a portfolio it is possible to construct optimal portfolios, which offer the maximum possible expected return for a given level of risk.
## key insight: an individual asset's return and volatility should not be assessed by itself, but rather by how it contributes to a portfolio's overall return and volatility.
## The optimal portofolios can be plotted on a graph where the line that connects the optimial portfolios will be an upward sloping hyperbola, which is called the Efficient Frontier.
## "Efficient" because the portfolios that lie on it provide the highest expected return for a given level of risk.


#### =============== Extract Stock Prices from Yahoo Finance =============== ####
# Gathering the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas_datareader as dr
from pandas_datareader import data
from datetime import datetime
import cvxopt as opt
from cvxopt import blas, solvers

# Define start and end date
end = datetime(2020, 7, 9)
start = datetime(2015, 8, 6)

# Create a list of the ticker symbols to be used in this project
tickers = ['AMZN', 'GOOGL', 'JNJ', 'V', 'PG', 'UNH', 'JPM', 'HD', 'VZ', 'NFLX', 'DIS', 'MRK', 'PEP', 'BAC', 'KO',
           'WMT','CVX', 'ABT', 'AMGN', 'MCD', 'COST', 'NKE', 'PM', 'QCOM', 'LOW', 'BA', 'LMT', 'SBUX', 'UPS', 'CAT']

# Obtain the adjusted closing prices from Yahoo Finance
prices = pd.DataFrame()
for tick in tickers:
    prices[tick] = data.DataReader(tick, data_source = 'yahoo', start = start, end = end)['Adj Close']
prices.columns = tickers

prices

# Plot the time series
normalised = prices / prices.iloc[0] * 100
normalised.plot(figsize=(20, 10))
plt.title('Stock Time Series 2015 - 2020', fontsize=20)

#--- Mean-Variance Portfolio Allocation
# Calculate the log returns
log_r = np.log(prices / prices.shift(1))

# Compute the annualised returns
annual_r = log_r.mean() * 255
annual_r
# Under the assumptions of independent and identically distributed returns we can also annualise the covariance matrix using trading days.

cov_matrix = log_r.cov() * 255
var = log_r.var() * 255

# Next, I will generate random weights for all of the 30 stocks, which will make up the randomly generated portfolios, under a combination of assumptions. The assumptions are that only long positions are allowed, which ultimately means that the investor's wealth has to be divided among all available stocks through positive positions, and the positions have to add up to 100%, i.e. no additional borrowing and investing more than 100% of wealth.
# Get the total number of stocks used
num_stocks = len(tickers)

# Generate 30 random weights between 0 and 1
weights = np.random.random(num_stocks)

# Constrain these weights to add up to 1
weights /= np.sum(weights)
weights
# Assuming that historical mean performance of the stocks making up the portfolio is the best estimator for future, i.e. expected, performance, expected portfolio return can be calculated as a product of the transpose of the weights vector and the expected returns vector of the stocks making up the portfolio.
# Example of what the portfolio return would look like given the above weights
ptf_r = np.sum(annual_r * weights)
ptf_r

# Given the portfolio covariance matrix computed above, the expected portfolio variance can be calculatd as the dot product of the transpose of the weights vector, the covariance matrix and the weights vector.
# Compute portfolio variance
ptf_var = np.dot(weights.T, np.dot(cov_matrix, weights))
ptf_var

# Using the computational concepts introduced so far we can generate many random portfolios and plot their returns against their risk (standard deviation), often referred to as volatility.
# Define a function to generate N number of random portfolios given a DataFrame of log returns
def generate_ptfs(returns, N):
    ptf_rs = []
    ptf_stds = []
    for i in range(N):
        weights = np.random.random(len(returns.columns))
        weights /= np.sum(weights)
        ptf_rs.append(np.sum(returns.mean() * weights) * 252)
        ptf_stds.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights))))
    ptf_rs = np.array(ptf_rs)
    ptf_stds = np.array(ptf_stds)
    return ptf_rs, ptf_stds

# Comparing portfolio returns and volatilities across portfolios is made a lot easier by computing a ratio of the two measures. The most common ratio that takes into consideration is the Sharpe ratio, which is a measure of the amount of excess return an investor can expect per unit of volatility (remember this is a measure of risk) that a portfolio provides. Because we assume that investors want to maximise returns while minimising risk, the higher this ratio the better.
# Generate the return and volatility of 5000 random portfolios
ptf_rs, ptf_stds = generate_ptfs(log_r, 5000)

# Plot the 5000 randomly generated portfolio returns and volatilities and colormark the respective Sharpe ratios
plt.figure(figsize=(15,8))
plt.scatter(ptf_stds, ptf_rs, c = (ptf_rs - 0.01)/ptf_stds, marker = 'o')
plt.grid(True)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label = 'Sharpe Ratio')
plt.title('5000 Randomly Generated Portfolios In the Risk-Return Space')

# Finding the optimal portfolios requires a constrained optimisation in which we maximise the Sharpe ratio. To begin, we need a function that returns the portfolio statistics that we computed previously, namely weights, portflio return, portfolio volatility and, based on the latter two, the portfolio Sharpe ratio.
# Define a function that returns the portfolio statistics
def ptf_stats(weights):
    weights = np.array(weights)
    ptf_r = np.sum(log_r.mean() * weights) * 252
    ptf_std = np.sqrt(np.dot(weights.T, np.dot(log_r.cov() * 252, weights)))
    return np.array([ptf_r, ptf_std, (ptf_r - 0.01) / ptf_std])

# Import the optimize sublibrary
import scipy.optimize as sco

# Minimize the negative value of the Sharpe ratio
def min_sharpe(weights):
    return -ptf_stats(weights)[2]

# Write the constraint that the wights have to add up to 1
cons = ({'type':'eq', 'fun': lambda x: np.sum(x) - 1})

# Bound the weights (parameter inputs) to be within 0 and 1
bnds = tuple((0,1) for x in range(num_stocks))

# Starting parameter (weights) list as equal distibution
starting_ws = num_stocks * [1. / num_stocks, ]

# Call the minimisation function
opts = sco.minimize(min_sharpe, starting_ws, method='SLSQP', bounds = bnds, constraints=cons)
opts
# In the results of the optimisation, the variable x stores the weights for the stocks making up the optimal portfolio. In the case of the 30 US stocks, there seem to be quite a few stocks with weights of zero, i.e. no capital allocated to them.
# Obtain the optimal weights
weights_opt = opts['x'].round(3)
weights_opt
# Plugging these weights into the portfolio statistics function above we can get the expected return, expected volatility and Sharpe ratio of the portfolio with the optimal weights.
# Plug optimal weights into the statistics function
ptf_stats(weights_opt)
# expected return:
ptf_stats(weights_opt)[0]

# expected volatility:
ptf_stats(weights_opt)[1]

# Sharpe ratio:
ptf_stats(weights_opt)[2]

# Next, we can obtain the absolute minimum variance portfolio. As the name suggests, in order to obtain this portfolio, we minimise the portfolio variance.
# Define a function that minimises portfolio variance
def min_var(weights):
    return ptf_stats(weights)[1]**2

# Call the optimisation function
opt_var = sco.minimize(min_var, starting_ws, method = 'SLSQP', bounds = bnds, constraints=cons)
opt_var

# For the absolute minimum variance portfolio, more portflios are invested in or, put differently, there are less stocks with weighst of zero.
# Obtain the optimal weigths
weights_opt_var = opt_var['x'].round(3)
weights_opt_var

# Get the statistics for the absolute minimum variance portfolio
ptf_stats(weights_opt_var)




# Using the same logic applied previously, we can compute all optimal portfolios, i.e. all portflios with the maximum return for a given risk level, by iterating over multiple starting conditions.
# Set up two conditions, one for the target return level and one for the sum of the portfolio weights
cons2 = ({'type':'eq', 'fun':lambda x: ptf_stats(x)[0] - r},
        {'type':'eq', 'fun':lambda x: np.sum(x) - 1})
# The boundary condition stays the same
bnds2 = tuple((0,1) for x in weights)

# return the volatility of a portfolio given a vector of weights
def min_port(weights):
    return ptf_stats(weights)[1]

# Get the target and volatilities given a range of returns
def efficient_frontier(start_r, end_r, steps):
    target_rs = np.linspace(start_r, end_r, steps)
    target_stds = []
    for r in target_rs:
        cons2 = ({'type':'eq', 'fun': lambda x: ptf_stats(x)[0] - r},
                {'type':'eq', 'fun': lambda x: np.sum(x) - 1})
        bnds2 = tuple((0,1) for x in weights)
        res = sco.minimize(min_port, starting_ws, method = 'SLSQP', bounds = bnds2, constraints = cons2)
        target_stds.append(res['fun'])
    target_stds = np.array(target_stds)
    return target_rs, target_stds

# Based on the random portfolio visualisation above it seems as though a target return of 30% would be a good upper bound
# Obtain the target returns and volatilities based on 50 target returns
target_rs, target_stds = efficient_frontier(0.0, 0.30, 50)

# Plot the efficient frontier in the same visualisation as the randomly generted portfolios
plt.figure(figsize=(15, 8))
plt.scatter(ptf_stds, ptf_rs, c=(ptf_rs - 0.01) / ptf_stds, marker = 'o')
plt.scatter(target_stds, target_rs, c = (target_rs - 0.01)/target_stds, marker = 'x')
plt.plot(ptf_stats(opts['x'])[1], ptf_stats(opts['x'])[0], 'r*', markersize=20.0)
plt.plot(ptf_stats(opt_var['x'])[1], ptf_stats(opt_var['x'])[0], 'b*', markersize=20.0)
plt.grid(True)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.xlim(0.14, 0.24)
plt.colorbar(label = 'Sharpe Ratio')
plt.title('Efficient Frontier Using 30 US Stocks')
# Blue star: the absolute minimum variance portfolio.
# Red star: the absolute maximum Sharpe ratio portfolio.
# Any portfolio that lies on the frontier but is below the blue star is not an optimal or efficient portfolio as it does not dominate all other portfolios in terms of expected return givven a certain risk level but rather is dominated by the others.

# why is the efficient frontier so far away from the cluster of randomly selected portfolios?
# the portfolio weights used to randomly generate the random portfolios lie between 0 and 1. This means that every stock in the portfolio has at least some positive weight.
# in both the absolute minimum variance portflio as well as the maximum Sharpe ratio portfolio a lot of the stocks in the portflio have a weight of zero. This is because the minimisation function determined the optimal weights for each stock in the portfolio based on the stocks expected return and covariance with all other stocks. Due to the expected return and covariance profiles of some stocks, the optimal weight for those just happened to be zero.

# In order to understand this further, I will use the very first set of randomly selected weights from early in this project and include its expected return and expected volatility in the above visualisation. In the visualisation below, the white star represents the portfolio based on the initially generated random weights.
# Include the initially generated random weights
plt.figure(figsize=(15, 8))
plt.scatter(ptf_stds, ptf_rs, c = (ptf_rs - 0.01)/ptf_stds, marker = 'o')
plt.scatter(target_stds, target_rs, c=( target_rs - 0.01)/target_stds, marker = 'x')
plt.plot(ptf_stats(opts['x'])[1], ptf_stats(opts['x'])[0], 'r*', markersize=20.0)
plt.plot(ptf_stats(opt_var['x'])[1], ptf_stats(opt_var['x'])[0], 'b*', markersize=20.0)
plt.plot(ptf_stats(weights)[1], ptf_stats(weights)[0], 'w*', markersize=20.0)
plt.grid(True)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.xlim(0.14, 0.24)
plt.colorbar(label='Sharpe Ratio')
plt.title('Efficient Frontier Using 30 US Stocks')

# portfolio composition of the maximum Sharpe ratio portfolio and the one represented by the white star.
# Create DataFrame of the weights assigned to each ticker
composition = {'Expected Return': annual_r.round(3), 'Maximum Sharpe':weights_opt, 'White Star':weights.round(3)}
comp = pd.DataFrame(composition, columns = ['Expected Return', 'Maximum Sharpe', 'White Star'], index = tickers)
comp.head()

# Inspect the correlation matrix
corr_matrix = log_r.corr()
corr_matrix


# Capital Market Line
