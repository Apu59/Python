#WAF to print the length of a list. (List in the parameter)

cities = ["Dhaka", "Rajshahi", "Chitagong", "Khulna", "Rangpur", "Barishal"]
language = ["C++", "JavaScript", "Python", "Assembly", "SQL"]

def printLength(list) :
    print(len(list))

printLength(cities)
printLength(language)



#WAF to print the elements of a list in a single line. (list in the parameter)
def printElements(list) :
    for i in list :
        print(i, end = " ")
printElements(cities)




print("\n")


#WAF to find the factorial of n. (n in the parameter)
def fact(n) :
    fact1 = 1
    i = 1
    while i <= n :
        fact1 *= i
        i += 1
    return(fact1)

n = int(input("Enter the number here : "))
facto = fact(n)
print(facto)



#WAF to convert USD to BDT
def converter(USD) :
    bdt_value = USD * 122
    print(USD, "USD = ", bdt_value, "BDT")

x = int(input("Enter the USD amount you want to convert : "))
converter(x)


#WAF to check is the number is Even or Odd. (Number in input)
def evenOrOdd(n) :
    if(n%2 == 0) :
        print("Even")
    else :
        print("Odd")

p = int(input("Enter the number here : "))
evenOrOdd(p)


