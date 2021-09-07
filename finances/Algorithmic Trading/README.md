# Algorithmic Trading
Financial industry is evolving, with computers playing a bigger roles. Algorithmic, or computer-driver, trading now makes up the large majority of trades - more than 90% of orders by some metrics and estimates.

## General Process
![diagram](algo_trading_general_process_diagram.png "Algorithmic Trading General Process")

## Example algorithm
- Get Time, Price, Index
- Calculate **Natural Price**
$$ Natural\ Price = Last\ Price - Relative\ Index\ Change * Std.\ Dev.$$
- **Buy/No Buy**
  - if( Natural Price > Price ): _Buy_
  - else: _No Buy_

## Basics
Algo Trading relies on programmable objective criteria, and essentially comes in two flavors:

- Market making: Market-making trades attempt to capitalize on the bid-ask spread - typically associated with high-frequency traders

- Data mining: data-mining trades based on patterns in data, including stock prices and outside information
  - We look for correlations between stock prices and other data points

### Market making
Marketing making is based on bid-ask spreads.

**Centralized Order Book: Orders, Stacks, and Matching**
**Order types**:
  - _Market order_ - immediately
  - _Limit order_ - specific price
  - _Iceberg order_ - large single order that has been divided into smaller lots

**Order conditions**:
  - _Time in force_
  - _Day order_ - valid only for less than a day
  - _Good till cancelled_ - valid until executed or cancelled
  - _Fill or kill_ - immediately execute or cancel

**Conditional Orders**:
  - _Stop order_ - to sell/buy when the price of a security falls/rises to a designated level
  - _Stop limit order_ - executed at the exact price or better

**Discretionary order**:
  - Traditional orders
  - Broker decides when and price

## Steps in Building an Algo
- Define trading hypothesis and goal
- Set operating time horizon and constraints
- Algo testing

**Maintaining an Algorithm**
- Continual monitoring and maintenance
  - Monitor performance
  - Monitor market conditions
- Maintenance and rejuvenation

**Algorithmic Trading Requirements**
- Centralize order book
- Access to the (highly liquid) markets
- Systems (three types):
  - In-house systems
  - Client systems
  - Vendor systems
- Information exchange

## An Algo Trading Example
- Renaissance Technologies is one of the most famous hedge funds pursuing algorithmic trading. RenTech gave an [example](www.bloomberg.com/news/articles/2016-11-21/how-renaissance-s-medallion-fund-became-finance-s-blackest-box) of the type of trade they pursue:
  - When skies are cloudy, equities markets tend to perform worse then when skies are clear
  - In theory, we can buy or sell based on data about weather forecasts then
  - Practically speaking it's hard to trade on weather patterns - they are imprecise and the correlations are low
  - Correlations between stock prices and weather are low
- Another [example](www.econ.yale.edy/~shiller/behfin/2006-04/cohen-frazzini.pdf) of algo trading is supplier/customer realtionships
  - When a samall firm reports earnings, it has implications for other large companies that are custormers or suppliers of that small company
  - Think Apple and some of the small vendors it uses

## Types of trading
- Long-term trading, spaning several days before a trade is made.
- Intraday trading, a high-frequency trade done in a single day, between the market opens and closes.

## Big Data in Finance
- Two ways of making investment decisions:
  - Intuition
  - Data
- Each method has adherents

### Data
#### Quantitative
> refers to using data to try and identify attractive investment opportunities.

- Smart beta vs. fundamentals vs. technicals

**Stock Price Data**
Usually comes with the following information:
- _Date_
- _Open_: is the price that a stock opens at in any given day.
- _High_: the highest price for a stock in any given day.
- _Low_: the lowest price for a stock in any given day.
- _Close_: Is the price that a stock closes at any given day.
- _Adj. Close_: This price represents not just the close on a particular day, but the close after taking into account any dividends that are paid out. Not all stock pay out dividends, but if it do pay out a dividend the stock price is automatically adjusted to compensate for that.

#### Qualitative
**Textual Data**
Knowledge field known as Textual Analysis, Natural language processing, Sentiment analysis, content analysis, computational linguistics.

Pull qualitative information and transform into quantitative signals that can be used in a model

A dictionary/list of words and their associated content (positive, negative, etc.) is required for sentiment analysis in text.

