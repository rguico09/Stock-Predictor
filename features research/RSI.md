# RSI
The RSI is a momentum indicator used in technical analysis
- RSI measures the speed and magnitude of a security's recent price changes to detect overbought or oversold conditions in the price of that security
- the RSI is displayed as an oscillator (a line graph) on a scale of 0 to 100

> Traditionally, an RSI reading of 70 or above indicates an overbought condition.
> A reading of 30 or below indicates an oversold condition.

In addition to identifying overbought and oversold securities, the RSI can also indicate securities that may be primed for a trend reversal or a corrective pullback in price

## How the RSI Works
As a momentum indicator, the RSI compares a security's stength on days when prices go up to its strength on days when prices drop
- comparing this result to price movement can help traders predict how a security might perform in the future

## Calculating RSI
$$
RSI_{\text{step one}} = 100 - \left[ \frac{100}{1+\frac{\text{Average gain}}{Average loss}} \right]
$$

The average gain or loss used in this calculation is the average percentage gain or loss during a look-back period
- the formula uses a +ve value for the average loss
	- periods with price losses are counted as 0 in the calculations of average gain
	- periods with price increases are counted as 0 in the calculations of average loss

The standard number of periods used to calculate the initial RSI value is 14
- for example, imagine the market closed higher 7 out of the past 14 days with an initial average gain of 1%
- the remaining 7 days all closed lower with an initial average loss of -0.8%

The first calculation for the RSI would look like:
$$
55.55 = 100 - \left[ \frac{100}{1+\frac{\frac{1\%}{14}}{\frac{0.8\%}{14}}} \right]
$$

Once there are 14 periods of data available, the second calculation can be done
- the purpose is to smooth the results so that the RSI only nears 100 or 0 in a strongly trending market
$$
RSI_{\text{step two}} = 100 - \left[ \frac{100}{1+\frac{\text{(Previous Average Gain} \times 13)+\text{Current Gain}}{(\text{Previous Average Loss} \times 13)+\text{Current Loss}}} \right]
$$

## Why RSI is Important
- traders can use RSI to predict the price behaviour of a security
- it can help traders validate trends and trend reversals
- it can point to overbought and oversold securities
- it can provide short-term traders with buy and sell signals

## Using RSI With Trends
### Modify RSI Levels to Fit Trends
The primary trend of the security is important to know to understand RSI readings properly
- for example, an oversold reading by the RSI in an uptrend is probably much higher than 30
- an overbought reading during a downtrend is also much lower than 70

During a downtredn, the RSI peaks near 50 rather than 70
- this could be seen by tradersas more reliably signaling bearish conditions

## What is a Bullish RSI Number?
A number of RSI levels can be considered bullish, depending on whether the market is trending up or down or is rangebound

One bullish signal is when the RSI crosses below 30, where it would be considered oversold

> Bullish RSI signals are best used in uptrends.

In a strong downtrend, prices can keep falling even after indicators are oversold
- so trades based on that signal may have limited upside and go against the main trend

Following a strong uptrend, another bullish RSI signal is a reversal after a decline to around 40 to 50 (an area considered support during an uptrend)
- this often confirms a +ve momentum shift back toward the uptrend after a pullback, signaling potential for continued gains

## What is a Bearish RSI Number?
Bearish signals from the RSI appear much like bullish ones but in reverse

A basic bearish signal is when the RSI crosses above 70, an overbought level
- if this is followed by a move below 70, upward momentum may weaken, alerting traders to a potential price reversal?

> Bearish RSI signals are best used in downtrends.

During a strong downtrend, a bearish RSI signal is a reversal after a rise to around 50 to 60
- this often confirms a momentum shift back towards the downside after a pullback, signaling potential for continued declines

## Interpretation of RSI and RSI Ranges
> During trends, the RSI readings may fall into a band or range.
- during a strong uptrend, the RSI tends to stay well above 30 and should frequently hit 70
- during a strong downtrend, it's rare to see the RSI exceed 70, while it frequently hits 30 or below

If the RSI can't reach 70 on a number of consecutive price swings during an uptrend, but drops below 30, the trend is likely breaking down

The opposite is true for a downtrend
- if the downtrend is unable to reach 30 or below and then rallies above 70, that downtrend has broken down and could be reversing to the upside

## Example of RSI Swing Rejections
A bullish swing rejection has 4 parts:
1. the RSI falls into oversold territory
2. the RSI crosses back above 30
3. the RSI forms another dip without crossing back into oversold territory
4. the RSI then breaks its most recent high

A bearish swing rejection also has 4 parts:
1. the RSI rises into overbought territory
2. the RSI crosses back below 70
3. the RSI forms another high without reaching overbought territory
4. the RSI then breaks its most recent low

## What is a Good RSI Number to Use?
The default is a 14-period time frame, which provides a balanced response to price changes and is well-suited to swing and position trading

Using shorter periods between 5 and 9 minutes makes the RSI more sensitive, appealing to day traders who want to capture quick momentum shifts, though they tend to generate more noise

Using longer periods, such as 21 to 30, suits long-term investors looking to capture major trends
