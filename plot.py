#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import math

# make up a list of points to be plotted
data = open("npiRatioIncome.txt", "r")
x = []
y = []
f = plt.figure()

line = data.readline()
while line:
    cur = line.split("|")
    # Convert the elements to float and take the logarithm if positive
    x_value = float(cur[1])
    y_value = float(cur[2])

    if x_value > 0 and y_value > 0:
        x.append(math.log(x_value))
        y.append(math.log(y_value))
    line = data.readline()


data.close()

plt.scatter(x,y,c = 'royalblue', alpha= 0.05)
# no ticks
#plt.tick_params(left = False, bottom=False, labelbottom = False, labelleft = False)

# specify the x and y axis labels
plt.xlabel("# Diabetic Rx Prescribed / # Diabetic Services")
plt.ylabel("Avg Income in Prescriber's zip")

f.savefig("plot.pdf")