Increased inerest attributable to:
  - Bigger, faster computers
  - Availability of large quantities of text
  - New technologies derived from search engines

Examples of textual data sources:
- EDGAR (1994-2011) - 22.7 million filings
- WSJ News Archive (2000 to present) - XML encapsulated
- Audio transcripts (such as conference calls) - [SeekingAlpha](Seekingalpha.com)
- Websites
- Google searchs
- Twitter/StockTwits

Textual Analysis Softwares:
- Block boxes, such as WordStat, Lexalytics, Diction
- Two critical components:
  - Ability to download data and convert into string/character variable
  - Ability to parse large quantities of text
  - Most modern languages provide for both of these functions (Perl, Python, SAS Text Miner, VB.NET)

### Why is Big Data Important?
**Avoid the HiPPO**
In the absence of data, business decisions are often made by the HiPPO (highest paid person's opinion).

### Big Data Project Steps
All big data projects require the same set of steps:
1. Gather and clean data
2. Analyze data
3. Test choice with data
4. Make a decision

## Regression Analysis
Regression analysis can be user as business tool for prediction

$$y = ax + b$$

A regression predicts the dependent variable ($y$) based upon values of the independent variables ($x$)
- Simple regression --> fits straight line to the data
- Multiple regression --> fits a straight line using several independent variables

### Predictions and Errors
Steps to prediction
1. Run regression
2. Save coefficients (e.g., impact of each inch of insulation)
3. Use _coefficients_ and _expected values_ for the future to get prediction

Ex:
$$Estimated\ Heating\ Oil = 526.15 - 5.432 (Temperature) - 20.012 (Insulation)$$

For each observation, the variation can be described as:
$$y = \hat{y} + ϵ$$
$y$: actual, $\hat{y}$: explained, $ϵ$: error


## Algorithmic Strategies
- _Mean Reversion_
  - Simplest strategies are based on mean reversion
  - Pairs trades: Walgreens and CVS, Ford and GM, etc.

- _Four-Factor Model_
  - Four-factor model of Fama and French
  - Identifies characteristics of firms that do well on average over time
  - Uses portfolios of companies with these characteristics
  - Too much noise in individual stocks
  - Stock returns predicted by factors
  - _Size_: market of the firm
    - Smal firms have higher returns than large firms over time
  - _Book-to-market (B/M) value_: proxy for firm valuation
    - Firms with higher B/M ratios have higher returns
    - Book value is accounting metric
    - B/M appears to be an indicator for financial distress
    - Distressed firms sometimes bounce back strongly
  - _Beta_: measures volatility of a stock
    - A beta of 1 means correlation of 1 between stock market and the firm. When market rises 1%, the stock on average rises 1% as well
    - A beta of 2 means a market rise of 1% is associated with a stock rise of 2%
  - _Momentum_: related to the concept of a "hot hand"
    - Companies that have done well in the recent past continue to do well in the future
    - Momentum can be measured by earnings or stock price

## Building Algorithms

## Algorithmic Trading with Python
- [Stock Trading with Python](https://github.com/FernandoMarcon/learning_notes/blob/main/finance/stock_trading_with_python.py)
- [Trying to understand wheter any of the prices seem artificially high or low, over a particular period of time.]()
- [ETF Pairs Trading]()
- [Dual share class pairs trading]()

## Algorithmic Trading with R
- [R and Bond Trading](https://github.com/FernandoMarcon/learning_notes/blob/main/finance/r_and_bond_trading.R)

## Algo Trading as a Carrer
- What do algo traders do?
- What skills do they need?
- How does the job/team work?
- [LinkedIn](https://www.linkedin.com/jobs/search/?keywords=algorithmic%20trading&location=Worldwide)

Typical Job Description
- Design of frameworks and functionality for development of trading algos
- Implementation, testing, and production
- System tuning and optimization
- Calibration and optimization of parameters
- Proactive identification of problems and issues and resolution of them

## Sources:
- [Algorithmic Trading and Finance Models with Python, R, and Stata Essential Training (LinkedIn Course)](https://www.linkedin.com/learning/algorithmic-trading-and-finance-models-with-python-r-and-stata-essential-training/)
- [Algorithmic Trading and Stocks Essential Training](https://www.linkedin.com/learning/algorithmic-trading-and-stocks-essential-training/)
