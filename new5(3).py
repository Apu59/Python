#Range() in Python 

#Range() functions returns a sequence of numbers, starting from 0 bu default and increments by 1 (by default) and stops before a specified number.

#Normal range() with stoping value(compulsory)
seq = range(5)
print(seq[0]) #0
print(seq[1]) #1
print(seq[2]) #2
print(seq[3]) #3
print(seq[4]) #4

seq2 = range(5)
for i in seq :
    print(seq[i]) # 0 1 2 3 4 

for x in range(10) :
    print(x) # 0 1 2 3 4 5 6 7 8 9


#range() with starting value(optional)
for p in range(3,10) : # 3 is staring value and 10 is stoping value, it will stop just before 10, means 9
    print(p) # 3 4 5 6 7 8 9


#range() with starting and step size(optional)
for a in range(3,10,2) : # 3 is staring value, 10 is stoping value, 2 is step size means it will increase by 2
    print(a) # 3 5 7 9
 



#Pass statement in Python 
#pass is a null statement that does nothing. It is used as a placeholder for further code.

for y in range(5) :
    pass #If we don't use the pass the it will give us an error because we have to do something in loop. But pass statement will pass that and it will not give an error and next code will work without any error

print("pass statement pass the loop")
