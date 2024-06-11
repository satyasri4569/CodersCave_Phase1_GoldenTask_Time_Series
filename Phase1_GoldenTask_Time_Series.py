
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "stock_data.csv"
stock_data = pd.read_csv('/content/portfolio_data.csv')

# Check the first few rows of the dataset
print(stock_data.head())


     
       Date        AMZN        DPZ         BTC       NFLX
0  5/1/2013  248.229996  51.190983  106.250000  30.415714
1  5/2/2013  252.550003  51.987320   98.099998  30.641428
2  5/3/2013  258.049988  52.446388  112.900002  30.492857
3  5/6/2013  255.720001  53.205257  109.599998  30.098572
4  5/7/2013  257.730011  54.151505  113.199997  29.464285

# Calculate statistics
mean_price = stock_data['AMZN'].mean()
std_dev_price = stock_data['AMZN'].std()
min_price = stock_data['AMZN'].min()
max_price = stock_data['AMZN'].max()

# Print statistics
print("Statistical Information about AMZN Stock Prices:")
print(f"Mean Price: {mean_price}")
print(f"Standard Deviation: {std_dev_price}")
print(f"Minimum Price: {min_price}")
print(f"Maximum Price: {max_price}")

     
Statistical Information about AMZN Stock Prices:
Mean Price: 821.5418097875
Standard Deviation: 518.4426534119237
Minimum Price: 248.229996
Maximum Price: 2039.51001


     

# Calculate autocorrelation
autocorr = stock_data['AMZN'].autocorr()

print(f"Autocorrelation of AMZN Stock Prices: {autocorr}")

     
Autocorrelation of AMZN Stock Prices: 0.9993459817702117

# Calculate statistics for BTC (Bitcoin)
mean_btc = stock_data['BTC'].mean()
std_dev_btc = stock_data['BTC'].std()
min_btc = stock_data['BTC'].min()
max_btc = stock_data['BTC'].max()

# Print statistics for BTC
print("Statistical Information about BTC (Bitcoin) Prices:")
print(f"Mean Price: {mean_btc}")
print(f"Standard Deviation: {std_dev_btc}")
print(f"Minimum Price: {min_btc}")
print(f"Maximum Price: {max_btc}")

     
Statistical Information about BTC (Bitcoin) Prices:
Mean Price: 2421.4656685598684
Standard Deviation: 3310.894199096725
Minimum Price: 69.660004
Maximum Price: 18972.32031

# Calculate statistics for DPZ (Domino's Pizza)
mean_dpz = stock_data['DPZ'].mean()
std_dev_dpz = stock_data['DPZ'].std()
min_dpz = stock_data['DPZ'].min()
max_dpz = stock_data['DPZ'].max()

# Print statistics for DPZ
print("Statistical Information about DPZ (Domino's Pizza) Prices:")
print(f"Mean Price: {mean_dpz}")
print(f"Standard Deviation: {std_dev_dpz}")
print(f"Minimum Price: {min_dpz}")
print(f"Maximum Price: {max_dpz}")

     
Statistical Information about DPZ (Domino's Pizza) Prices:
Mean Price: 146.7716948388158
Standard Deviation: 72.19228694375192
Minimum Price: 51.190983
Maximum Price: 298.635986

# Calculate statistics for NFLX (Netflix)
mean_nflx = stock_data['NFLX'].mean()
std_dev_nflx = stock_data['NFLX'].std()
min_nflx = stock_data['NFLX'].min()
max_nflx = stock_data['NFLX'].max()

# Print statistics for NFLX
print("Statistical Information about NFLX (Netflix) Prices:")
print(f"Mean Price: {mean_nflx}")
print(f"Standard Deviation: {std_dev_nflx}")
print(f"Minimum Price: {min_nflx}")
print(f"Maximum Price: {max_nflx}")

     
Statistical Information about NFLX (Netflix) Prices:
Mean Price: 147.6682725796053
Standard Deviation: 107.64148632525642
Minimum Price: 29.464285
Maximum Price: 418.970001

from statsmodels.tsa.seasonal import seasonal_decompose

# Perform decomposition
decomposition = seasonal_decompose(stock_data['AMZN'], model='additive', period=50)

# Plot decomposition components
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(stock_data.index, decomposition.observed, label='Observed')
plt.legend()
plt.subplot(4, 1, 2)
plt.plot(stock_data.index, decomposition.trend, label='Trend')
plt.legend()
plt.subplot(4, 1, 3)
plt.plot(stock_data.index, decomposition.seasonal, label='Seasonal')
plt.legend()
plt.subplot(4, 1, 4)
plt.plot(stock_data.index, decomposition.resid, label='Residual')
plt.legend()
plt.tight_layout()
plt.show()

     


import matplotlib.pyplot as plt

# Calculate mean prices for each stock
mean_prices = {
    'AMZN': stock_data['AMZN'].mean(),
    'DPZ': stock_data['DPZ'].mean(),
    'BTC': stock_data['BTC'].mean(),
    'NFLX': stock_data['NFLX'].mean()
}

# Plot bar graph
plt.figure(figsize=(10, 6))
plt.bar(mean_prices.keys(), mean_prices.values(), color='skyblue')
plt.title('Mean Prices of Different Stocks')
plt.xlabel('Stock')
plt.ylabel('Mean Price')
plt.show()

     


import numpy as np

# Calculate statistics for each column
stats = {
    'Mean': [stock_data['AMZN'].mean(), stock_data['DPZ'].mean(), stock_data['BTC'].mean(), stock_data['NFLX'].mean()],
    'Median': [stock_data['AMZN'].median(), stock_data['DPZ'].median(), stock_data['BTC'].median(), stock_data['NFLX'].median()],
    'Std Deviation': [stock_data['AMZN'].std(), stock_data['DPZ'].std(), stock_data['BTC'].std(), stock_data['NFLX'].std()]
}

# Create a colorful bar graph
labels = ['AMZN', 'DPZ', 'BTC', 'NFLX']
bar_width = 0.2
x = np.arange(len(labels))

plt.figure(figsize=(10, 6))
for i, (label, values) in enumerate(stats.items()):
    plt.bar(x + i * bar_width, values, bar_width, label=label)

plt.xlabel('Stock')
plt.ylabel('Values')
plt.title('Statistical Information for Different Stocks')
plt.xticks(x + bar_width, labels)
plt.legend()
plt.show()

     


# Calculate mean prices for each stock
mean_prices = {
    'AMZN': stock_data['AMZN'].mean(),
    'DPZ': stock_data['DPZ'].mean(),
    'BTC': stock_data['BTC'].mean(),
    'NFLX': stock_data['NFLX'].mean()
}

# Create a pie chart
labels = mean_prices.keys()
sizes = mean_prices.values()
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribution of Mean Prices Among Different Stocks')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

     
