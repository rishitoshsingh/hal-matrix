class TypeMismatchError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        t1 -- Type of first object
        t2 -- Type of second object
    """

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        self.message = 'Invalid type of matrix {}, it should be {}'.format(type(t1),type(t2))
        super().__init__(self.message)
        
class ShapeMismatchError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        n1 -- Dimension of first matrix
        n2 -- Dimension of second matrix
    """

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.message = 'Shape mismatch {} != {}, cannot find dot product'.format(n1,n2)
        super().__init__(self.message)

class BlockShapeMismatchError(Exception):
    """Exception raised for errors in the Block Shape.

    Attributes:
        d1 -- Dimension of first matrix
        d2 -- Dimension of second matrix
    """

    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.message = 'Blocks shape mismatch {} != {}, cannot find dot dot product'.format(d1,d2)
        super().__init__(self.message)

class BroadcastError(Exception):
    """Exception raised for errors in the Broadcasting.
    """

    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
        self.message = 'Cannot broadcast {} and {}'.format(shape1,shape2)
        super().__init__(self.message)