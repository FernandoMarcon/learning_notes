# Introduction to Financial Markets

Financial institutions are a pillar of civilized society, directing resources across space and time to their best uses,
supporting and incentivizing people in their productive ventures, and managing the economic risks they take on. The workings
of these institutions are important to comprehend if we are to predict their actions today and their evolution in the
coming of information age.

# VaR
- "Value at risk"
- Invented after stock market crash of 1987
- Usually quoted in units of $ for a given probability and time horizon
- 1% one-year VaR of $10 million means 1% chance that a portfolio will lose $10 million in a year

# Stress Tests
- Originally, term referred to a medical procedure to test for cardiovascular fitness
- OFHEO started testing firms' ability to withstand economic crisis before the 2008 crisis, failed.
- Dodd Frank Act 2010 requires the Federal Reserve to do annual stress tests for nonbank financial institutions it supervises for at least three different economic scenarios.
- European Banking Authority, created 2011
- UK, China, etc.
- Critics of stress tests such as Anat Admati find them inadequate.

# S&P 500
- Used as a benchmark for return

# Beta
- The CAPM implies that the expected return on the ith asset Millennials, also known as Generation Y (or simply Gen Y), are the demographic cohort following Generation X and preceding Generation Z. Researchers and popular media use the early 1980s as starting birth years and the mid-1990s to early 2000s as ending birth years, with 1981 to 1996 being a widely accepted defining range for the generation.is determined from its beta
- Beta ($\beta_i$) is the regression slope coefficient when the return on the ith asset is regressed on the return on the market.
$$\beta_i = \frac{Cov (r_i, r_{market})}{Var (r_{market})}$$
where $r$ stands for _return_

# Market Risk versus Idiosyncratic risk
- By construction, the residuals or oerror terms in a regression are uncorrelated with the fitter or predicted value
- So, the variance of the return of a stock is equal to its beta squared times the variance of tyhe market return (systematic risk) plus the variance of the residual in the regression (idiosyncratic risk)

# Distributions and outliers
- In finance, things tends to not follow the normal distribution
- Normal vs. Cauchy (Fat-tailed) distributions

## Central Limit Theorem
- Averages of a large number of independent identically distributed shocks (whose variance is finite) are approximatelly normally distributed
- Can fail if the underlying shocks are fat tailed
- Can fail if the underlying shocks lose their independence

# Insurance
## Fundamental Insurance Principles and Issues
- __Risk Pooling__ is the source of all value in insurance
- If _n_ policies, each has independent probability _p_ of a claim, then the number of claims follows the binomial distribution. The standard deviation of the fraction of policies that result in a claim is
$$\sqrt{(1-p)/n}$$
- _Law of large numbers_: as _n_ gets large, standard deviation approaches zero.
- _Moral Hazards_ dealt with partially by deductions and co-insurance.
- _Selection Bias_ dealt with by group policies, by testing and referrals, and by mandatory government insurance.
## Radical Financial Innovation - Example I: Insurance
- Burial societies ancient Rome, true insurance policies appeared in Italy in 14th century
- Rapid development of actuarial theory starting in 1600s with notion of probability
- Morris Robinson Mutual Life of NY 1840: highly-paid salesmen (agency theory)
- Henry Hyde Equitable Life Assurance Society 1880s: large cash value (psychological framing)
- Viviana Zelizer: challenging God, tempting fate (psychological framing)
- Inventions copied around the world
- Life insurance is a relic, of a day when people died young

# Portfolio Management: An Alternative to Insurance
- Investment core idea: is inherintly risky, if it were not risky woudn't give you any return
```
 Don't put all your eggs in one basket
```
- Diversification of ownership

## A Later Insight
- If people are all like me, all calculating with the same data, all wanting to hold portfolios on the frontier, then they all want to hold the same portfolio (and cash)
- so __THAT HAS TO BE THE MARKET PORTFOLIO__

## Portfolio Diversification
- All that should matter to an investor is the performance of the entire portfolio
- Mean and variance of portfolio matter
- Law of large numbers means that spreading over many independent assets reduces risk, has no effect on expected return

# Capital Asset Pricing Model (CAPM)
- CAPM asserts that all investors hold their optimial portfolio
- Consequence of the mutual fund theorem: all investors hold thhe same portfolio of risky assets, the tangency portfolio
- Therefore the CAPM says that the tangency portfolio equals the maket portfolio

## Beta
- The CAPM implies that the expected return on the ith asset is determined from its beta
- Beta ($β_i$) is the regression slope coefficient when the return on the ith asset is regressed on the
return on the market

