# Rolling Standard Deviation of Returns
Standard deviation is a statistical measurement that looks at how far discrete points in a dataset are dispersed from the mean of that set
- it's calculated as $\sqrt{Variance}$

If data points are far from the mean, there is a higher deviation within the data set

The Rolling Standard Deviation of Returns measures how much an investment's returns fluctuate over a defined, moving time window
- it tracks how return volatility changes over time, highlighting periods of high instability (e.g. market crashes) and low stability (e.g. steady growth) without being locked into a single fixed historical period

## Understanding Standard Deviation
### For Price Volatility
When applied to annual rate of return of an investment, it can provide information on that investment's historical volatility
- this means that this shows how much the price of that investment has fluctuated over time

The greater the standard deviation of securities, the greater the variance between each price and the mean, which shows a larger price range

For example:
- a volatile stock has a high standard deviation, meaning that its price goes up and down frequently
- the standard deviation of a stable blue-chip stock, on the other hand, is usually rather low, meaning that its price is usually stable

### For Price Trends
Standard deviation can also be used to predict performance trends
- in investing for example, an index fund is designed to replicate a benchmark index
- this means that the fund should have a low standard deviation from the value of the benchmark

On the other hand, aggressive growth funds often have a high standard deviation from relative stock indices
- this is because their portfolio managers make aggressive bets to generate higher-than-average returns
- this higher standard deviation correlates with the level of risk investors can expect from that index

## Rolling Standard Deviation of Returns Formula
$$
\begin{align}
 & \sigma = \sqrt{\frac{\sum(R_{i}-\mu)^2}{N-1}} \\ \\
 & where: \\
 & \sigma = \text{rolling standard deviation (volatility)} \\
 & R_{i} = \text{return in a single period} \\
 & \mu = \text{mean (average) return over the window} \\
 & N = \text{number of periods in the rolling window}
\end{align}
$$

## Standard Deviation Formula
$$
\begin{align}
 & \text{Standard Deviation} = \sqrt{\frac{\sum ^n_{i=1}(x_{i}-\overline x)^2}{n-1}} \\ \\
 & where: \\
 & x_{i} = \text{value of the } i^{th} \text{ point in the data set} \\
 & \overline x = \text{the mean value of the data set} \\
 & n = \text{the number of data points in then set}
\end{align}
$$
### Calculating Standard Deviation
Standard deviation is calculated as follows:
1. Calculate the mean of all data points: add the data point values and divide by the number of data points
2. Calculate the variance for each data point: subtract the mean from the value of the data point
3. Square the variance of each data point
4. Sum the squared variance values
5. Divide the sum of squared variance values by the number of data points in the data set less 1
6. Take the square root of the quotient

## How Standard Deviation is Used
### Risk Management
Standard deviation is widely used in business for risk management
- it helps businesses quantify and manage various types of risks

By calculating the standard deviation of certain outcomes, businesses can assess the volatility or uncertainty associated with how they operate

### Financial Analysis
In finance and accounting, standard deviation is used to analyse financial data and assess the variability of financial performance metrics

For example, standard deviation is employed to measure the volatility of investment returns
- this can be used to determine risk-return tradeoffs and the strategy of how a company wants to deploy capital

## Example: Apple Share Price Volatility
Consider shares of Apple (AAPL) over 5 particular years

Historical returns for Apple's stock were:
- 34.65% for 2021
- -26.40% for 2022
- 49.01% for 2023
- 30.70% for 2024
- 9.05% for 2025
The average return over the 5 years was thus 19.40%

The value of each year's return minus the mean were then:
- 15.25% for 202
- -45.80% for 2022
- 29.61% for 2023
- 11.30% for 2024
- -10.35% for 2025

All those values are then squared to yield:
- 0.0233, 0.2098, 0.0877, 0.0128, and 0.0107
- the sum of these values is: 0.3442
- dividing that value by 4 (N - 1) gives the variance: $0.3442 \div 4=0.0860$

The square root of the variance is taken to obtain the standard deviation of:
- 0.2933, or 29.33%

## What does a High Standard Deviation Mean?
> A large standard deviation indicates that there is a big spread in the observed data.

> A small or low standard deviation would indicate instead that much of the data observed is clustered tightly around the mean.

## Is Lower Standard Deviation Better in Investing?
A lower standard deviation isn't necessarily better
- it indicates less risk, which investors may or may not prefer
- when assessing the amount of deviation in their portfolios, investors should consider their tolerance for volatilty and their overall investment objectives

More aggressive investors may be comfortable with an investment strategy that opts for vehicles with higher-than-average volatility, while more conservative investors may not
