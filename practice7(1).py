#WAF to find in which line of the file does the word "learning" occur first. Print -1 if the word is not found.

def check_for_line() :
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f :
        while data :
            data = f.readline()
            if(word in data) :
                print(line_no)
                return
            line_no += 1

    return -1


check_for_line()



#From a file containing numbers separated by comma, print the count of even numbers.

with open("practice2.txt", "r") as f :
    data2 = f.read()
count = 0
nums = data2.split(",")
for val in nums :
    if(int(val) %2 == 0) :
        count += 1

print(count)  


#This is the raw program of parsing comma separated values manually 
#     num = ""
#     for i in range(len(data2)) :
#         if(data2[i] == ",") :
#             print(int(num))
#             num = ""
#         else:
#             num += data2[i]
# print(int(num)) #Above program will not print the last value that's why we use this


