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



#example 2: A*sin(pi/4 *t + theta)
#the goal is to generate 100 numbers theta between (-pi, pi), pi is a float around 3.14
#also generate 100 numbers A follow iid with mean 0, variance = 4 (segma = 2)
#set t with indexs from 0 to 99. since the computer count from 0. 

#creat an empty pandas data frame
df = pd.DataFrame()

#random.uniform (low, upper, number)
df['Theta']=rand.uniform(-math.pi, math.pi, 100)

#random.normal(mean,segma, number)
df['A']=rand.normal(0,2, 100)

#creat an index for df using time t [0,99]
df.index=[x for x in range(100)]

#math.degrees(f) is to covert number to a degree
y=list(map(lambda A,T,Theta: A*math.sin(45*T+math.degrees(Theta)),df['A'],df.index,df['Theta']))

df['y']=y


print(df['y'].mean())
print(df['y'].var())

print(np.cov(df.A,df.y))
print(np.cov(df.Theta,df.y))
print(df.corr())

df.y.plot()
plot.show()

