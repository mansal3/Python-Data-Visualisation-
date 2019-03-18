# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:13:07 2019

@author: manpreet.saluja
"""

import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 
# Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)
plt.plot(z,t)

#Adding Annotate
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry') 

#addling legends
plt.legend(["Race1","Race2"],loc=4)

#adding style to graoh
plt.style.use('fast')