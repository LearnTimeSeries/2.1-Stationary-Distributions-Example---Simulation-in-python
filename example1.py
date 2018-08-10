# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:40:34 2018

@author: Chunhui Zhu
"""

#NumPy is the fundamental package for scientific computing 
import numpy as np
# we are going to do some calculation with sin(), degree and pi
import math
#import numpy.random to simulate random seeds 
import numpy.random as rand 
#convert list to Data Frame
import pandas as pd


#example 1 : 2*x
# the goal is to generate 100 numbers Xn as you roll the dice 100 times indepedently
# {Zn}={2* Xn}, this is your sequence distribution y at the following 


#creat an empty pandas data frame
df = pd.DataFrame()

x,y=[],[]

for i in range(100):
    seed=rand.randint(1,6)
    x.append(seed)
    y.append(seed*2)

#storage numpy array into df with column name
df['x']=x
df['y']=y


print(df.y.mean())
print(df.y.var())
print(np.cov(df.x, df.y)) # only exist when the sequence is continous
print(df.corr()) 


df.plot()
plot.show()

