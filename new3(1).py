#Tuples in Python 
#Tuples are the built in Data structure in python which in immutable and we can store numtiple types of data in it.

tup = (1,) #For single element we must have to give comma(,) otherwise python will take it as a int or string or float value
print(type(tup))
tup2 = (2.5,)
print(type(tup2))
tup3 = ("Hello",)
print(type(tup3))
tup4 = ("Apu", 59, 3.1416) #For multiple element it is optional to give comma after the last element
print(tup4)
print(type(tup4))

#Tuples Slicing 
#Tuples slicing workd as same as like string and list slicing 
tup5 = (1,4,6,7,"Apu","Sarker",59)
print(tup5[4:6])


#Tuple Method 
tup6 = (2,5,6,9,5)

#index(), It returns the index of first occurence of the element
print(tup6.index(9)) # 3 (index)

#count(), It returns the total occurence of the element in the tuple
print(tup6.count(5)) # 2 (occurence)
