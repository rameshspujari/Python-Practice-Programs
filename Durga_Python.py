# # Constructor Examples By Durga Software
# class con:
#     def __init__(self):
#         print("Constructor Exe...")
# c=con()
# c1=con()
####Note: We can define multiple constructor in Python, but PVM consider only last one.
'''*************************************************************************************************'''
# class Student:
#     def __init__(self,name,age):
#         print("Constructor Exe...")
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Method Exe...")
#         print(self.name,self.age)
# obj=Student("Ramesh",20)
# obj.display()
####Note: Constructor can be executed only one time, but method can be executed any no. of times.
from array import array

'''*************************************************************************************************'''
'''
3 types of variables.
1) Instance Variable/Object level var->The variables which declared using self called Instance var.
2) Static Variable/Class level var
3) Local Variable

3 types of methods.
1) Instance Method
2) Class Method
3) Static Method
'''
'''*************************************************************************************************'''
# class Student:
#     cname="DURGASOFTWARE" #Static var
#     def __init__(self,x,y): # x,y are local var
#         self.name=x #self.name,self.age are instance var
#         self.age=y
#
#     def display(self):
#         x=10 # local var
#         print(self.name,self.age) #if you are accessing using self means it's instance method
#
#     @classmethod #Class level method data
#     def getcollegename(cls):
#         print("Colllege Name:",cls.cname)
#
#     @staticmethod #Static Method
#     def staticmethod():
#         print("This is static method..")
#
# s=Student("Ramesh",20)
# s.display()
# Student.getcollegename()
# Student.staticmethod()
'''*************************************************************************************************'''
# class student:
#     def __init__(self,name, rollno):
#         self.name=name
#         self.rollno=rollno
#
#     def info(self):
#         self.marks=80
# s1=student("Ramesh",10)
# s1.info()
# print(s1.__dict__)
'''*************************************************************************************************'''
# class Student:
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks=marks
#
#     def display(self): #Instance method
#         print(self.name,self.marks)
#
#     def grade(self):
#         if self.marks>=60:
#             print("Fist Grade")
#         elif self.marks>=50:
#             print("Second Grade")
#
#         elif self.marks>=35:
#             print("Passed")
#         else:
#             print("Fail")
# n=int(input("Enter No. of Student:"))
# for i in range(n):
#     name=input("Enter Student Name:")
#     marks=int(input("Enter Marks:"))
#     s=Student(name,marks)
#     s.display()
#     s.grade()
'''*************************************************************************************************'''
# #setter() and getter()
# class Std:
#     def setName(self, name):
#         self.name=name
#     def getName(self):
#         return self.name
#
#     def setMarks(self,marks):
#         self.marks=marks
#     def geMarks(self):
#         return self.marks
#
# n=int(input("Enter No. of Student:"))
# for i in range(n):
#     name=input("Enter Student Name:")
#     marks=int(input("Enter Marks:"))
#
#     s=Std()
#     s.setName(name)
#     s.setMarks(marks)
#
#     print("Name:",s.getName())
#     print("Marks:", s.geMarks())
'''*************************************************************************************************'''
'''
#Diff between Instance methods and Class method
instance method we have to call inside class through the objects only
Class method we can call it outside also by using object or class name.

#Diff between self and cls is that, self represents current instance object,
where cls represents the current class object. and we have to use @classmethod decorator for the cls.
'''
# class Animal:
#     legs=4
#
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs'.format(name,cls.legs))
# Animal.walk("Dog")
# Animal.walk("Cat")
'''*************************************************************************************************'''
# # Program to Track the no. of object present in the class
# class Test:
#     count=0
#     def __init__(self):
#         Test.count+=1
#
#     @classmethod
#     def getnumber_of_object(cls):
#         print("No. of object:",cls.count)
# t1=Test()
# t2=Test()
# t3=Test()
# t4=Test()
# t5=Test()
# Test.getnumber_of_object()
'''*************************************************************************************************'''
# # Static Method
# #if we are not using any instance var and static var inside method body, then we can use static method
# # we can static method by using object reference or class name.

