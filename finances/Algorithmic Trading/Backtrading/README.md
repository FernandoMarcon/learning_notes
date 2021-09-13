# Backtrading

To backtest a trading strategy using Python, you can:
  1) run your backtests with pre-existing libraries,
  2) 2) build your own backtester, or
  3)  3) use a cloud trading platform.

There are 2 popular libraries for backtesting:
  1. [Backtrader](https://www.backtrader.com/)
  2. [Zipline](https://www.zipline.io/)

## Backtrader
It's a Python library that aids in strategy development and testing for traders of the financial markets.

It is an open-source framework that allows for strategy testing on historical data.

It can be used to optimize strategies, create visual plots, and can even be used for live trading.

### Pros:
- **_Backtesting_** – This might seem like an obvious one but Backtrader removes the tedious process of cleaning up your data and iterating through it to test strategies. It has built-in templates to use for various data sources to make importing data easier.
- **_Optimizing_** – Adjusting a few parameters can sometimes be the difference between a profitable strategy and an unprofitable one. After running a backtest, optimizing is easily done by changing a few lines of code.
- **_Plotting_** – If you’ve worked with a few Python plotting libraries, you’ll know these are not always easy to configure, especially the first time around. A complex chart can be created with a single line of code.
- **_Indicators_** – Most of the popular indicators are already programmed in the Backtrader platform. This is especially useful if you want to test out an indicator but you’re not sure how effective it will be. Rather than trying to figure out the math behind the indicator, and how to code it, you can test it out first in Backtrader, probably with one line of code.
- **_Support for Complex Strategies_** – Want to take a signal from one dataset and execute a trade on another? Does your strategy involve multiple timeframes? Or do you need to resample data? Backtrader has accounted for the various ways traders approach the markets and has extensive support.
- **_Open Source_** – There is a lot of benefit to using open-source software
- **_Active Development_** – This might be one area where Backtrader especially stands out. The framework was originally developed in 2015 and constant improvements have been made since then. Just a few weeks ago, a pandas-based technical analysis library was released to address issues in the popular and commonly used TA-Lib framework. Further, with a wide user base, there is also active third-party development.
- **_Live Trading_** – If you’re happy with your backtesting results, it is easy to migrate to a live environment within Backtrader. This is especially useful if you plan to use the built-in indicators offered by the platform.


## Overview
The library’s most basic functionality is to iterate through historical data and to simulate the execution of trades based on signals given by your strategy.

- A Backtrader “analyzer” can be added to provide useful statistics.

- Strategy: This is where all the logic goes in determining and executing your trade signals. It is also where indicators can be created or called, and where you can determine what get’s logged or printed to screen.
  - The cerebro engine is the core of Backtrader. This is the main class and we will add our data and strategies to it before eventually calling the cerebro.run() command.

Basic Backtrader setup

```Python
import backtrader as bt

class MyStrategy(bt.Strategy):
    def next(self):
        pass # do something

# Instantiate Cerebro
cerebro = bt.Cerebro()

# Add strategy to Cerebro
cerebro.addstrategy(MyStrategy)

# Run Cerebro Engine
cerebro.run()
```

- `log()` allows us to pass in data via the txt variable that we want to output to the screen.
- `next()` gets called every time Backtrader iterates over the next new data point.

## Source
[algotrading101 - Backtrader for backtesting](https://algotrading101.com/learn/backtrader-for-backtesting/)
