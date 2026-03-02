# Break and Continue in Python

# Break, It will terminate or stop the loop as per given condition
i = 0
while i <= 5 :
    if(i == 3) :
        break  #It will terminate the loop
    print(i)
    i += 1
# It will only print 1 2 3 and then terminate the loop because given condition wsa i == 3, that means when i == 3 it will terminate the loop


# Continue, It will skip or ignore the current iteration of the loop as per given condition
x = 0
while x <= 5 :
    if(x == 3) :
        x += 1
        continue  #It will skip the current iteration execution 
    print(x)
    x += 1
# It will print 0 1 2 4 5 and it will skip or ignore the 3 because given condition was x == 3, that means when x == 3 it will skip the print and go for next iteration 