#Write a recursive function to calculate the sum of list n natural number.

def sum(n) :
    if(n == 1) :
        return 1
    return sum(n-1) + n 

n = int(input("Enter the n here : "))
print(sum(n))


#Write a recursive function to print all elements in a list.

def printElem(list, idx) :
    if(idx == len(list)) :
        return
    print(list[idx], end = " ")
    printElem(list, idx+1)

list = [1,2,3,4,5,6,7,8,9]
idx = 0
printElem(list, idx)
