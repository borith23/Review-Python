class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def showName(self):
        print("My name is " + self.firstName, self.lastName)

class Student(Person):
    pass
x = Student("Borith", "MOEK")
x.showName()

print("================>*(+)*<==================")

class Teacher(Student):
    def __init__(self, fname, lname, sex):
        super().__init__(fname, lname)
        self.gender = sex

    def showNameAndGender(self):
        print("My name is", self.firstName, self.lastName, "and my gender is", self.gender)

xx = Teacher("Lurna", "MOON", "Fimale")
xx.showName()
xx.showNameAndGender()

print("================>*(+)*<==================")

class Staff(Teacher):
    pass

xxx = Staff("Lucas", "Mora", "Male")
xxx.showNameAndGender()

class Student2(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.endYear = year
    def dital(self):
        print("My name is", self.firstName, self.lastName, "and year:", self.endYear)

xxxx = Student2("Nak", "DINS", 2020)
xxxx.dital()

print("================>*(+)*<==================")


# Python code showing use of iter() using OOPs 
class Counter: 
    def __init__(self, start, end): 
        self.num = start 
        self.end = end 
  
    def __iter__(self): 
        return self
  
    def __next__(self):  
        if self.num > self.end: 
            raise StopIteration 
        else: 
            self.num += 1
            return self.num - 1
                        
# Driver code 
if __name__ == '__main__' : 
      
    a, b = 2, 5
      
    c1 = Counter(a, b) 
    c2 = Counter(a, b) 
      
    # Way 1-to print the range without iter() 
    print ("Print the range without iter()") 
      
    for i in c1: 
        print ("Eating more Pizzas, couting ", i, end ="\n") 
      
    print ("\nPrint the range using iter()\n") 
      
    # Way 2- using iter() 
    obj = iter(c2) 
    try: 
        while True: # Print till error raised 
            print ("Eating more Pizzas, couting ", next(obj)) 
    except:  
        # when StopIteration raised, Print custom message 
        print ("\nDead on overfood, GAME OVER")  

    