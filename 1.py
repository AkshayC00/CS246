import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# print("Generated Values are:")
# print(seq)

# Given values of n
n = [1000, 10000, 100000]

# Defining the figure and sizes of axes
fig, ax = plt.subplots(2,3, figsize=(30,10))

c = ['c', 'g', 'r']
k=0
# For every value of n, creating a histogram and plotting the values of (U(i-1), Ui)
for i in n:
    ax[0][k].hist(seq[:i], range=(0,1), bins=30, edgecolor='black', color=c[k])
    ax[0][k].set_xlabel('Range')
    ax[0][k].set_ylabel('Frequency')
    ax[0][k].set_title(f'N={i}')
    ax[1][k].plot(seq[:i],seq[1:i+1], f'{c[k]}o')
    ax[1][k].set_xlabel(r"$U_{i-1}$")
    ax[1][k].set_ylabel(r"$U_i$")
    k+=1
plt.show()
