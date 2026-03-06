#File I/O in Python 

f = open("hello.txt", "r") #It opens the file and stores the file object in variable f
print(type(f))

data = f.read() #It reads the file content and stores it in the variable data
print(data)

print(type(data)) #String

f.close() #It closes the opened file

# r (read) and t (text) modes are the default mode of files