# class Test:
#     def m1():
#         print("ABCD")
# t=Test()
# t.m1()
'''
t.m1()
TypeError: Test.m1() takes 0 positional arguments but 1 was given
bez here we are not passing self keyword to method, so it's default considered as instance method.
for instance method mandatory to pass self keyword.
'''
# #Example of Static method with @staticmethod
# class Test:
#     @staticmethod
#     def m1():
#         print("ABCD")
# t=Test()
# t.m1()
'''*************************************************************************************************'''
# # Accessing members of one class inside another class.
# class Employee:
#     def __init__(self, eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#
#     def display(self):
#         print("EMP No:",self.eno,"EMP Name:",self.ename,"EMP Sal:",self.esal)
#
#     def emp_modify(emp):
#         emp.esal=emp.esal+20000
#         emp.display()
#
# e=Employee(10,"Ramesh",10000)
# # e.display()
# Employee.emp_modify(e)
'''*************************************************************************************************'''
'''
Inner class = The class which is declared inside another class is called inner class.
Without existing outer class object there is no chance of existing inner class object. 
Inner class object is always associated with outer class object.
'''
##Example1
# class Outer:
#     def __init__(self):
#         print("Outer class object creations...")
#
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation...")
#
#         def m1(self):
#             print("Inner class method...")
#
# o=Outer() # Outer class object
# i=o.Inner() # Inner class object
# i.m1() # Inner class method calling
# ###OR####
# o1=Outer().Inner()
# o1.m1()
# ###OR####
# Outer().Inner().m1()

'''Example2'''
# class Person:
#     def __init__(self):
#         self.name="Ramesh"
#         self.dob=self.DOB()
#
#     def display(self):
#         print("Name:",self.name)
#         self.dob.display()
#
#     '''Inner class'''
#     class DOB:
#         def __init__(self):
#             self.dd=24
#             self.mm=7
#             self.yyyy=1995
#
#         def display(self):
#             print('DOB: {}/{}/{}'.format(self.dd,self.mm,self.yyyy))
# p=Person()
# p.display()
'''*************************************************************************************************'''
# # Nested Methods
'''
Nested methods help for code reusability

Garbage Collection....?
Methods 1) gc.isenabled()
        2) gc.isdisabled()
        3)gc.enable()
'''
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())
'''
Just before destroying an object, gc will call destructor method to cleanup activity.
PVM will take care of calling gc methods
'''
# import time
# class Test:
#     def __init__(self):
#         print("Object Initializations...")
#     def __del__(self):
#         print("Performing Cleanup activities...")
# t=Test()
# print(t)
# t=None
# time.sleep(5)
# print("End of Applications...")
# print(t)
# ##OR##
# del t
# print(t)
'''*************************************************************************************************'''
# class Animal(object):
#    def __init__(self, animal_type):
#       print('Animal Type:', animal_type)
#
# class Mammal(Animal):
#    def __init__(self):
#       # call superclass
#       super().__init__('Mammal')
#       print('Mammals give birth directly')
#
# dog = Mammal()
'''*************************************************************************************************'''
# # The Logging Module
'''
Levels of Log Messages...
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''
import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
'''*************************************************************************************************'''
'''
Operator Overloading implemented by internally using magic methods.
'''
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#         # print(pages)
#
#     def __add__(self, other): # Internally these methods are calling by PVM
#         return self.pages+other.pages
#
#     def __sub__(self, other):
#         return self.pages-other.pages
#
#     def __mul__(self, other):
#         return self.pages*other.pages
#
# b1=Book(10)
# b2=Book(20)
# b3=Book(50)
# print(b1+b2)
# print(b1-b3)
# print(b1*b3)

# # Overriding of Multiplication Operator
# class Emp:
#     def __init__(self, name,salary):
#         self.name=name
#         self.salary=salary
#
#     def __mul__(self, other):
#         return self.salary*other.days
#
# class Timesheet:
#     def __init__(self, name, days):
#         self.name=name
#         self.days=days
#
# e=Emp("RSP",1737)
# t=Timesheet("Ramesh",30)
# print("Monthly Salary: ", e*t)
'''*************************************************************************************************'''
# # Method overloading => python not supported method and constructor overloading
'''Same method with different arguments types, no. of arguments'''
# class Test:
#     def m1(self):
#         print("No argument method..")
#     def m1(self,x):
#         print("One argument method..")
#
# m=Test()
# m.m1()
'''*************************************************************************************************'''
# # Default argument and variable length arguments..
'''
class Test:
    def m1(self, a=None,b=None,c=None):
        if a !=None and b!=None and c!=None:
            print("Sum of 3 Numbers:",a+b+c)
        elif a!=None and b!=None:
            print("Sum of 2 Numbers:", a+b)
        else:
            print("Please provide 2 or 3 arguments...")
