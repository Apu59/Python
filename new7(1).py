#Reading a file

f = open("hello.txt")
data = f.read(5)  #It will take first 5 character in the data 
print(data) 

line1 = f.readline() #In this line1 variable there will no Hello, because we already read the Hello word
print(line1) #It will also print a new line in output

line2 = f.readline()
print(line2) #It will also print a new line in output 

#After read whole file if we try to read more, then it will print an empty line

f.close()


#Writing a file
#There are 2 types of writing method in a file. w (write mode) which will overwright the file and another one is a (append mode) it will add character at the end of the existing characters.

# w (write mode)
f1 = open("hello.txt", "w")

f1.write("Hello , this is Apu Sarker \n and i am learning JavaScript.")

f1.close()


# a (append mode)
f2 = open("hello.txt", "a")

f2.write("\n and then i will learn ReactJS.")

f2.close()

#If we want to open a file in write or append mode and the file not exist, then python will create the file for us.

f3 = open("sample.txt", "a") #Python will create sample.txt
f3.close()

#We have more file i/o mode line r+ , w+ , a+ these mode are also important and we will study further.


#Better syntax for read and write 
with open("sample.txt", "r") as f4 :
    data2 = f4.read() 
    print(data2)

with open("sample.txt", "a") as f5 :
    data3 = f5.write("\n This is new text")

#If we use this syntax for I/O operation we don't have do close the file after operation with will close the file after finish. 



