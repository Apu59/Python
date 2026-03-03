#WAP to find the sum of the list n natural numbers.

#using while loop
n = int(input("Enter the limit here : "))
i = 1
sum = 0
while i <= n :
    sum = sum + i
    i += 1
print(sum)

#using for loop and range()
n2 = int(input("Enter the limit here : "))
sum1 = 0
for i in range(1,n2+1) :
    sum1 += i
print(sum1)




#WAP to find the factorial of first n natural numbers.

#using while loop
n1 = int(input("Enter the limit here : "))
fact = 1
z = 1
while z <= n1 :
    fact *= z
    z += 1
print(fact)


#using for loop and range()
n3 = int(input("Entwr the limit here : "))
fact1 = 1
for q in range(1,n3+1) :
    fact1 *= q
print(fact1)
