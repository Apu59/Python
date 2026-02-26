#Sets in Python 
#Set is the collection of the unordered items
#Each element in the set must be unique and immutable 
#Set will ignore duplicate elements
#Sets are mutable but elements are immutable 

collection = {1,2,3,4,5,"Hello", "World",6}
print(collection)
print(len(collection))
print(type(collection))

#Empty set
collec = set() #This is an empty set
print(type(collec))

#Set Methods

#add(), it adds  an element in the set
collec.add(1)
collec.add(2)
collec.add(2) #It will be ignore in set
collec.add(3)
collec.add("Apu")
collec.add(5.9)
collec.add((2,4,6)) #Tuple, but we can't add dict or list in set as an element because dict and lists are unhashable
print(collec)
print(len(collec))

#remove(), it will removes an element in the set 
collec.remove(3)
print(collec)
print(len(collec))

#pop(), it will removes a random value
print(collec.pop())
print(collec.pop())
print(collec.pop())

#clear(), it will clear or empties the set
collec.clear()
print(collec)
print(len(collec))

#union(), it combines both set values and returns new set
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2)) #It will return a new set which is {1,2,3,4,5}

#intersection(), it combines common values and returns a new set
set3 = {2,4,6,8}
set4 = {4,6,8,9}
set5 = {1,3,5,7}
print(set3.intersection(set4)) #It will return common values of new set which is {4,6,8}
print(set3.intersection(set5)) #It will return an empty set
