# On-Balance Volume
OBV is a pivotal technical trading indicator that leverages volume flow to anticipate stock price movements
- market volume is the driving force behind significant price shifts

The OBV metric aims to forecast when major market moves will occur based on changes in volume
- when volume rises sharply without a corresponding price change, an eventual significant price movement is likely (either upward or downward) due to this "spring being wound tightly" effect

## Understanding the OBV Formula
$$
OBV = OBV_{prev} +
\begin{cases}
volume, \text{if close > }close_{prev} \\
0, \text{if close = }close_{prev} \\
-volume, \text{if close < }close_{prev}
\end{cases}
$$
- where:
	- $OBV = \text{Current on-balance volume level}$
	- $OBV_{prev} = \text{Previous on-balance volume level}$
	- $volume = \text{Latest trading volume amount}$

## How to Calculate OBV Effectively
OBV provides a running total of an asset's trading volume and indicates whether this volume is flowing in or out of a given security or currency pair

> The OBV is a cumulative total of volume (+ve and -ve).

There are 3 rules implemented when calculating the OBV:

1. If today's closing price is higher than yesterday's closing price, then:
	- Current OBV = Previous OBV + Today's volume

2. If today's closing price is lower than yesterday's closing price, then:
	- Current OBV = Previous OBV - Today's volume

3. If today's closing price equals yesterday's closing price, then:
	- Currennt OBV = Previous OBV

## Insights Provided by OBV
The theory behind OBV is based on the distinction between smart money (namely, institutional investors) and less sophisticated retail investors
- as mutual funds and pension funds begin to buy into an issue that retail investors are selling, volume may increase even as the price remains relatively level

Eventually, volume drives the price upward
- at that point, larger investors begin to sell, and smaller investors begin buying

## Example: Using OBV in Trading
Example:
1. Day one: closing price equals $10, volume equals 25,200 shares
2. Day two: closing price equals $10.15, volume equals 30,000 shares
3. Day three: closing price equals $10.17, volume equals 25,600 shares
4. Day four: closing price equals $10.13, volume equals 32,000 shares
5. Day five: closing price equals $10.11, volume equals 23,000 shares
6. Day six: closing price equals $10.15, volume equals 40,000 shares
7. Day seven: closing price equals $10.20, volume equals 36,000 shares
8. Day eight: closing price equals $10.20, volume equals 20,500 shares
9. Day nine: closing price equals $10.22, volume equals 23,000 shares
10. Day 10: closing price equals $10.21, volume equals 27,500 shares

As can be seen, days 2, 3, 6, 7, 9 are up days, so these trading volumes are added to the OBV

Days 4, 5, and 10 are down days, so these trading volumes are subtracted from the OBV

On day 8, no changes are made to the OBV since the closing price didn't change

Given the days, the OBV for each of the 10 days is:
1. Day one OBV = 0
2. Day two OBV = 0 + 30,000 = 30,000
3. Day three OBV = 30,000 + 25,600 = 55,600
4. Day four OBV = 55,600 - 32,000 = 23,600
5. Day five OBV = 23,600 - 23,000 = 600
6. Day six OBV = 600 + 40,000 = 40,600
7. Day seven OBV = 40,600 + 36,000 = 76,600
8. Day eight OBV = 76,600
9. Day nine OBV = 76,600 + 23,000 = 99,600
10. Day 10 OBV = 99,600 - 27,500 = 72,100
