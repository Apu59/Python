#Solve these practice question by using for and range()

#Pring numbers from 1 to 100
for i in range(1,101) :
    print(i)


#Print numbers from 100 to 1
for x in range(100,0,-1) :
    print(x)


#Print the multiplication table of a number n
n = int(input("Enter the number here : "))
for p in range(1,11) :
    print(n, "X", p, "=", n*p)