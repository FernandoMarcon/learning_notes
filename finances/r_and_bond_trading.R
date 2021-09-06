##########
#= Bond Trading with R
#= source: Algorithmic Trading and Finance Models with Python, R, and Stata Essential Training (LinkedIn Course)
##########

#--- Load Libraries
library(quantmod)

#--- Data Retrieval and Visualization with `quantnid`
# Get Apple (AAPL) Stock Prices
getSymbols('AAPL')
head(AAPL)

barChart(AAPL)

barChart(AAPL, subset='last 28 days')

# Get Microsoft (MSFT) Stock Prices
rm(AAPL)
getSymbols('MSFT')
chartSeries(MSFT)

addMACD()

addBBands()

chartSeries(MSFT, subset='last 60 days')

addMACD()

addBBands()

#--- Data Analysis
summary(MSFT)

library(BatchGetSymbols)

first.date <- Sys.Date() - 60
last.date <- Sys.Date
freq.data <- 'daily'
tickers <- c('MSFT','AAPL','SPY')
df.SP500 <- GetSP500Stocks()
tickers <- df.SP500$Tickers

#--- Regressions
linearMod <- lm(Cash ~ EBITDA, data = x03_05_Start_R)
print(linearMod)
