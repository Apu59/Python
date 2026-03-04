#Functions in Python 

#User defined functions

def calcSum(a,b) : #Function define with parameters
    sum = a + b
    return(sum)

outputSum = calcSum(20,10) #Function calling with arguments
print(outputSum) 


def calcAvg(a,b,c) :
    sum = a + b + c 
    avg = sum / 3
    return(avg)

outputAvg = calcAvg(10,20,30)
print(outputAvg)

#Default parameters in functions

def calcProd(a = 1, b = 1) : #Function with default parameters
    return a * b

outputProd = calcProd() #Here we can pass arguments, but if we don't pass any arguments then those default parameter will work which we set in the function
print(outputProd)
