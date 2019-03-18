# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:31:30 2019

@author: manpreet.saluja
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
dataset.plot.box(grid='True')