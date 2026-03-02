#Loops in Python 
#while loop
i = 1
while i <=5 :
    print("Hello World", i)
    i+= 1

# Print numbers from 1 to 100
j = 1
while j <= 100 :
    print(j)
    j += 1


# Print numbers from 100 to 1
x = 100
while x >= 1 :
    print(x)
    x -= 1

# Print a multiplication table of a number n
n = int(input("Enter the number here : "))
y = 1
while y <= 10 :
    print(n,"*", y, "=", n*y)
    y += 1

# Print the elements of the following list using a loop 
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1

# Search for a number x in this tuple using loop
# (1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
a = 81
b = 0
while b < len(tup) :
    if(tup[b] == a) :
        print(a, "Found at index", b)
        break
    else :
        print("Finding....")
    b += 1