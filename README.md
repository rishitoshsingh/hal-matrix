# HAL-Matrix

Consider a matrix A of size *<strong>R<sup>(nd x nd)</sup></strong>*, where each non-overlapping *<strong>(d x d)</strong>* block of the matrix, *<strong>D<sub>ij</sub></strong>*, is a diagonal matrix. So the matrix consists of *<strong>n<sup>2</sup></strong>* such blocks. An example of such a matrix is shown below:

![matrix](http://www.sciweavers.org/tex2img.php?eq=%0A%20%20%20%5Cbegin%7Bbmatrix%7D%20D_%7B11%7D%20%26%20D_%7B12%7D%20%26%20D_%7B13%7D%20%26%20%5Ccdots%20%26%20D_%7B1n%7D%20%5C%5C%20D_%7B21%7D%20%26%20D_%7B22%7D%20%26%20D_%7B23%7D%20%26%20%5Ccdots%20%26%20D_%7B2n%7D%20%5C%5C%20%5Ccdots%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%20%5Ccdots%20%5C%5C%20D_%7Bn1%7D%20%26%20D_%7Bn2%7D%20%26%20D_%7Bn3%7D%20%26%20%5Ccdots%20%26%20D_%7Bnn%7D%20%5Cend%7Bbmatrix%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0 "matrix")

## Comparision with NumPy arrays
![dot](graphs/dot.png "dot")
![add](graphs/add.png "add")
![sub](graphs/sub.png "sub")
![mul](graphs/mul.png "mul")