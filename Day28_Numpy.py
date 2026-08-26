'''
Data Analysis:
-------------
-->Data Analysis is the process of collecting,cleaning,transforming,
organizing,and analyzing data to convert into useful information and
also used for make decision to get the better outcome.

Library Used
------------
1.Numpy
2.Pandas
3.matplotlib
4.seaborn


1.Numpy
-------
-->this refers to Numerical Python.
-->It is an python library used for calculation and operations
-->This python library is more faster than the list to perform
operations.
-->And also supports multi-dimensions array.

Functions
---------
-->The function is used to find out the dimensions of an array.
syntax:array.ndim
eg:
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.ndim)

eg:
eg:
'''
import numpy as np
arr_2=np.array([1,2,3,4,5])
print(arr_2.ndim)
arr_3=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(arr_3.ndim)
'''
Shape
-----
-->The shape functions is used to find the row &col of an array.
syntax:array.shape
eg:
--
'''
import numpy as np
arr_2=np.array([1,2,3,4,5])
print(arr_2.shape)
arr_3=np.array([
    [1,2,3],
    [4,5,6],
    ])
print(arr_3.shape)
'''
reshape
-------
-->The function is used to convert one dimension to another if the
elements are there convert into the any dimension.
syntax:array.reshape(row,col)
eg:
'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))
arr_3=np.array([1,2,3,4,5,6,7,8,9])
print(arr_3.reshape(3,3))
'''
size:
----
-->The size functions is used find out number of elements present in an array.
syntax:array.size
eg:
'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.size)
'''
arange
------
-->The range func is used to generate number in a sequence upto a limit and it form 1D array.
-->And this array can convert into 2D arrays by using reshape
syntax:np.arange(range)
eg:
'''
import numpy as np
arr_2=np.arange(1,10)
print(arr_2.reshape(3,3))
print(arr_2)
'''
eg:'''
import numpy as np
arr_2=np.arange(1,10)
arr_=arr_2.reshape(3,3)
print(arr_)
print(arr_.ndim)
print(arr_2)
'''
Operations
----------
--Same as list we can also perform some operations on arrays like
1.indexing
eg:
'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2[5])
'''
2.slicing
eg:
'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2[2:5])
'''
3.sum
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.sum())
'''
4.add
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr_3=np.array([7,8,9,10,11,12])
print(arr_2+arr_3)

'''
5.sub
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr_3=np.array([7,8,9,10,11,12])
print(arr_2-arr_3)
print(arr_3-1)
'''
6.mul
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr_3=np.array([7,8,9,10,11,12])
print(arr_2*arr_3)
print(arr_2*2)
'''
7.power'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr_3=np.array([7,8,9,10,11,12])
print(arr_2**3)

'''
8.Div'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2/2)
'''
9.max
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.max())
'''
10.min
eg:'''
import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.min())