t=Test()
t.m1(10,20,30)
t.m1(10,20)
t.m1(10)
t.m1()
'''
'''*************************************************************************************************'''
# # Variable length arguments
# class Test:
#     def m1(self,*a):
#         total=''
#         for i in a:
#             total=total+i
#         print(total)
# t=Test()
# # t.m1(4,5)
# t.m1("Ramesh")
'''*************************************************************************************************'''
# # Method Overriding
# class Parent:
#     def property(self):
#         print("All property...")
#     def marry(self):
#         print("SSSS")
# class Child(Parent):
#     def new_marry(self):
#         super().marry()
#         print("RRRR")
# c=Parent()
# c.property()
# # c.marry()
#
# c1=Child()
# c1.new_marry()
'''*************************************************************************************************'''
'''
Types of Inheritance
1)Single inheritance
2)Multi level inheritance
3)Hierarchical inheritance
4)Multiple inheritance
5)Hybrid inheritance
6)Cyclic inheritance
'''
# #Single Inheritance
# class P:
#     def m1(self):
#         print("Parent Method..")
# class C(P):
#     def m2(self):
#         print("Child Method..")
# c=C()
# c.m1()
# c.m2()
'''*************************************************************************************************'''
# #Multi Level Inheritance
# class P:
#     def m1(self):
#         print("Parent Method..")
# class C(P):
#     def m2(self):
#         print("Child Method..")
# class CC(C):
#     def m3(self):
#         print("Sub Child Method..")
# c1=CC()
# c1.m1()
# c1.m2()
# c1.m3()
'''*************************************************************************************************'''
# # Hierarchical inheritance - One parent but multiple child class at same level.
# class P:
#     def m1(self):
#         print("Parent Method..")
# class C1(P):
#     def m2(self):
#         print("Child Method..")
# class C2(P):
#     def m3(self):
#         print("Sub Child Method..")
# c1=C2()
# c1.m1()
# c1.m3()
# print("------------------")
# c2=C1()
# c2.m1()
# c2.m2()
'''*************************************************************************************************'''
# # Multiple Inheritance - Multiple parents but only single child.
# class P1:
#     def m1(self):
#         print("Parent1 Method..")
# class P2:
#     def m1(self):
#         print("Parent2 Method..")
# class C(P1, P2):  #Here based on the sequence of the class method will be executed
#     def m1(self):
#         print("Child Method..") #If child contains method first child  only executes else sequence.
# c = C()
# c.m1()
'''*************************************************************************************************'''
# # Super() method
'''
Used for calling parent class members from child class 
main objective is that code reusability 
'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     # def dis(self):
#     #     print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age,rollno,marks):
#         # self.name = name #To avoid these super class members declarations, we are using the super()
#         # self.age = age
#         super().__init__(name,age)
#         self.rollno = rollno
#         self.marks = marks
#
#     def display(self):
#         print(self.name,self.age,self.rollno,self.marks,)
#         # super().dis() #By using this we can avoid printing of name and age again and again
#
# class Teacher(Person):
#     def __init__(self,name,age,salary,subject):
#         self.name=name
#         self.age=age
#         super().__init__(name, age)
#         self.salary=salary
#         self.subject=subject
#
#     def display1(self):
#         print(self.name,self.age,self.salary,self.subject,)
#
# s=Student("Ramesh",27,24,77)
# s.display()
# t=Teacher("Rani",28,20000,"CS")
# t.display1()
'''*************************************************************************************************'''
# # Python UnitTesting Framework
import unittest
'''
class SimpleTest(unittest.TestCase):
    # Returns True or False.
    def test(self):
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()
'''
'''
def test_sum():
    assert sum([2, 3, 5]) == 10, "It should be 10"
    print("test_sum method execution...")
if __name__ == "__main__":
    print("Ramesh")
    test_sum()
    print("Everything passed")
    print("Ramesh1")
    unittest.main()
'''
'''
def test_sum2():
    assert sum([2, 3, 5]) == 10, "It should be 10"
    print("test_sum2 method...")
def test_sum_tuple():
    assert sum((1, 3, 5)) == 10, "It should be 9"
    print("test_sum_tuple method...")

test_sum2()
test_sum_tuple()
print("Everything is correct")
unittest.main()
'''

