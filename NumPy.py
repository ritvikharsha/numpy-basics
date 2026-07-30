import numpy as np
import time
import sys

a = np.arange(6).reshape(3,2)
print(a)


'''
a1 = np.array([1,2,3,4,5,6])
a2 = np.array([[1,2],[3,4],[5,6]])
print(a1.ndim)
print(a2.ndim)
print(a1.itemsize)
print(a1.dtype)

a3 = np.array([[1,2],[3,4],[5,6]] , dtype=np.float64)
print(a3.dtype)
a4 = np.array([[1,2],[3,4],[5,6]] , dtype=complex)
print(a4)

a5 = np.zeros((3,3))
print(a5)
print(a5.dtype)
a5 = np.ones((3,3))
print(f"{a5} \n")

a6 = np.arange(5)
print(a6)

a7 = np.linspace(1,5,10)
print(a7)
'''



"""    # execution time of python list and numpy array
SIZE = 1000000

l = range(SIZE)
print(sys.getsizeof(1)*len(l))

array = np.arange(SIZE)
print(array.size*array.itemsize)

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [x+y for x,y in zip(l1,l2)]
print("python list took: ",(time.time()-start)*1000)

# numpy array
start = time.time()
result = a1+a2
print("numpy took: ",(time.time()-start)*1000)
"""