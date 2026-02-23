#Lists in Python
#Lists are the built in Data Structure in python which is mutable and we can store multiple types of data in it.

student = ["Apu", 12, 3.14, "Dhaka"]
print(type(student)) #list
print(student)
print(student[2])
student[0] = "Sarker" #It will Apu with Sarker
print(student)
print(len(student)) #4

#List Slicing 
#List slicing works as like string slicing 

marks = [10, 20, 30, 40, 50]
print(marks[1:4]) # 20, 30, 40
print(marks[:3]) # 10, 20, 30
print(marks[2:]) # 30, 40, 50
print(marks[1:len(marks)]) # 20, 30, 40, 50
print(marks[-4:-1]) # 20, 30, 40

#List Methods

#append(), it will add another value in the list at the last index
list =[1,7,5,4,8,6]
print(list)
list.append(9) #It will return None, because it changes in the original list
print(list) # 1,7,5,4,8,6,9

#sort(), it will sort the list in ascending order
list.sort() #It will return None, because it changes in the original list 
print(list) # 1,4,5,6,7,8,9
list.sort(reverse=True) #It will sort the list in descending order
print(list) # 9,8,7,6,5,4,1

list2 = ["a", "d", "c", "b"] #Sorting in string or character
list2.sort()
print(list2) # a,b,c,d
list2.sort(reverse=True)
print(list2) #d,c,b,a

#reverse(), it will reverse the whole list
list3 = [12,65,67,34,21,54]
list3.reverse() 
print(list3) # 54,21,34,67,65,12

#insert(), it will add an element in the list at particular index
list4 = [10,20,40,50,60]
list4.insert(2,30) #2 is the index number and 30 in the element
print(list4) # 10,20,30,40,50,60

#remove(), it will remove the first occurrence of the element
list5 = [2,3,1,4,5,1,6]
list5.remove(1) #It will remove first 1 from the list
print(list5) # 2,3,4,5,1,6

#pop(), it will remove/pop an element from a particular index
list6 = [2,3,4,6,7,8,9]
list6.pop(3) #it will remove 6 from the list
print(list6) # 2,3,4,7,8,9










