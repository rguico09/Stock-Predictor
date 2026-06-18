# ATR
The Average True Range (ATR) is a technical analysis indicator that measures market volatility by decomposing the entire range of an asset price for that period

The true range indicator is taken as the greatest of the following:
- the current high less the current low
- the absolute value of the current high less the previous close
- the absolute value of the current low less the previous close

The ATR is then a MA of the true ranges, generally using 14 days
- traders can use shorter periods than 14 days to generate more trading signlas
- longer periods have a higher probability of generating fewer trading signals

## The ATR Formula
$$
\begin{align}
 & \frac{\text{Previous ATR(n-1) + TR}}{n} \\ \\
 & where: \\
 & n = \text{number of periods} \\
 & TR = \text{true range}
\end{align}
$$

If there isn't a previous ATR calculated, we must use:
$$
\begin{align}
 & \left( \frac{1}{n} \right)\sum^n_{i}TR_{i} \\ \\
 & where: \\
 & TR_{i} = \text{particular true range, such as first day's TR, then second, then third} \\
 & n = \text{number of periods}
\end{align}
$$

We must first use this formula to calculate the true range:
$$
\begin{align}
 & TR = Max \ [ \ (H-L), \ |H-C_{p}|, \ |L-C_{p}| \ ] \\ \\
 & where: \\
 & H = \text{today's high} \\
 & L = \text{today's low} \\
 & C_{p} = \text{yesterday's closing price} \\
 & Max = \text{highest value of the three terms} \\ \\
 & so \ that: \\
 & (H-L) = \text{today's high minus the low} \\
 & |H-C_{p}| = \text{aboslute value of today's high minus yesterday's closing price} \\
 & |L-C_{p}| = \text{absolute value of today's low minus yesterday's closing price}
\end{align}
$$

## How to Calculate the ATR
Suppose that XYZ's stock had a trading high today of $21.95 and a low of $20.22
- it closed yesterday at $21.51

Using the three terms, we use the highest result:
- $(H-L) = 21.95 - 20.22 = \$1.73$
- $|(H-C_{p}| = |21.95 - 21.51| = \$0.44$
- $|L-C_{p}| = |20.22 - 21.51| = \$1.29$
The number we'd use would be $\$1.73$ because it has the highest value

Because we don't have a previous ATR, we must use the ATR formula:
$$
\left( \frac{1}{n} \right)\sum^n_{i}TR_{i}
$$
- using 14 days as the number of periods, we'd calculate the TR for each of the 14 days

|        | High    | Low     | Yesterday's Close |
| ------ | ------- | ------- | ----------------- |
| Day 1  | $ 21.95 | $ 20.22 | $ 21.51           |
| Day 2  | $ 22.25 | $ 21.10 | $ 21.61           |
| Day 3  | $ 21.50 | $ 20.34 | $ 20.83           |
| Day 4  | $ 23.25 | $ 22.13 | $ 22.65           |
| Day 5  | $ 23.03 | $ 21.87 | $ 22.41           |
| Day 6  | $ 23.34 | $ 22.18 | $ 22.67           |
| Day 7  | $ 23.66 | $ 22.57 | $ 23.05           |
| Day 8  | $ 23.97 | $ 22.80 | $ 23.31           |
| Day 9  | $ 24.29 | $ 23.15 | $ 23.68           |
| Day 10 | $ 24.60 | $ 23.45 | $ 23.97           |
| Day 11 | $ 24.92 | $ 23.76 | $ 24.31           |
| Day 12 | $ 25.23 | $ 24.09 | $ 24.60           |
| Day 13 | $ 25.55 | $ 24.39 | $ 24.89           |
| Day 14 | $ 25.86 | $ 24.69 | $ 25.20           |
We'd use these prices to calculate the TR for each day

|        | $H-L$  | $H-C_{p}$ | $L-{C_{p}}$ |
| ------ | ------ | --------- | ----------- |
| Day 1  | $ 1.73 | $ 0.44    | $ (1.29)    |
| Day 2  | $ 1.15 | $ 0.64    | $ (0.51)    |
| Day 3  | $ 1.16 | $ 0.67    | $ (0.49)    |
| Day 4  | $ 1.12 | $ 0.60    | $ (0.52)    |
| Day 5  | $ 1.15 | $ 0.61    | $ (0.54)    |
| Day 6  | $ 1.16 | $ 0.67    | $ (0.49)    |
| Day 7  | $ 1.09 | $ 0.61    | $ (0.48)    |
| Day 8  | $ 1.17 | $ 0.66    | $ (0.51)    |
| Day 9  | $ 1.14 | $ 0.61    | $ (0.53)    |
| Day 10 | $ 1.15 | $ 0.63    | $ (0.52)    |
| Day 11 | $ 1.16 | $ 0.61    | $ (0.55)    |
| Day 12 | $ 1.14 | $ 0.63    | $ (0.51)    |
| Day 13 | $ 1.16 | $ 0.66    | $ (0.50)    |
| Day 14 | $ 1.17 | $ 0.66    | $ (0.51)    |
We'd find that the highest values for each day are from the $(H-L)$ column, so we'd add up all the results from the $(H-L)$ column and multiply the result by $\frac{1}{n}$
$$
\begin{align}
 & \$1.73+\$1.15+\$1.16+\$1.12+\$1.15+ \\
 & \$1.16+\$1.09+\$1.17+\$1.14+\$1.15+ \\
 & \$1.16+\$1.14+\$1.16+\$1.17 \\
 & =\$16.65 \\ \\ \\
 & \frac{1}{n}(\$16.65) = \frac{1}{14}(\$16.65) = \$1.18
\end{align}​
$$
- the average volatility for this asset is therefore $\$1.18$

Now that we have the ATR for the previous period, we can use it to determine the ATR for the current period using:
$$
\frac{\text{Previous ATR(n-1) + TR}}{n}
$$
This formula is much simpler because we only have to calculate the TR for one day
- assuming on day 15, the asset has a high of $\$25.55$, a low of $\$24.37$, and closed the previous day at $\$24.87$, its TR works out to $\$1.18$
$$
\begin{align}
 & \frac{\$1.18(14-1)+\$1.18}{14} \\ \\
 & \frac{\$1.18(13)+\$1.18}{14} \\ \\
 & \frac{\$15.34+\$1.18}{14} \\ \\
 & \frac{\$16.52}{14} = \$1.18
\end{align}
$$
- the stock closed the day again with an average volatility (ATR) of $\$1.18$

## What does the ATR Tell Us?
A stock experiencing a high level of volatility has a higher ATR
- and a lower ATR indicates lower volatility for the period evaluated

The ATR may be used by market technicians to enter and exit trades
- it was created to allow traders to more accurately measure the daily volatility of an asset by using simple calculations

The indicator doesn't indicate the price direction
- it's primarily used to measure volatility caused by gaps and limit up or down moves

> The ATR is commonly used as an exit method that can be applied regardless of how the entry decision is made.

One popular technique is known as the "chandelier exit"
- it places a trailing stop under the highest high the stock has reached since you entered the trade
- the distance between the highest high and the stop level is defined as some multiple multiplied by the ATR

The ATR can also give a trader an indication of what size trade to use in the derivatives markets

## Example of How to Use the ATR
Assume the first value of a 5-day ATR is calculated at 1.41, and the 6th day has a TR of 1.09
- the sequential ATR value could be estimated by multiplying the previous value of the ATR by the number of days less 1 and then adding the TR for the current period to the product

Next, divide the sum by the selected timeframe
- the 2nd value of the ATR is estimated to be 1.35, or $\frac{1.41*(5-1) + (1.09))}{5}$
- the formula could then be repeated over the entire period

The ATR doesn't tell us in which direction the breakout will occur
- but it can be added to the closing price
- and the trader can buy whenever the next day's price trades above that value

Trading signals occur relatively infrequently, but they usually indicate significant breakout points
- the logic behind these signals is that whenever a price closes more than an ATR above the most recent close, a change in volatility has occurred
