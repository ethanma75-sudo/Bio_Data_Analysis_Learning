# Day 1: What is Numpy?

# TODO:
#  np.array()、np.zeros()、np.ones()、np.arange()
#  shape
#  indexing and slicing
#  Set up a 2-dimensional array and fetch data.

import numpy as np

protein = np.array([12.5, 18.2, 9.7])

print(protein)
print(type(protein))

# The full name of ndarray is "N-dimensional array". Then what is the dimension of protein?

print(protein.ndim)

# You may think that the dimension simply means the number of groups in the array. But it's not! To find out,
# predict the output of this code:

a = np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(a.ndim)

# Are you surprised? Actually the word dimension means the number of coordinates so that we could locate one
# element. In this example, you need 2. So the dimension is 2.
# By the way, "element" simply means the number of number in the array. In this case, a has 6 elements.

# Another function is called "shape". This is not asking how large the data is, rather it is asking how the
# data look like.

print(protein.shape)

# Maybe this is a bit hard to find out the pattern. Let's "upgrade" the protein to a 2-d array.

protein = np.array([
    [12.5, 18.2, 9.7],
    [11.3, 16.8, 10.2]
])

print(protein.shape)

# For a 2-D array, its shape is (row, column).

# Now let's move on to slicing and indexing. We have obtained some data from our experiment.

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

#         column
#        0   1   2   3
#      ┌───┬───┬───┬───┐
# row 0│10 │20 │30 │40 │
#      ├───┼───┼───┼───┤
# row 1│50 │60 │70 │80 │
#      └───┴───┴───┴───┘

# To find the data "70", we need row-1 and column-2. Then what is the output? (remember: like list,
# array starts from 0).

print(data[1,2])

# What if I only provide one parameter? Guess the output:

print(data[0])

# Yes! If you only provide the index of the row and leave the column blank, Numpy will give the whole row.

# Now what if we want the whole column?

print(data[:, 2])

# By adding one colon, you are telling Numpy that I want the whole dimension. And yes, the colon is the same
# with the slicing operator in Python as in s[:] means the all element in s.
# And the slicing system works the same as Python.

# TODO
#  Exercise: Deign code that could generate these outputs.
#  1) To fetch the 1st column
#  2) To fetch 30  40
#              70  80
#  3) To fetch 60  70
#              100 110

# Now let's go through np.zeros()
# Just guess the output:

a = np.zeros(5)

print(a)
print(a.shape)
print(a.ndim)

# np.zeros(5) means: construct an array whose shape is (5, ) and fill the place with 0.

# Now let's move to 2-D np.zeros()
# Guess the output:

a = np.zeros((2, 3))
print(a)
print(a.shape)
print(a.ndim)

# Basically we are telling the Numpy the shape of our desired array:
# np.zeros((2, 3))
#            ↓
#         shape = (2, 3)
#         2 rows × 3 columns

# Look at the output again: have you wondered why NumPy gives "0." instead of 0?

# np.zeros() uses a floating-point dtype by default.

a = np.zeros(5)

print(a)
print(a.dtype)

# Why? Because NumPy is mainly used for scientific data processing and most data are in float type.

# You could assign the data type as you like.
a = np.zeros(5, dtype=int)
print(a)

# Guess the output. It should be simple:

a = np.ones((2, 3))
print(a)

# What about this?
a = np.arange(5)
print(a)

# np.arange() works similarly to Python's range(),
# but it returns a NumPy ndarray.

a = np.arange(2, 8)
print(a)
b = np.arange(2, 10, 2)
print(b)