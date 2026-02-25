#Dictionary in Python
#Dict is a built in Data Structure in Python which is mutable and we can store data as key : value pairs 
#Dictionary are unordered, mutable and don't allow duplicate keys

dict = {
    "key" : "value",
    "name" : "Apu",
    "age" : 23,
    "learning" : "python",
    "is_learning" : True,
    "cgpa" : 3.5,
    "subjects" : ["python", "c++", "javascript"], #We can store list in dict
    "sub" : ("c", "assembly", "bash"), #We can store tuple in dict
    10 : 10,
    3.5 : False,
}

print(dict) #It will print the whole dict
print(type(dict)) #dict
print(len(dict)) #10

#We can access values by call their key from a dict
print(dict["name"]) #Apu
print(dict["age"])  #23
print(dict["sub"])  #("c", "assembly", "bash")
print(dict["is_learning"]) #True
print(dict["subjects"]) #["python", "c++", "javascript"]
print(dict[10]) #10

#We can change the value 
dict["name"] = "Sarker" #It will change the value of name key with Sarker
print(dict)

#We can assign a new key:value in dict 
#If we assign a new value with same key, it will overwrite with the new value 
dict["game"] = "cricket" #It will add another key:alue pair in the dict 
print(dict)

#We can also create empty dict and can assign key:value pairs in it 
null_dict = {}
print(null_dict)
null_dict["name"] = "Apu Sarker"
print(null_dict)

#Nested Dictionary
student = {
    "name" : "Apu Sarker",
    "subjects" : {
        "DSA" : 90,
        "DBMS" : 88,
        "TOC" : 85,
    }
}
print(student) #Full dict
print(student["subjects"]) #Nested dict 
print(student["subjects"]["TOC"]) #Value inside nested dict which is 85


#Methods in Dictionary 

#keys(), it wll return all the keys from the dict 
print(student.keys()) #It will not return the nested dict key, it will only return name and subjects
print(list(student.keys())) #We can also print the result in a list or tuples by casting 
print(len(list(student.keys()))) #We also can print the list length
print(tuple(student.keys())) 
print(len(tuple(student.keys())))


#values(), it will return all the vlaues from the dict
print(student.values()) #It will return all the vlaues of the dict
print(list(student.values())) #Casting the vlaues in a list 
print(len(list(student.values()))) #We also can print the length of casted list


#items(), it will return all key:value pairs in a tuple
print(student.items()) 
print(list(student.items())) #Casted tupls into list
#We can also access the element of the casted list or tuple
pairs = list(student.items()) 
print(pairs[0]) #It will return the first pair of element from casted list which is name , Apu Sarker  


#get(), it will return the key according to value 
#We need get() method because if we try to access a value with its key which is not exist in the dict then it will not give error, it will give None 
print(student.get("name")) #Apu Sarker 


#update(), insert  the specified items to the dictionary 
info = {
    "name" : "Apu",
    "age" : 23
} 
info.update({"city" : "Dhaka"}) #We can add new key:value pair in dict
new_dict = {
    "name" : "Sarker", #If we can add a new dict which key is duplicate, it will overwrite the old value
    "game" : "cricket",
    "equipment" : "bat"
}
info.update(new_dict) #We can add new dict in the dict

print(info)

