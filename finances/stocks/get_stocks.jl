# Get stock prices using Julia
# http://dm13450.github.io/2020/07/05/AlphaVantage.html
using AlphaVantage
using DataFrames
using DataFramesMeta
using Dates
using Plots

#--- Settings
api_key = ""
AlphaVantage.global_key!(api_key)
AlphaVantage.GLOBAL[]

#--- Helper Functions
# convert between the raw data and Julia dataframes
function raw_to_dataframe(rawData)
    df = DataFrame(rawData[1])
    dfNames = Symbol.(vcat(rawData[2]...))
    df = rename(df, dfNames)

    df.Date = Date.(df.timestamp)
    for x in (:open, :high, :low, :close, :adjusted_close, :dividend_amount)
        df[!, x] = Float64.(df[!, x])
    end
    df.volume = Int64.(df.volume)
    return df
end

function intra_to_dataframe(rawData)
    df = DataFrame(rawData[1])
    dfNames = Symbol.(vcat(rawData[2]...))
    df = rename(df, dfNames)

    df.DateTime = DateTime.(df.timestamp, "yyyy-mm-dd HH:MM:SS")
    for x in (:open, :high, :low, :close)
        df[!, x] = Float64.(df[!, x])
    end
    df.volume = Int64.(df.volume)
    return df
end

#--- Stocks
# AlphaVantage provides daily, weekly and monthly historical stock data from 2000 right up to when you call the function. With the adjusted functions you also get dividends and adjusted closing prices to account for these dividends.
function getStock(stock_name)
    stockRaw = AlphaVantage.time_series_daily_adjusted(stock_name, outputsize="full", datatype="csv")
    stock = raw_to_dataframe(stockRaw);
    return stock
end

function plotStock(stock, stock_name)
    plot(stock.Date, stock.open, label = "Open", title = stock_name)
end


market = getStock("SP&500")
plotStock(market, "SP&500")

tesla = getStock("TSLA")
plotStock(tesla, "TSLA")
plot(market.open, tesla.open)
function plotStockVsMarket(stock1, stock2)
    plot(market.open, tesla.open)


#--- Intraday
# What separates AlphaVantage from say google or yahoo finance data is the intraday data. They provide high frequency bars at intervals from 1 minute to an hour. The only disadvantage is that the maximum amount of data appears to be 5 days for a stock. Still better than nothing!
tslaIntraRaw = AlphaVantage.time_series_intraday("TSLA", "1min", outputsize="full", datatype="csv");
tslaIntra = intra_to_dataframe(tslaIntraRaw)
tslaIntraDay = @where(tslaIntra, :DateTime .> DateTime(today()-Day(1)))
subPlot = plot(tslaIntraDay.DateTime, tslaIntraDay.open, label="Open", title="TSLA Intraday $(today()-Day(1))")
allPlot = plot(tslaIntra.DateTime, tslaIntra.open, label="Open", title = "TSLA Intraday")
plot(allPlot, subPlot, layout=(1,2))

#--- Techinical Indicators
# Relative Strength Index
rsiRaw = AlphaVantage.RSI("TSLA", "1min", 10, "open", datatype ="csv")
rsiDF = DataFrame(rsiRaw[1])
rsiDF = rename(rsiDF, Symbol.(vcat(rsiRaw[2]...)))
rsiDF.time = DateTime.(rsiDF.time, "yyyy-mm-dd HH:MM:SS")
rsiDF.RSI = Float64.(rsiDF.RSI)

rsiSub = @where(rsiDF, :time .> DateTime(today() - Day(1)))
plot(rsiSub[!,:time], rsiSub[!, :RSI], title = "TSLA")
hline!([30,70], label = ["Oversold","Overbought"])


# Sector Performance
# AlphaVantage also provides the sector performance on a number of timescales through one API call.
sectorRaw = AlphaVantage.sector_performance()
sectorRaw["Rank F: Year-to-Date (YTD) Performance"]

# Forex
eurgbpRaw = AlphaVantage.fx_weekly("EUR", "GBP", datatype="csv");
eurgbp = DataFrame(eurgbpRaw[1])
eurgbp = rename(eurgbp, Symbol.(vcat(eurgbpRaw[2]...)))
eurgbp.Date = Date.(eurgbp.timestamp)
eurgbp.open = Float64.(eurgbp.open)
eurgbp.high = Float64.(eurgbp.high)
eurgbp.low = Float64.(eurgbp.low)
eurgbp.close = Float64.(eurgbp.close)
plot(eurgbp.Date, eurgbp.open, label="open", title="EURGBP")

# NDF's
usdkrwRaw = AlphaVantage.fx_monthly("USD", "KRW", datatype="csv");
usdkrw = DataFrame(usdkrwRaw[1])
usdkrw = rename(usdkrw, Symbol.(vcat(usdkrwRaw[2]...)))
usdkrw.Date = Date.(usdkrw.timestamp)
usdkrw.open = Float64.(usdkrw.open)
usdkrw.high = Float64.(usdkrw.high)
usdkrw.low = Float64.(usdkrw.low)
usdkrw.close = Float64.(usdkrw.close)
plot(usdkrw.Date, usdkrw.open, label="open", title="USDKRW")

# FX Intraday
# intraday data is available for the FX pairs.
usdcadRaw = AlphaVantage.fx_intraday("USD", "CAD", datatype="csv");
usdcad = DataFrame(usdcadRaw[1])
usdcad = rename(usdcad, Symbol.(vcat(usdcadRaw[2]...)))
usdcad.timestamp = DateTime.(usdcad.timestamp, "yyyy-mm-dd HH:MM:SS")
usdcad.open = Float64.(usdcad.open)
plot(usdcad.timestamp, usdcad.open, label="Open", title="USDCAD")

# Crypto
# The API follows the same style as traditional currencies and again has more digital currencies than you can shake a stick at. Again daily, weekly and monthly data is available plus a ‘health-index’ monitor that reports how healthy a cryptocurrency is based on different features.
ethRaw = AlphaVantage.digital_currency_daily("ETH", "USD", datatype="csv")
ethHealth = AlphaVantage.crypto_rating("ETH");
titleString = ethHealth[""]

eth = DataFrame(ethRaw[1])
eth = rename(eth, Symbol.(vcat(ethRaw[2]...)), makeunique=true)
eth.Date = Date.(eth.timestamp)
eth.Open = Float64.(eth[!, Symbol("open (USD)")])

plot(eth.Date, eth.Open, label="Open", title = "Ethereum")