# import unittest
# class Ramesh(unittest.TestCase):
#     def test_sum(self):
#         self.assertEqual(sum([2,3,5]),10,"This Should be 10")
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 3, 5)), 9, "It should be 10")
#
#     def RSP(self):
#         self.assertGreater((10,20),"10 is not > 20, Fail")
# if __name__ == '__main__':
#     unittest.main()
'''*************************************************************************************************'''
# # List all the indexes in the string that have capital letter
# s="HeLlO"
# # # expected:[0,2,4]
# ll=[]
# for i,j in enumerate(s):
#     if s[i].isupper():
#         ll.append(i)
# print(ll)
'''*************************************************************************************************'''
# # Return middle string, if no middle string, the return empty string
# ex1: s="abc"  output=b, ex2: s1="aaaa" output = ""
# def mid(x):
#     if len(x)%2==0:
#         return ""
#     else:
#         return x[int(len(x)/2)]
# print(mid("aacaasdddsrdsw"))
'''*************************************************************************************************'''
# # Count the number of people online in the below dictionary.
# statuses={
# "A": "Online",
# "B": "Offline",
# "C": "Online"
# }
# def online_count(statuses):
#     num=0
#     for i in statuses.values():
#         if i == "Online":
#             num+=1
#     return num
# print(online_count(statuses))
'''*************************************************************************************************'''
'''
class p:
    a=10
    def __init__(self):
        print("Parent Constructor")

    def m1(self):
        print("Parent Instance Method")
        self.b=20

    @classmethod
    def m2(cls):
        print("Parent Class Method")

    @staticmethod
    def m3():
        print("Parent Static Method")

class c(p):
    def m1c(self):
        print(super().a)
        # From child class by using super() we cannot call parent class instance variable
        # we should use self only.
        # print(super().b) #AttributeError: 'super' object has no attribute 'b'
        print(self.b)
        ####OR####
    # def __init__(self):
    #     super().__init__()
    #     super().m1()
    #     super().m2()
    #     super().m3()
cc=c()
cc.m1()
cc.m2()
cc.m3()
cc.m1c()
'''
'''*************************************************************************************************'''
# # File Handling
# l=[]
# n=int(input("Enter List Len:"))
# for i in range(n):
#     val=eval(input("Enter Values:"))
#     l.append(val)
# print(l)
# print(type(l))

'''To store the data permanently we are using files, avoid/loss of temporary data saving
Two Type of files available 1).txt file 2)Binary file
except .txt extension files, rest of all files belongs to Binary files only.
Allowed file operations mode in python are: 
Read        ->r
Write       ->w
Append      ->a
Read+Write  ->r+
Write+Read  ->w+
Append+Read ->a+
Exclusive   ->x

Same modes for binary files also, but diff is that binary files modes ends with b
ex: rb, wb, ab, r+b, w+b, a+b, x+b
'''
# f=open('rsp.txt','a')
# f.write("Ramesh\n")
# f.write("Sharanappa\n")
# f.close()
# print("Write operation completed!")
# print(f)
'''*************************************************************************************************'''
# fname= input("Enter File Name:")
# f=open('fname','w')
# feed=input("Give Your Valuable Feedback:")
# f.write(feed)
# f.close()
'''*************************************************************************************************'''
'''
File reading
f.read() -> to read total data 
f.read(n) -> to read n characters from file
f.readline() -> to read only one line 
f.readlines() -> to read all lines 
'''
# # Copy data from one file to another file
# f1=open('rsp.txt')
# f2=open("fname.txt",'w')
# f2.write(f1.read())
# f1.close()
# f2.close()
'''*************************************************************************************************'''
# # Multithreading
# import threading
# print('Current Executing Thread:',threading.currentThread().getName())
'''
3 ways we can define thread in python
1) Creating thread without using any class
2) Creating thread by extending Thread class
3) Creating thread without extending Tread class
'''
# from threading import *
# def display():
#     for i in range(10):
#         print("Child Tread")
# t=Thread(target=display()) #creatinon of thread object to execute display method
# t.start()
#
# for i in range(10):
#     print("Main Tread")
'''*************************************************************************************************'''
# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread")
# t=MyThread()
# t.start()
# for j in range(10):
#     print("Main Thread")
'''*************************************************************************************************'''
# from threading import *
# class Test:
#     def m1(self):
#         for i in range(5):
#             print("Child Thread-1")
# obj=Test()
# t=Thread(target=obj.m1())
# t.start()
# for j in range(5):
#     print("Main Thread-1")
'''*************************************************************************************************'''
# import time
# from threading import *
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double Value",2*n)
# def square(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square Values",n*n)
# numbers=[1,2]
# begintime=time.time()
# t1=Thread(target=doubles, args=(numbers,))
# time.sleep(5)
# t2=Thread(target=square, args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# endtime=time.time()
# print("Total Time Taken:",begintime-endtime)
'''
To get name=>1) t.name  2)t.getName()
To set name=>1) t.name="Ramesh" 2)t.setName("Ramesh")
'''
'''*************************************************************************************************'''
# # Generator Example
# import time
# def countdown(num):
#     print("Count down starting...")
#     while num>0:
#         yield num
#         num=num-1
# values=countdown(5)
# for x in values:
#     print(x)
#     time.sleep(1)
'''*************************************************************************************************'''
# # To Generate First N Numbers.
# def firstn(num):
#     n=1
#     while(n<=num):
#         yield n
#         n=n+1
# for i in range(5):
#     print(i)
'''*************************************************************************************************'''
# # Print first 100 number of fibonacci numbers
# def feb(n):
#     a=b=0,1
#     while 100:
#     yield a
#     a=b
#     b=a+b
# # p=feb(5)
# for i in range(feb(5)):
#     # if (i)>100:
#     #     break
#     print(i)
'''*************************************************************************************************'''
# a = int(input('Give amount: '))
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# print(list(fib(a)))
'''*************************************************************************************************'''
# # Program to find factorial using recursive function
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter Number:"))
if num<0:
    print("Invalid input...")