## Investment Companies as Providers of Diversification
- Investment trust (before 1040s)
- Mutual funds (especially index funds)
- Closed end investment companies
- Unit investment trust
  - All these institutions can enable small investors to overcome transactions cost and lumpiness problems in achieving diversified portfolios

## Doubts about Diversification
- Complete diversification would imply holding much in fixed incomes, real state, etc. But hasn't stock market outperformed these?
- [Risk/Return Pyramid](https://www.investopedia.com/thmb/F1dQqU5OOp9p1KpkBsNgito7J6Y=/6250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/DeterminingRiskandtheRiskPyramid3-1cc4e411548c431aa97ac24bea046770.png)

# Short Sales
- How do you own a negative quantity of a stock? → you buy the share and sell them, now you own the shares of someone else (?)
- Brokers can enable you to hold a negative quantity of a tradable asset: they borrow the security and sell it, escrow the proceeds, you receive the proceeds, owe the security
- [Short sales in the United States were briefly abolished in September 2008 for a list of 799 stocks.](https://www.sec.gov/news/press/2008/2008-211.htm)
- Short selling, which is defined as the sale of a security that the seller has borrowed, is motivated by the belief that: The price of the security will decline. Buying back the security at a lower price will allow you to make a profit.

## In the Capital Asset Pricing Model (CAPM):
- A stock cannot have an optimial holding value which is negative. Otherwise, everyone would be shorting, which cannot happen in equilibrium since you need an investor to provide the stock to be shorted.
- The optimal portfolio in on the "efficient portfolio frontier"

# Gordon Growth Model
- Myron Gordon
- a formula that to calculate the present value of an asset that yields an infinite amount of value in the future
$$PV = \frac{x}{1 + r} + \frac{x(1 + g)}{(1 + r)^2} + \frac{x(1 + g)^2}{(1 + r)^3} + ... $$
$$PV = \frac{x}{r - g}$$

# Efficient Frontier
- An efficient portfolio is a combination of assets which achieves the highest return for a given risk.

## [Expected Return and Variance for a Two Asset Portfolio](https://financetrain.com/expected-return-and-variance-for-a-two-asset-portfolio/)
### Expected Return for a Two Asset Portfolio
The expected return of a portfolio is equal to the weighted average of the returns on individual assets in the portfolio.

$$R_p = w_1R_1 + w_2R_2$$
R_p = expected return for the portfolio
w_1 = proportion of the portfolio invested in asset 1
R_1 = expected return of asset 1

### Expected Variance for a Two Asset Portfolio
The variance of the portfolio is calculated as follows:

$$σ_p^2 = w_1^2σ_1^2 + w_2^2σ_2^2 + 2w_1w_2Cov_{1,2}$$

$Cov_{1,2}$ = covariance between assets 1 and 2
$Cov_{1,2} = ρ_{1,2} * σ_1 * σ_2$; where ρ = correlation between assets 1 and 2

The above equation can be rewritten as:
$$σ_p^2 = w_1^2σ_1^2 + w_2^2σ_2^2 + 2w_1w_2 ρ_{1,2}σ_1σ_2$$

# Limited Liability
- Limited Liability New York State 1811
- Divided up an enterprise into shares, and no shareholder is liable for more than he or she put in
- Other states were very  skeptical
- New York produced many failed corporations, a few spectacular successes
- Investors, in order to be encouraged to invest in businesses, should be protected against liability for what the managers of the business do.
- Investors in stocks cannot be pursued for the mistakes of the company they are investing in.

## Inflation Indexed Debt
Indexing the value of debt to an index:
- Is a better indexation method than indexing debt to a single commodity with a potentially unstable price evolution.
- Protects investors from currency instability. Currency instability can become a concern, especially if the government prints the currency.

# Real Estate Risk Management Devices
- Value of homes is a major source of risk
- Casualty insurance
- Securitized mortgages
- Home price futures and options 2006, housing.cme.com
- Equity-protected mortgages

# Limited Liability
In his work, David Moss describes how investors’ psychology favored limited liability after the early 19th century New York experiment. In fact, the comparison between investors’ psychologies in the context of  unlimited liability and lottery tickets is asymmetrical. Unlimited liability investors tend to overestimate the minimum probability of loss, whereas in lottery tickets, they overestimate the minimum probability of win.

# Inflation indexed debt
The introduction of inflation indexed debt was motivated by:
- An incentive to hedge from inflation volatility.
- Historical examples of nominal debt being wiped out in real terms by high inflation.
- An incentive to have a debt contract fixed in real terms.

# Unidad de Fomento
Chile introduce the Unidad de Fomento ro create a unit of account indexed to inflation, in order to counteract the impact of hyperinflation.

# Equity-protected mortgages
The concept of equity-protected mortgages consists in mortgages that include house price insurance. As an example, if the house price falls below the amount you owe, the mortgage debt will be corrected down.

# Forecasting - The Efficient Markets Hypothesis
An efficient market is defined as one in which asset prices quickly and fully reflect all available information.

## Random Walk & AR-I Models
- Random Walk:
$$x_t = x_{t-1} + ϵ_t$$
- First-order autoregressive (AR-I) Model:
$$x_t=100+ρ(x_{t-1}-100) + ϵ_t$$
Mean reverting (to 100), -1 < ρ < 1
- Random walk as approximate implication of unpredictability of returns
- Similarity of both random walk and AR-I to actual stock prices

## Intuition of Efficiency
- Reuter's pigeons and the telegraph
- Beepers & the internet
- Must be hard to get rich

## Price as PDV of Expected Dividends
The Dividend Discount Model (or Gordon Growth Model) can be stated as follows: let the investor’s discount rate be equal to r .If earnings equal dividends, and if dividends grow at the long-run rate g, then the price of the stock P can be written as follows: $P = E/(r-g)$
- Gordon Model: If earnings equal dividends and if dividends grow at long-run rate $g$, then by growing consol model
$$P=E/(r-g)$$
$$P/E = 1 / (r-g)$$
- So, efficient markets theory purports to explain why P/E varies across stocks
- Low P/E does not mean that the stock is a "bargain", it ontly means that earnings are rationally forecasted to decrease in future
- Efficient markets denies that any rule works
- The price-to-earnings ratio (P/E) tell you how much investors are willing to pay per unit of a company’s earnings.

## Reasons to Think Markets Ought to be Efficient
- Marginal investor determines prices
- Smart money dominates trading
- Survival of the fittest

# [Hedging](https://www.investopedia.com/terms/h/hedge.asp)
-  A hedge is an investment that is made with the intention of reducing the risk of adverse price movements in an asset. Normally, a hedge consists of taking an offsetting or opposite position in a related security.
- Hedging is a strategy that tries to limit risks in financial assets.
- Popular hedging techniques involve taking offsetting positions in derivatives that correspond to an existing position.
- Other types of hedges can be constructed via other means like diversification. An example could be investing in both cyclical and counter-cyclical stocks.
- Most common way of hedging in the market is through derivatives.

## Derivatives
- The underlying assets can be stocks, bonds, commodities, currencies, indices or interest rates.
- Derivatives can be effective hedges against their underlying assets, since the relationship between the two is more or less clearly defined.
- It’s possible to use derivatives to set up a trading strategy in which a loss for one investment is mitigated or offset by a gain in a comparable derivative.
- The effectiveness of a derivative hedge is expressed in terms of delta, sometimes called the "hedge ratio." Delta is the amount the price of a derivative moves per $1 movement in the price of the underlying asset.

# Elliott Wave Theory
- Ralph Nelson Elliott (1930)
- Elliott believed that stock markets, generally thought to behave in a somewhat random and chaotic manner, in fact, traded in repetitive patterns.
- Elliott proposed that financial price trends result from investors' predominant psychology.
- He found that swings in mass psychology always showed up in the same recurring fractal patterns, or "waves," in financial markets
- Elliott's theory somewhat resembles the Dow theory in that both recognize that stock prices move in waves. Because Elliott additionally recognized the "fractal" nature of markets, however, he was able to break down and analyze them in much greater detail.
## Impulse and Corrective Waves
- _impulse wave_: net travels in the same direction as the larger trend, always shows five waves in its pattern
- Five waves move in the direction of the main trend, followed by three waves in a correction (totaling a 5-3 move). This 5-3 move then becomes two subdivisions of the next higher wave move.
- The underlying 5-3 pattern remains constant, though the time span of each wave may vary.
- _corrective wave_: net travels in the opposite direction of the main trend.
- On a smaller scale, within each of the impulsive waves, five waves can again be found.
- This next pattern repeats itself _ad infinitum_
at ever-smaller scales.

## Wave Degrees
Elliott identified nine degrees of waves, which he labeled as follows, from largest to smallest:

- Grand Super Cycle
- Super Cycle
- Cycle
- Primary
- Intermediate
- Minor
- Minute
- Minuette
- Sub-Minuette

Since Elliott waves are a fractal, wave degrees theoretically expand ever-larger and ever-smaller beyond those listed above.

To use the theory in everyday trading, a trader might identify an upward-trending impulse wave, go long and then sell or short the position as the pattern completes five waves and a reversal is imminent.




Price action is divided into trends and corrections. Trends show the main direction of prices, while corrections move against the trend.
