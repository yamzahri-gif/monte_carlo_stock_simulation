import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as pd_yf

# Import Apple's data
apple = pd_yf.download('AAPL', period = '2y')



# Remove the ticker level from column names
apple.columns = apple.columns.get_level_values(0)
print(apple.head())

# yields calculation (use log easier with percentages)
apple_yields = np.log(apple['Close']/apple['Close'].shift(1))
apple_clean = apple_yields.dropna()
print(apple_clean)

# calculation of daily mean yields 
apple_yields = apple_clean.mean()

# Calculation of the volatility
apple_vix = apple_clean.std()

print("Average yields : " ,apple_yields)
print("Volatility : " , apple_vix)

# Initial price S0 (252 days ago)
S0 = apple['Close'].iloc[-252]

# Random simlulation paramters
# Number of simulations 
N = 10000
print("Number of simulation :" , N)
# Number of days simulated
T = 252 
print("Days simulated :" , T)

# Random 
# symetry around the mean
loc = 0
# Neutral standard variation (volatilty) 
scale = 1
# Matrix size (T days , N simulation)
size = (T,N)

###randomization
Z = np.random.normal(loc , scale , size)
print("Matrix of all our random simulation is : ")
print(Z)
# Geometric Brownian Motion calculation 
# Combining historical statistics with random draws
# Drift : average yields adjusted with Itô's lemma
# Ito correction : effect of the volatility on S0

daily_returns = (((apple_yields - apple_vix**2)/2)
                + (apple_vix*Z))
print("Daily returns:", daily_returns)

# conversion in dollars 

real_price = np.exp(np.cumsum(daily_returns , axis = 0))*S0
print("real prices are :")
print(real_price)


# creating a plot of our 10,000 simulated price
plt.plot(real_price)
plt.title("Monte carlo simulation showing 10000 prediction")
plt.xlabel("Number of days")
plt.ylabel("Apple stock price")
plt.show()



# Extracting the final price
final_price = real_price[-1,:]
print("final price : " , final_price)

# Precision
final_price_mean = final_price.mean()
print("Mean : " , final_price_mean)

final_price_median = np.median(final_price)
print("Median : " , final_price_median)

final_price_percentile_5 = np.percentile(final_price , 5)
print("Worst scenario :" , final_price_percentile_5)

final_price_percentile_95 = np.percentile(final_price , 95)
print("Best scenario: " , final_price_percentile_95)

# Date correponding to S0
day_S0 = print(" Date :", apple.index[-252])

# Final precision 
plt.hist(final_price)
plt.title("Final price distribution")
plt.xlabel("Price $ ")
plt.ylabel("Draws")
plt.show()