else:
    # print('Factorial of %d is %d' %(num,fact(num)))
    print(fact(num))
'''
# def factorial(n):
#     return 1 if n==0 else n*factorial(n-1)
# number = int(input('Enter number: '))
# if(number< 0):
#     print('Factorial does not exist!')
# else:
#     print('Factorial of %d is %d' %(number,factorial(number)))
'''*************************************************************************************************'''
# l=lambda x:x*x
# print(l(3))
#
# add = lambda x, y : x + y
# print(add(10,20))
'''*************************************************************************************************'''
# # Logger decorator
# def logger(fn):
#     from datetime import datetime, timezone
#     def inner(*args, **kwargs):
#         called_at = datetime.now(timezone.utc)
#         to_execute = fn(*args, **kwargs)
#         print('{0} executed. Logged at {1}'.format(fn.__name__, called_at))
#         return to_execute
#     return inner
# @logger
# def function_1():
#     pass
#
# @logger
# def function_2():
#     pass
#
# @logger
# def function_3():
#     pass
#
# @logger
# def function_4():
#     pass
#
# function_1()
# function_4()
# function_2()
# function_3()
# function_1()
# function_4()
'''*************************************************************************************************'''
# # Iterables
# mylist = [1, 2, 3]
# for i in mylist:
#     print(i)
'''
mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)
'''
# # Generators
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)
'''*************************************************************************************************'''
# y=0
# z=2
# x = y or z
# print(x)

# # import array as arr
# x = array('d',  [ 1.0, 2.2, 3.4, 4.8, 5.2, 6.6, 7.3])
# print("Before... ",x)
# print(x.pop())
# print(x.pop(3))
# x.remove(1.0)
# print("After... ", x)
#
'''*************************************************************************************************'''
# x = "Mindmajix Online Training"
# print(x.split())
# print("".join(x))
# try:
#     int(x)/10
# except Exception as e:
#     print("Rest of the code goes here...")
#     print(e)
'''*************************************************************************************************'''
# # Write a program to count the number of capital letters in a file?
# with open('rsp.txt') as f:
#     print(f.read())
#     c = 0
#     for i in f:
#         if i.isupper():
#             c+=1
# print(c)
'''*************************************************************************************************'''
# # count lower and upper case letters in python string
# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#       if(i.islower()):
#             count1=count1+1
#       elif(i.isupper()):
#             count2=count2+1
# print("The number of lowercase characters is:")
# print(count1)
# print("The number of uppercase characters is:")
# print(count2)
'''*************************************************************************************************'''





'''*************************************************************************************************'''






'''*************************************************************************************************'''





'''*************************************************************************************************'''









'''*************************************************************************************************'''









'''*************************************************************************************************'''




'''*************************************************************************************************'''







'''*************************************************************************************************'''