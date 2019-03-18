# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:38:33 2019

@author: manpreet.saluja
"""

import matplotlib.pyplot as plt
import numpy as np
 
# create data
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = np.random.rand(40) 
# use the scatter function
plt.scatter(x, y, s=z*1000,c=colors)
plt.show()
 