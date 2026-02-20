print("Hello World")  #frist program

name = "Apu Sarker" #string
age = 23            #int
money = 499.99      #float
canPlayCricket = True  #bool
score = None           #none


print("This is",name, "age is",age, "he have",money, "Taka", 
"Can he play cricket?",canPlayCricket, "the score is",score)   #Printing variables

print(age+money)  #adding variables

#finding the type of variables
print(type(name))  
print(type(age))
print(type(money))
print(type(canPlayCricket))
print(type(score))

#Arithmetic operators 
a = 5
b = 2

add = (a + b)
print(add)

sub = (a - b)
print(sub)

mul = (a * b)
print(mul)

div = (a / b)
print(div) # Div always gives floating value althought it can give int value. It returns 2.0

mod = (a % b) # Reminder
print(mod) 

pow = (a ** b) #Power a^b
print(pow)

#Relational Operators 
c = 10
d = 20
#Relation operaors return bool values 
print(c == d) #False
print(c != d) #True
print(c > d) #False
print(c >= d) #False
print(c < d) #True
print(c <= d) #True

#Assignment Operators 
num = 5
num = num + 10
num += 10
num -= 10
num *= 10
num /= 10
num %= 10
num **= 10
print(num)

#Logical operators 
#Logical operator works on bool values
#not operator
print(not True) #False
print (not False) #True

val1 = True
val2 = False
print("AND operator", val1 and val2) #False, AND will return true when both conditions are true
print("OR operator", val1 or val2) #True, OR will return true when if any of the condition is true

#Type Conversion
#Type conversion is when python automaticaly convert from any data type to another 
x = 2 #int
y = 2.59 #float
sum = (x + y) # 2.0 + 2.59 = 4.59 Here python automaticaly convert the int into float and dis the sum and the sum also return a float value
print(sum) #4.59 which is a float value 

#Type casting 
#Type casting is when we forcefully convert from any data type to another 
s = "3" #strig, in this situation we can't perform arithmetic operation because we can't add a string with a int
p = 4 #int
r = int(s) #Now s is a int value and we can perform arithmetic operations
sum = (p + r)  # 3 + 4 = 7
print(sum) #It will return a int value

#Input in python 
input("Please enter your name : ") #This is normal input in python 
name = input("Please enter your name : ") #This will take the input in a variable 
print("Welcome",name) 
#Python always takes input as a string if we need to convert in another data type we have to use type casting 
val = int(input("Please enter you age :")) #Now it will take the input and convert in a int value
print(type(val), val)



