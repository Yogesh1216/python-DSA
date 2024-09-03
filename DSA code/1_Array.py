# array = collection of same type of elements
#         fixed size,indexed,mutable

# list = collection of heterogenious elements
#        not fix size (dynamic array),mutable

from array import *

# Array CRUD

#create
a1 = array('i',[10,20,30])

# read
for i in a1:
    print(i)
    
for i in range(3):
    print(a1[i])

#update (in python array is also growable)
a1.append(5)
print(a1)

a1.insert(0,50)
print(a1)

# delete
a1.pop()
print(a1)

a1.pop(0)  
print(a1)

a1.remove(10)
print(a1)

# reverse() , toList() ....etc

# List Crud

# create
l1 = []
l1 = [10,20,30]
l1 = [1,"yogesh",26]

# read
for i in l1:
    print(i)
    
# update   append(),insert(index,value):
l1.append("soft developer")
print(l1)

# delete = pop() ,pop(index),remove(value)

# reverse() , sort() , , len() , sum() , min() , max() , sort()



# for mathematical calculation we should use numpy to create array 
# pip install numpy
import numpy as np
# create
a = np.array([10,20,30])
a1 = np.array([[1,2,3],[4,5,6]])  #2d array

#read
for i in a:
    print(i) 

print(a1)
