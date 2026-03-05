#Recursion in Python 
def show(n) :
    if(n == 0) : #This is base, whent it hits the recursive call will stop
        return
    print(n)
    show(n-1)

show(5)

#Factorial using recursion

def fact(n) :
    if(n == 1 or n == 0) :
        return 1
    return fact(n-1) * n

n = int(input("Enter the nmber here : "))
print(fact(n))
