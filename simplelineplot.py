# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:04:42 2019

@author: manpreet.saluja
"""

import numpy as np
from matplotlib import pyplot as plt

x=np.arange(0,10)
y=x^2

#Labeling the graph
plt.title("Graph Displaying")
plt.xlabel("Time")
plt.ylabel("Distance")

#Simple plot
plt.plot(x,y)