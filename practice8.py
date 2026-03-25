#Create student class that takes name & marks of 3 students as arguments in constructor.Then create a method to print the avrage.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_of_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello,",self.name,"your avrage mark is : ", sum/3)


s1 = Student("Stark", [91, 93, 95])
s1.avg_of_marks()