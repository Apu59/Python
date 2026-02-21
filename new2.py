#Strings in Python 
str1 = "Hello World"
str2 = 'Helow world'
str3 = """Hello World"""  #All are valid string in python

#Escape sequence character in Python 
str4 = "This is a string. \nWe are creating it in Python" #It will give a new line
print(str4)

str5 = "This is a string. \tWe are creating it in Python" #it will give a tab
print(str5)

#String concatinate
str6 = "Hello"
str7 = "World"
concatinateString = str6 + str7 #It will print HelloWorld
print(concatinateString) 

#Length of string
print(len(str6)) #len() is a function in python which will return the length of any string 
conStr = str6 + " " + str7
print(len(conStr)) #it will return 11 because we add a space between str6 and str7. Space will count as length


#Indexing 
str8 = "Hello World"
ind = str8[6] #It is pointing the 7th character of the string which is W
print(ind)  #it will print W

#Slicing 
str9 = "Sarker" 
print(str9[1:4]) #It will print ark, 1 is denoting starting index and 4 is denoting the next index of ending
print(str9[3:6]) #It will print ker 
print(str9[3:len(str9)]) #It also will print ker because string length is 6
print(str9[3:]) #It will also print ker, because puthon will automatically detect the last index
print(str9[:3]) #It will print Sar, because python will automatically detect the staring index 

#Negative Index
print(str9[-3:-1]) #It will print ke because starting -3 which is k (From right side) and ending -1 that means it will print till -2 which is e
# -6 is S, -5 is a, -4 is r, -3 is k, -2 is e -1 is r , That's why it will return ke

#String Functions 

str10 = "hello this is Apu Sarker"

#endswith()
print(str10.endswith("ker")) #The endswith() function returns bool value, and it will return True because the ending sub string is ker

#capitalize()
print(str10.capitalize()) #It will convert the first character in Capital and rest of them in small
#and the function don'r change into the original string, it will create another string and then change it

#replace()
print(str10.replace("hello", "Hey")) #It will replace hello with Hey
print(str10.replace("r", "R")) #It will replace every r with R in the string 

#find()
print(str10.find("A")) #It will return the index where first A present in the string 
print(str10.find("Sarker")) #It will return the index where the first Apu is present in the string 

#coutn()
print(str10.count("e")) #It will return the number how many times e is present in the string 
print(str10.count("Apu")) #It will return the number how many times Apu is present in the string 





