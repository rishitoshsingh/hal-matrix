import numpy as np
from hal import Hal_Matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from test import *

dot_hal_time, dot_numpy_time = [], []
add_hal_time, add_numpy_time = [], []
sub_hal_time, sub_numpy_time = [], []
mul_hal_time, mul_numpy_time = [], []
n_s, d_s = [], []
for n in [25, 50, 75]:
    for d in [25, 50, 75]:
        if(n == 0 or d == 0 ):
            continue
        n_s.append(n)
        d_s.append(d)
        print('Sample: ({}, {})'.format(n,d))
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        x = Hal_Matrix(n=n,d=d, data=data)
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        y = Hal_Matrix(n=n,d=d, data=data)
        hal, numpy = compare_dot_product(x,y)
        dot_hal_time.append(hal)
        dot_numpy_time.append(numpy)
        hal, numpy = compare_add_product(x,y)
        add_hal_time.append(hal)
        add_numpy_time.append(numpy)
        hal, numpy = compare_subtract_product(x,y)
        sub_hal_time.append(hal)
        sub_numpy_time.append(numpy)
        hal, numpy = compare_multiply_product(x,y)
        mul_hal_time.append(hal)
        mul_numpy_time.append(numpy)
    
df = pd.DataFrame()
df['n'] = n_s
df['n'] = df['n'].astype('str')
df['d'] = d_s
df['d'] = df['d'].astype('str')
df['dot_hal_time'] = dot_hal_time
df['dot_numpy_time'] = dot_numpy_time
df['add_hal_time'] = add_hal_time 
df['add_numpy_time'] = add_numpy_time
df['sub_hal_time'] = sub_hal_time 
df['sub_numpy_time'] = sub_numpy_time 
df['mul_hal_time'] = mul_hal_time 
df['mul_numpy_time'] = mul_numpy_time

dot_hal_time = []
add_hal_time = []
sub_hal_time = []
mul_hal_time = []
n_s, d_s = [], []
for n in range(0,401,100):
    for d in range(0,401,100):
        if(n == 0 or d == 0 ):
            continue
        n_s.append(n)
        d_s.append(d)
        print('Sample: ({}, {})'.format(n,d))
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        x = Hal_Matrix(n=n,d=d, data=data)
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        y = Hal_Matrix(n=n,d=d, data=data)
        hal = dot_product(x,y)
        dot_hal_time.append(hal)
        hal = add_product(x,y)
        add_hal_time.append(hal)
        hal = subtract_product(x,y)
        sub_hal_time.append(hal)
        hal = multiply_product(x,y)
        mul_hal_time.append(hal)    

df2 = pd.DataFrame()
df2['n'] = n_s
df2['n'] = df2['n'].astype('str')
df2['d'] = d_s
df2['d'] = df2['d'].astype('str')
df2['dot_hal_time'] = dot_hal_time
df2['add_hal_time'] = add_hal_time
df2['sub_hal_time'] = sub_hal_time
df2['mul_hal_time'] = mul_hal_time

dot_hal_time = []
add_hal_time = []
sub_hal_time = []
mul_hal_time = []
n_s, d_s = [], []
for n in range(0,401,100):
    for d in range(0,51,50):
        if(n == 0 or d == 0 ):
            continue
        n_s.append(n)
        d_s.append(d)
        print('Sample: ({}, {})'.format(n,d))
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        x = Hal_Matrix(n=n,d=d, data=data)
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        y = Hal_Matrix(n=n,d=d, data=data)
        hal = dot_product(x,y)
        dot_hal_time.append(hal)
        hal = add_product(x,y)
        add_hal_time.append(hal)
        hal = subtract_product(x,y)
        sub_hal_time.append(hal)
        hal = multiply_product(x,y)
        mul_hal_time.append(hal)    

df3 = pd.DataFrame()
df3['n'] = n_s
df3['n'] = df3['n'].astype('str')
df3['d'] = d_s
df3['d'] = df3['d'].astype('str')
df3['dot_hal_time'] = dot_hal_time
df3['add_hal_time'] = add_hal_time
df3['sub_hal_time'] = sub_hal_time
df3['mul_hal_time'] = mul_hal_time

dot_hal_time = []
add_hal_time = []
sub_hal_time = []
mul_hal_time = []
n_s, d_s = [], []
for d in range(0,401,100):
    for n in range(0,51,50):
        if(n == 0 or d == 0 ):
            continue
        n_s.append(n)
        d_s.append(d)
        print('Sample: ({}, {})'.format(n,d))
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        x = Hal_Matrix(n=n,d=d, data=data)
        data=np.array([[10]*d]).repeat(n**2,axis=0)
        y = Hal_Matrix(n=n,d=d, data=data)
        hal = dot_product(x,y)
        dot_hal_time.append(hal)
        hal = add_product(x,y)
        add_hal_time.append(hal)
        hal = subtract_product(x,y)
        sub_hal_time.append(hal)
        hal = multiply_product(x,y)
        mul_hal_time.append(hal)    

df4 = pd.DataFrame()
df4['n'] = n_s
df4['n'] = df4['n'].astype('str')
df4['d'] = d_s
df4['d'] = df4['d'].astype('str')
df4['dot_hal_time'] = dot_hal_time
df4['add_hal_time'] = add_hal_time
df4['sub_hal_time'] = sub_hal_time
df4['mul_hal_time'] = mul_hal_time

pd.concat([df,df2,df3,df4]).sort_values(by=['n','d']).to_csv('comparision.csv')