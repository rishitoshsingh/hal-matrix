import numpy as np
from hal import Hal_Matrix
import time

def dot_product(x,y):
    t1 = time.time()
    z1 = x.dot(y)
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def add(x,y):
    t1 = time.time()
    z1 = x + y
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def subtract(x,y):
    t1 = time.time()
    z1 = x - y
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def multiply(x,y):
    t1 = time.time()
    z1 = x.multiply(y)
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def inverse(x):
    t1 = time.time()
    z1 = x.inverse()
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def compare_dot_product(x,y):
    hal_time = dot_product(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x.dot(y)
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_add(x,y):
    hal_time = add(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x + y 
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_subtract(x,y):
    hal_time = subtract(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x - y 
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_multiply(x,y):
    hal_time = multiply(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x * y
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_inverse(x):
    hal_time = inverse(x)
    x = x.to_numpy()
    t1 = time.time()
    z2 = np.linalg.inv(x) 
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

data = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8],
                 [9,10],
                 [11,12],
                 [13,14],
                 [15,16],
                 [17,18]])
# data = np.array([[1.,2.],
#                  [3.,4.],
#                  [5.,6.],
#                  [7.,8.]])
# x = Hal_Matrix(n=3,d=2, data=data)
# print(x.inverse())  
# print(x.to_numpy())