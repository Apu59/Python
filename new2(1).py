#Conditional Statemtn 

#Grading system using conditinal statement 

mark = int(input("Please enter your marks here : "))

if(mark > 100 or mark < 0):
    print("Please enter a valid mark.") #indentation is important in Python, indentation means proprr spacing
elif(mark >= 90):
    print("Your grade is : A")
elif(mark < 90 and mark >= 80):
    print("Your grade is : B")
elif(mark < 80 and mark >=70):
    print("Your grade is : C")
elif(mark < 70 and mark >= 50):
    print("Your grade is : D")
else:
    print("Your grade is : F")


#Nesting in Python

age = int(input("Enter your age here : "))

if(age >= 18):
    if(age >= 80):
        print("You can't driveeee")
    else:
        print("You can drive")
else:
    print("You can't drive")