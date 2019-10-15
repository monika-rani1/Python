# x = lambda a,b,c,d : a*b*c*d
# print(x(4,5,1,2))

# def my_fun(n):
# 	return lambda a : a*n

# doubler = my_fun(2)
# print doubler(2)

# Merge two sorted Array

from array import *
array1 = array('i',[1,3,2,4])
array1_1 = sorted(array1)
array2 = sorted(array('i',[6,8,2,4,5]))
array1_1.append(array2)
print array1_1

