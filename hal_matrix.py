import numpy as np
from scipy.sparse import dia_matrix, bmat

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

        dia_matrices = []
        for dia_data in data:
            dia_matrices.append(dia_matrix((dia_data,[0]),shape=(d,d)))
        dia_matrices = np.array(dia_matrices).reshape(n,n)
        self.matrix=bmat(dia_matrices)
        self.shape = self.matrix.shape

    
data=np.array([[1,2,3,4]]).repeat(4,axis=0)
x = Hal_Matrix(n=2,d=4, data=data)
print(x.shape)

