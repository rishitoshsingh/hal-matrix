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
        if data.shape != (n**2,d):
            raise DataShapeMismatchError((n**2,d))
        # assert data.shape==(n**2,d), 'data is of incorrect shape, it shpuld be ({},{})'.format(n**2,d)
        self.data=data
        self.shape = (self.n * self.d, self.n * self.d) 

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
        return Hal_Matrix(n=n,d=d,data=data)
    
    def inverse(self):
        eye_matrix = self.eye(self.n, self.d)
        given_matrix = copy.deepcopy(self)
        self.data = self.data.astype('float')
        eye_matrix.data = eye_matrix.data.astype('float')

        def divide(matrix, i, j, num):
            cur_row = i // matrix.n
            cur_col = i % matrix.n
            matrix.data[cur_row*matrix.n : (cur_row+1)*matrix.n, j] = matrix.data[cur_row*matrix.n : (cur_row+1)*matrix.n, j] / num

        def subtract(matrix, eye_matrix, i, j):
            cur_row = i // matrix.n
            cur_col = i % matrix.n
            for row_i in range(1,matrix.n):
                row = (row_i + cur_row) % matrix.n
                sub_mul = matrix.data[row*matrix.n + cur_col, j]
                matrix.data[row*matrix.n : (row+1)*matrix.n, j] = matrix.data[row*matrix.n : (row+1)*matrix.n, j]  - sub_mul * matrix.data[cur_row*matrix.n : (cur_row+1)*matrix.n, j]
                eye_matrix.data[row*eye_matrix.n : (row+1)*eye_matrix.n, j] = eye_matrix.data[row*eye_matrix.n : (row+1)*eye_matrix.n, j]  - sub_mul * eye_matrix.data[cur_row*eye_matrix.n : (cur_row+1)*eye_matrix.n, j]

        def add_if_zero(matrix, i, j, nonzero_i):
            cur_row = i // matrix.n
            nonzero_row = nonzero_i // matrix.n
            nonzero_col = nonzero_i % matrix.n
            matrix.data[cur_row*matrix.n : (cur_row+1)*matrix.n, j] = matrix.data[cur_row*matrix.n : (cur_row+1)*matrix.n, j] + matrix.data[nonzero_row*matrix.n : (nonzero_row+1)*matrix.n, j]

        for i in range(0, given_matrix.n**2, given_matrix.n+1):
            for j in range(given_matrix.d):
                if given_matrix.data[i,j] == 0:
                    if np.any(given_matrix.data[i+given_matrix.n : : given_matrix.n, j] != 0):
                        nonzero_i = np.nonzero(given_matrix.data[i+given_matrix.n : : given_matrix.n, j])[0][0] + (i+given_matrix.n)
                        add_if_zero(given_matrix, i, j, nonzero_i)
                        add_if_zero(eye_matrix, i, j, nonzero_i)
                        divide_num = given_matrix.data[i,j]
                        divide(given_matrix, i, j, divide_num)
                        divide(eye_matrix, i, j, divide_num)
                    else:
                        raise InreversibleError()
                    
                elif given_matrix.data[i,j] != 1:
                    divide_num = given_matrix.data[i,j]
                    divide(given_matrix, i, j, divide_num)
                    divide(eye_matrix, i, j, divide_num)
                
                subtract(given_matrix, eye_matrix, i, j)

        return eye_matrix

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
        blocks = []
        for dia_data in self.data:
            blocks.append(dia_matrix((dia_data,[0]),shape=(self.d,self.d)))
        blocks = np.array(blocks).reshape(self.n,self.n)
        # creating matrix from blocks
        matrix=bmat(blocks)
        return matrix.toarray()
    
    @staticmethod
    def eye(n, d):
        data = [0]*n**2
        data[0::n+1] = [1]*n
        data = np.array(data).reshape(-1,1).repeat(d,axis=1)
        return Hal_Matrix(n=n,d=d,data=data)    
    
    @staticmethod
    def zeros(n, d):
        data = [0]*n**2
        data = np.array(data).reshape(-1,1).repeat(d,axis=1)
        return Hal_Matrix(n=n,d=d,data=data)    

    @staticmethod
    def ones(n, d):
        data = [1]*n**2
        data = np.array(data).reshape(-1,1).repeat(d,axis=1)
        return Hal_Matrix(n=n,d=d,data=data)    

    def __add__(self,y):
        return self.add(y)
    
    def __sub__(self,y):
        new_y = copy.deepcopy(y)
        new_y.data = new_y.data * -1
        return self.add(new_y)
    
    def __mul__(self,y):
        return self.multiply(y)

    def __str__(self):
        return 'Hal_Matrix of dimension (n) {} and block dimension (d) {} with data = \n{}'.format(self.n,self.d,self.data)
