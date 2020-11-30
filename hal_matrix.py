import numpy as np
from scipy.sparse import bsr_matrix

class Hal_Matrix:
    def __init__(self, n, d, data):
        """
        Create a HAL Matrix
        Parameters:
            n: shape of matrix (nxn)
            d: shape of blocks (dxd)
            data: data of block matrix, shape of data should be (n^2,d)
        """
        self.n=n
        self.d=d
        assert data.shape==(n**2,d), 'data is of incorrect shape, it shpuld be ({},{})'.format(n**2,d)
        self.data=data
        self.shape = (d*n, d*n)
    
    
    

data=np.array([[1,2,3,4]]).repeat(4,axis=0)
x = Hal_Matrix(n=2,d=4, data=data)
print(x.shape)

