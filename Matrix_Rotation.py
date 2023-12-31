import numpy
# matrix Rotation


def rotate_left(m1: numpy.ndarray) -> numpy.ndarray:
	assert len(m1.shape) == 2, "Not a Matrix"
	assert type(m1) is numpy.ndarray, "Not an array"

	r1 = c2 = len(m1)
	r2 = c1 = len(m1[0])
	m2 = numpy.zeros((r2, c2))
	print(r1, c1, r2, c2)
	k2 = r2
	for i in range(r2):
		k2 -= 1
		for j in range(c2):
			m2[i][j] = m1[j][k2]
	return m2


def rotate_right(m1: numpy.ndarray) -> numpy.ndarray:
	assert type(m1) is numpy.ndarray, "Not an array"
	assert len(m1.shape) == 2, "Not a Matrix"
	r1 = c2 = len(m1)
	r2 = c1 = len(m1[0])
	m2 = numpy.zeros((r2, c2))
	print(r1, c1, r2, c2)

	for i in range(r2):
		k2 = c2
		for j in range(c2):
			k2 -= 1
			m2[i][j] = m1[k2][i]
	return m2


def rotate_about(m1: numpy.ndarray) -> numpy.ndarray:
	assert type(m1) is numpy.ndarray, "Not an array"
	assert len(m1.shape) == 2, "Not a Matrix"
	r2 = len(m1)
	c2 = len(m1[0])
	m2 = numpy.zeros((r2, c2))

	i2 = r2
	for i in range(r2):
		i2 -= 1
		j2 = c2
		for j in range(c2):
			j2 -= 1
			m2[i][j] = m1[i2][j2]
	return m2


# This works fine for all matrices, NxM, Row, Column Matrices
# arr = numpy.array([[2, 8, 9, 6], [4, 1, 2, 3], [9, 7, 8, 1], ])
# arr = numpy.array([[2, 8, 9, 6], ])
arr = numpy.array([[2], [8], [9], [6]])

matrix_left = rotate_left(arr)
matrix_right = rotate_right(arr)
matrix_about = rotate_about(arr)

print("\t\t\tOriginal Matrix: \n", arr)
print("\t\t\tRotated Left: \n", matrix_left)
print("\t\t\tRotated Right: \n", matrix_right)
print("\t\t\tRotated About: \n", matrix_about)

# m = rotate_left(numpy.array([2, 8, 9, 6]))  # Not a Matrix
# the shape attribute exists here as it is a numpy.ndarray object
# So, this will obviously throw an Assertion Error
# m1 = rotate_left([1,2,3,4])  # Not a numpy-array
