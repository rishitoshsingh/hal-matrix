import numpy as np
from error import *
from scipy.sparse import dia_matrix, bmat
import copy

class Hal_Matrix:
    def __init__(self, n, d, data):
        """
        Create a HAL Matrix
        Attributes:
            n -- shape of matrix (nxn)
            d -- shape of blocks (dxd)
            data -- data of block matrix, shape of data should be (n^2,d)
        """
        self.n=n
        self.d=d
        assert data.shape==(n**2,d), 'data is of incorrect shape, it shpuld be ({},{})'.format(n**2,d)
        self.data=data

        # creating blocks array
        self.blocks = []
        for dia_data in data:
            self.blocks.append(dia_matrix((dia_data,[0]),shape=(d,d)))
        self.blocks = np.array(self.blocks).reshape(n,n)
        # creating matrix from blocks
        self.matrix=bmat(self.blocks)
        self.shape = self.matrix.shape

    def add(self, y):
        if not isinstance(y, Hal_Matrix):
            raise TypeMismatchError(self, y)
        if self.n != y.n and min(self.n, y.n) != 1:
            raise BroadcastError(self.n, y.n)
        if self.d != y.d and min(self.d, y.d) != 1:
            raise BroadcastError(self.d, y.d)
        
        # setting new dimensions 
        n = max(self.n,y.n)
        d = max(self.d,y.d)

        # adding data 
        data = self.data + y.data
        # updatinig blocks
        self.blocks = []
        return Hal_Matrix(n=n,d=d,data=data)

    def multiply(self, y):
        """
        Perform element wise multiplication
        """
        if not isinstance(y, Hal_Matrix):
            raise TypeMismatchError(self, y)
        if self.n != y.n:
            raise ShapeMismatchError(self.n,y.n)
        if self.d != y.d:
            raise BlockShapeMismatchError(self.d,y.d)

        data = self.data * y.data
        return Hal_Matrix(n=self.n,d=self.d,data=data)
        
    def dot(self, y):
        """
        Find dot product of self and other matrix
        """
        if not isinstance(y, Hal_Matrix):
            raise TypeMismatchError(self, y)
        if self.n != y.n:
            raise ShapeMismatchError(self.n,y.n)
        if self.d != y.d:
            raise BlockShapeMismatchError(self.d,y.d)
        
        new_dia_datas = []
        for i in range(self.n):
            left = self.data[i*self.n : (i+1)*self.n ]
            for j in range(self.n):
                right = y.data[j :  : self.n ]
                new_dia_datas.append((left * right).sum(axis=0))
        new_dia_datas = np.array(new_dia_datas)
        return Hal_Matrix(n=self.n,d=self.d,data=new_dia_datas)

    def to_numpy(self):
        return self.matrix.todense()

    def __add__(self,y):
        return self.add(y)
    
    def __sub__(self,y):
        new_y = copy.deepcopy(y)
        new_y.data = new_y.data * -1
        return self.add(new_y)

    def __str__(self):
        return 'Hal_Matrix of dimension (n) {} and block dimension (d) {} with data = \n{}'.format(self.n,self.d,self.data)
