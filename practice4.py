#Store following word meaning in a python dict
#table : "a piece of furniture" , "list of facts and figure"
#cat : "a small animal"

dictionary = {
    "table" : ["a piece of furnoture", "list of facts and fugure"],
    "cat" : "a small animal"
}
print(dictionary)


#You are given a list of subjects for all students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# Subjects are :- "Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"

subjects = {"Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"}
print("Classrooms needed by all students are :",len(subjects))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictinary and add one by one. Use subjects name as key and marks as value.

marks = {}

x = int(input("Enter math mark : "))
marks.update({"math" : x})

y = int(input("Enter english mark : "))
marks.update({"eng" : y})

z = int(input("Enter physics mark : "))
marks.update({"phy" : z})

print(marks)


#Figure out a way to store 9 and 9.0 as separate values in the set. (You can take help of built in data types)

values = {("float", 9.0), ("int", 9)}
print(values)



