import numpy as np
from hal import Hal_Matrix
import time

def dot_product(x,y):
    t1 = time.time()
    z1 = x.dot(y)
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def add_product(x,y):
    t1 = time.time()
    z1 = x + y
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def subtract_product(x,y):
    t1 = time.time()
    z1 = x - y
    t2 = time.time()
    hal_time = t2-t1
    return hal_time

def multiply_product(x,y):
    t1 = time.time()
    z1 = x.multiply(y)
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

def compare_add_product(x,y):
    hal_time = add_product(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x + y 
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_subtract_product(x,y):
    hal_time = subtract_product(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x - y 
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)

def compare_multiply_product(x,y):
    hal_time = multiply_product(x,y)
    x, y = x.to_numpy(), y.to_numpy()
    t1 = time.time()
    z2 = x * y
    t2 = time.time()
    numpy_time = t2-t1
    return (hal_time, numpy_time)