import numpy as np
from hal_matrix import Hal_Matrix
import time

def compare_dot_product():
    data=np.array([[10]*100]).repeat(100,axis=0)
    x = Hal_Matrix(n=10,d=100, data=data)
    data=np.array([[10]*100]).repeat(100,axis=0)
    y = Hal_Matrix(n=10,d=100, data=data)
    t1 = time.time()
    z1 = x.dot(y)
    t2 = time.time()
    print(' HAL_matrix time : {}'.format(t2-t1)) # 0.01703357696533203
    x = x.to_numpy()
    y = y.to_numpy()
    t1 = time.time()
    z2 = x.dot(y)
    t2 = time.time()
    print('NumPy time: {}'.format(t2-t1)) # 2.231570243835449




