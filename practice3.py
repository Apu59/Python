#WAP to ask the user to enter names of their 3 favorite movies and store them in a list

movies = []
movies.append(input("Enter 1st movie name : "))
movies.append(input("Enter 2nd movie name : "))
movies.append(input("Enter 3rd movie name : "))

print(movies)


#WAP to check if a list contains a palindrome of elements.

list = [1,"abc","abc",1]
copyList = list.copy()
copyList.reverse()

if(list == copyList):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")


#WAP to count the number of students with the "A" grade in the following tuple.

tup = ("C", "D", "A", "A", "B", "B", "A")
totalAgrade = tup.count("A")
print("Total number of student with grade A : ",totalAgrade)


#Store the above values in a list and sort them form "A" to "D"

sList = ["C", "D", "A", "A", "B", "B", "A"]
sList.sort()
print(sList)