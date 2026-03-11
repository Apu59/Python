#Create a new file "practice.txt" using python. Add the following data in it
# Hi everyone 
# we are learning File I/O
# using C++.
# I like programming in C++.

with open("practice.txt", "w") as f :
    f.write("Hi everyone\nwe are learning File I/O\nusing C++.\nI like programming in C++.")




#WAP that replaces all occurrences of "C++" with "python" in above file.

with open("practice.txt", "r") as f :
    data = f.read()

new_data = data.replace("C++", "Python")
print(new_data)

with open("practice.txt", "w") as f :
    f.write(new_data)




#Search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt", "r") as f :
    data2 = f.read()
    idx = data2.find(word)
    if(idx != -1) :
        print(word, "Found at index", idx)
    else :
        print("Not Found")