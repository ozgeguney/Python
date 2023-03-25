class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is %s!" % self.name)

#single level inheritance
#Inheritance is a process in which a subclass can inherit the attributes and methods of another class,
# allowing it to rewrite some of the super class’s functionalities
class TenYearOldPerson(Person):
    def __init__(self, name):
        Person.__init__(self, name, 10)
    def greet(self):
        print("I don't like to talk to strangers")

a = Person("Ozge", 35)
a.greet()
print(a.name, a.age)

d = TenYearOldPerson("Defne")
d.greet()
print(d.name, d.age)


class Rectangle:
    def __init__(self, x1,y1,x2,y2):
        if x1<x2 and y1 > y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
        else:
            print("Inccorect coordinates of the rectangle")
    def width(self):
        return self.x2 - self.x1
    def height(self):
        return self.y1 - self.y2
    def area(self):
        width = self.width()
        height = self.height()
        return width*height
    def perimeter(self):
        width = self.width()
        height = self.height()
        return 2*width + 2*height

    def __str__(self):
        return str(self.x1)+", " + str(self.y1)+", " + str(self.x2)+", " + str(self.y2)

    def __repr__(self):
        return "hello ozge, how are you"

#if we don' t define __str__ method, __str__ calls  __repr__ method and
# __repr__ describes the pointer of the object.

rectangle = Rectangle(2, 7, 8, 4)
print((rectangle))
print(rectangle.__str__())
print(rectangle.__repr__())
print(rectangle.width())
print(rectangle.height())
print("Area: " + str(rectangle.area()))
print("Perimeter:", rectangle.perimeter())
print("Area: %s" %rectangle.area(),"Perimeter: %s" %rectangle.perimeter())

#multi-level inheritance
#you can create a hierarchy of classes, each inheriting from its superclass.
class Animal:
    def __init__(self, name, food, characteristic):
        self.name = name
        self.food = food
        self.characteristic = characteristic
        print("I am a " + str(self.name) + ".")
class Mammal(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name, food, "warm blooded")
        print("I am a warm blooded")
class Carnivore(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
        print("I eat meat")

lion = Carnivore("lion")

#multiple inheritance
#In Python, a class can inherit attributes and methods from more than one class

class Student(Person):
    def __init__(self,name,age,rollnumber):
        Person.__init__(self, name, age)
        self.rollnumber = rollnumber
    def report(self):
        print("my roll number is " + str(self.rollnumber) + ".")
class Teacher(Person):
    def __init__(self, name, age, course):
        self.course = course
        Person.__init__(self, name, age)
    def introduce(self):
        print("I teach " + self.course + ".")
class TA(Student, Teacher):
    def __init__(self, name, age, rollnumber, course, grade):
        Student.__init__(self, name, age, rollnumber)
        Teacher.__init__(self,name, age, course)
        self.grade = grade

    def details(self):
        if self.grade == "A":
            Person.greet(self)
            Student.report(self)
            Teacher.introduce(self)
            print("I got an " + str(self.grade) + " in " + self.course)
        else:
            print(self.name + " you can not apply for TAship.")
ta = TA("Ozge",35, "12345", "Data Structure", "A")
ta.details()
ta.greet()
ta.report()
ta.introduce()

ta2 = TA("DEfne",35, "123", " Algorithm", "A-")
ta2.details()
ta2.greet()
ta2.report()
ta2.introduce()




