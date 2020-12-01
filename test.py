import numpy as np
from hal_matrix import Hal_Matrix

data=np.array([[1,1,1,1]]).repeat(4,axis=0)
x = Hal_Matrix(n=2,d=4, data=data)
data=np.array([[1,1,1,1]]).repeat(1,axis=0)
y = Hal_Matrix(n=1,d=4, data=data)
print(y.matrix.todense())
x.add(y)
print(x.matrix.todense())
