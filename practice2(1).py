#WAP to check if a number entered by the user is odd or even

num = int(input("Enter you number here : "))
rem = num % 2

if(rem == 0):
    print("The number is Even.")
else:
    print("The number is Odd.")


#WAP a program to find greatest of 3 numbers entered by the user 

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the thired number : "))

if(num1 >= num2 and num1 >= num3):
    print("First number is largest.")
elif(num2 >= num3):
    print("Second number is largest.")
else:
    print("Thired number is largest.")


#WAP to check if a number is a multiple of 7 or not

number = int(input("Enter the number here : "))
rem1 = number % 7 

if(rem1 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")