# Moving Averages
## Common MA Periods
For identifying significant, long-term support and resistance levels and overall price trends:
- 50-day, 100-day, and 200-day MAs are the most common

The 200-day MA is considered especially significant in stock trading
- when the 50-day MA of a stock price remains above the 200-day MA, the stock is generally thought to be in a bullish trend
- a crossover to the downside of the 200-day MA is interpreted as bearish

The 5-, 10-, 20-, and 50-day MAs are often used to spot near-term trend changes
- changes in direction by these shorter-term MAs are watched as possible early clues to longer-term trend changes
- crossovers of the 50-day MA with either the 10-day or 20-day MA are regarded as significant

 > The 10-day MA plotted on an hourly chart is frequently used to guide traders in intraday trading
 
 > Some traders use Fibonacci numbers (5, 8, 13, 21, ...) to select MAs
 
## Types of MAs
There are numerous variations of MAs
- they can be based on closing price, opening price, high price, low price, or a calculation combining these various price levels

Most MAs are some form of:
- the SMA (average price over a given period)
- the EMA (weighted to favour more recent price action)

> Time is of the essence when trading. An EMA and a double EMA (DEMA) both reflect the current price trend for given securities in a more up-to-date reading

Short-term traders typically rely on the 12- or 26-day EMA
- while the 50-day and 200-day EMA is used by long-term investors

> While the EMA line reacts more quickly to price swings than the SMA, it can still lag quite a bit over longer periods

DEMA helps to solve the lagging issue, bringing a MA line closer to the current fluctuations in price
- this metric is calculated not just by doubling the EMA but by using the following complex formula:
$$
DEMA = 2*EMA - EMA(EMA)
$$
- where the current EMA is a function of the EMA factor

Essentially, this means even more weight is applied to the recent data, bringing the DEMA line into closer correlation with the current price
- traders see DEMA crossovers before EMA and SMA crossovers, allowing for quicker reaction times with trades

# SMA
A SMA is a tool used in financial analysis to determine the average price of an asset over a set number of periods, typically calculated using closing prices

By smoothing out price fluctuations, the SMA aids investors in identifying potential trends and making informed decisions

## How SMAs work
A SMA is an arithmetic MA calculated by adding recent prices and then dividing that figure by the number of time periods in the calculation range
- for example: add the closing prices over several periods and divide the sum by the number of periods

Short-term averages react quickly to price changes, whereas long-term averages respond more slowly

The formula for SMA is:
$$
\begin{align}
&SMA = \frac{A_{1} + A_{2}+ \dots + A_{n}}{n} \\ \\
wh&ere: \\
A_{n} &= \text{the price of an asset at period n} \\
n &= \text{the number of total periods}
\end{align}
$$

For example, this is how we would calculate the simple moving average of a security with the following closing prices over a 15-day period:
$$
\begin{align}
&\text{Week One (5 days)}: 20, 22, 24, 25, 23 \\
&\text{Week Two (5 days)}: 26, 28, 26, 29, 27 \\
&\text{Week Three (5 days)}: 28, 30, 27, 29, 28 \\ \\
&20+22+24+25+23+26+28+26+29+27+28+30+27+29+28=392 \\
&392/15 = 26.13
\end{align}
$$
- the 15-day SMA for this security is $26.13
- a 10-day MA considers only the last 10 closing prices
- each day, the newest closing price replaces the oldest, updating the average

# EMA
The EMA is a refined MA that emphasises recent data points more heavily, offering a crucial edge in tracking price dynamics
- unlike the SMA, which distributes weight equally across data points, the EMA's technique gives it a distinct advantage in responding swiftly to price fluctuations

## Formula for EMA
$$
\begin{align}
EMA_{Today} = &\left( Value_{Today} * \left( \frac{Smoothing}{1 + Days} \right) \right) \\
&+ EMA_{Yesterday} * \left( 1 - \left( \frac{Smoothing}{1 + Days} \right) \right) \\ \\
where: \\
EMA =& \text{Exponential Moving Average}
\end{align}
$$
While there are many possible choices for the smoothing factor, the most common choice is:
-  `smoothing = 2`

That gives the most recent observation more weight
- if the smoothing factor is increased, more recent observations have more influence on the EMA

## How to Calculate the EMA
Calculating the EMA needs one more observation than the SMA
- if we choose 20 days for our EMA, we wait until the 20th day to get the SMA
- then, use that SMA as the first EMA on the 21st day

Next, we must calculate the multiplier for smoothing (weighting) the EMA
- which typically follows the formula: $[2 \div (\text{number of observations + 1})]$
- for a 20-day MA, the multiplier would be: $[2 \div (20+1)] = 0.0952$

We then use this formula to calculate the current EMA:
$$
EMA = \text{Closing price x multiplier + EMA(previous day) x (1-multiplier)}
$$

EMAs give more weight to recent prices, while SMAs give equal weight to all values
- shorter-period EMAs give more weight to recent prices than longer-period EMAs
- for example, an 18.18% multiplier is applied to the most recent price data for a 10-period EMA, while the weight is only 9.52% for a 20-period EMA

 > Variations of the EMA can be calculated using the open, high, low, or median price instead of the closing price.

## Insights From the EMA
The 12- and 26-day EMAs are often the most quoted short-term averages
- they're used to create indicators like the MACD and the PPO

EMAs are much better suited for trending markets
- when the market is in a strong and sustained uptrend, the EMA indicator line will also show an uptrend and vice-versa for a downtrend

A vigilant trader will pay attention to both the direction of the EMA line and the relation of the ROC from one bar to the next
- suppose the price action of a strong uptrend begins to flatten and reverse
	- from an opportunity cost POV, it might be time to switch to a more bullish investment
