import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')

# Random Numbers generated between (0,1)

a = 17
m = 1000
b = 51
x = np.random.randint(1, m+1)

seq = []
seq.append((x%m)/m)
for i in range(17):
    x = (a*x+b)%m
    seq.append(x/m)


# set values of N
N = 100001

# create the rest of the sequences
for i in range(18,N):
    u = seq[-18]-seq[-6]
    if u < 0:
        u += 1
    seq.append(u)

# Define the range of X
X = np.arange(1, 10000, 2)

# Define CDF for the discrete distribution
P = np.arange(len(X))/(len(X)-1)

# Initilise the array of frequencies
count = len(X)*[0]

# Update frequencies using the generated X
for x in np.multiply(seq,(len(X)-1)):
    count[int(x)] += 1

# Creating a Table of frequencies
df = pd.DataFrame({'X': X, 'Frequency':count})
print(df)
df.to_csv('Discrete X Frequency.csv', index=False)