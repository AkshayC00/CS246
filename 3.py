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
    seq.append(float(u))
  

# Generate values of X1, X2, . . . , XN from the above distribution for N = 10, 100, 1000, 10000, 100000
seq1 = np.sin(np.multiply(np.pi/2,seq))**2
x = [seq1[:10], seq1[:100], seq1[:1000], seq1[:10000], seq1[:100000]]

n = [10, 100, 1000, 10000, 100000]

fig = plt.figure(figsize=(30,10))

# Iterating through values of n
for i in range(5):
    # Sorting the values of Generated X
    X = np.sort(x[i])
    # Specifying the values of P(X<=x)
    y = np.arange(len(x[i]))/(len(x[i])-1)
    ax = plt.subplot(2, 3, i+1)
    # Plotting the values
    plt.plot(X, y, label=f'CDF for N={n[i]}')
    plt.xlabel('X')
    plt.ylabel('F(X)')
    plt.legend()

# Printing the Mean and Variance for all the distributions
means = [np.mean(x[i]) for i in range(5)]
variance = [np.var(x[i]) for i in range(5)]

for i in range(5):
    print(f'For N = {n[i]}: ')
    print(f'Mean = {means[i]}')
    print(f'Variance = {variance[i]}\n')

# Creating array of points for generating the CDF of X
x1 = np.arange(0,50,0.01)
y = np.multiply(2/np.pi, np.arcsin(np.sqrt(x1))) 
ax = plt.subplot(2, 3, 6)
# Plotting the graph
plt.plot(x1, y, 'r', label='Actual CDF of X')
plt.xlabel('X')
plt.ylabel('F(X)')
plt.legend()
plt.show()
