#For loop in Python 
#For loops basically used for sequential traversal like for traversing list,string,tuples etc

list = [1,2,3,4,5]
for el in list :
    print(el) #It will print 1 2 3 4 5


tup = (6,7,8,9,10)
for val in tup :
    print(val) #It will print 6 7 8 9 10


string = "ApuSarker"
for char in string :
    print(char) #It will print A p u S a r k a r



#We can add optional else with for loop 

list2 = [2,4,6,8,10,12,14,16,18,20]
for i in list2 :
    print(i)
else :
    print("The END") #If we want to do something after the end of the whole loop we can add the thing in the else condition. The END will print after complete the whole loop



#Print the elements of the following list using a for loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for z in list3 :
    print(z)


#Search for a number x in this tuple using loop 

list4 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 81]
x = 81
indx = 0
for elm in list4 : 
    if(elm == x) :
        print(x, "is found at the index", indx)
        # break
    else :
        print("Finding...")
    indx += 1


    