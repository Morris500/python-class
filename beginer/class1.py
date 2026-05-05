# data = input('what is your name  ')
# print(len(data))

# a = input('a:')
# b = input('b:')

# c = a
# a = b
# b = c

# print('a =' + a)
# print('b =' + b)

#DATA TYPE
# print('hello'[0])
# k = 'njjkkj'
# print(k[1])
 
#FLOAT are decimals in py eg 3.24, Int are whole numbers, BOOLEAN are true or false STRING are letters / characters and usually come with "" 
# type() is use check data_type of a data. data type can also converted by using either str(), int(), float() e.t.c

# name = input('what is your name ')
# length = str(len(name))
# print('your name has ' + length + ' char') 

#MATH OPERATOR
# * multiplication, + addtion, - subtraction, ** exponent(raise to power), / division, // divide and round up the value. 
# score = 10
# score += 1 gives 11
# score /= 2 gives 5
# score -= 2 gives 8 

# total_bill =  int(input('waht is your total bill'))
# tip_percent = int(input('what is the tip percent'))
# no_people = int(input('how many person are to share the bill'))

# billPer_person = ((tip_percent/100) * total_bill + total_bill) / no_people 

# print(billPer_person)

#COMPARISON OPERATORS are the > greater than , < less then, >= , <= , == equal to , != not equl to e.t.c % mean modula which get the remainder of a division. 

# NOTE = One equal sign assign a value to a variable or constant while == 2 equal sign chack if the value on the left equal the value on the right

# height = int(input('what is your height '))

# if (height >= 120):
#     print('you can ride the rollercoster')
#     age = int(input('wahat is your age '))
#     if age <= 12:
#        print('pay 50 $')
#     elif age >= 13 & age <= 17 : 
#         print('pay 70 $')
#     else:
#        print('pay 100 $')    

# else:
#     print('you can not ride the rollercoster') 

#LOGIC OPERATORS are the OR ( written as. or), AND (written as. and | &), NOT (written as. not)
#IDENTITY OPERATORS are IS or IS NOT
#MEMBRESHIP OPERATOR are IN or NOT IN they if something is included in a object or array 

# number = int(input('enter a number'))
# data = number % 4
# if data == 0 and data/100 == 0 and data / 400 == 0:
#     print('it is a leap year')
# else:
#     print('it is not a leap year')    

#DOC STRING this is used to document our function when we create a function we write a documentation about that function using doc string e.g. 
# def Name_format(f_name, l_name):
#     """it takes the first  7 last name from an input"""

#DICTIONARIES ON PYTHON are yused to save data with key value pair. they are objects notation in javascript eg 
# calculator = {'multi': multiple,
            #   'subtration': sub}
# the values can be access by calling the name of the dictionary with square bracket and the name of the value you want to access eg calculator[subtration]

# n1 = 20
# n2 = 30
# sub = n1 - n2
# def multiple(n1, n2):
#     return n1 * n2

# calculator = {'multi': multiple,
#               'subtration': sub}

# operation = calculator['multi']
# answer = operation(n1, n2)
# print(f'the answer is  {answer}')

# LOOPS
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
# OR 
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break  
#   e.t.c

#With the while loop we can execute a set of statements as long as a condition is true.

# i = 1
# while i < 6:
#   print(i)
#   i += 1
#   OR
#   i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#random.choice() used to generate random number, append() is used to push/add item to a list

#Note to modify a global variable in a local scope or function we have to call the variable by using the global then the name of the variable you to modify. e.g
# car = 1
# def increse_cars():
#     global car
#     car = car + 1
#     print(car)
# increse_cars()    
 
# #  but global variable can be read inside a function it can be read e.g

# def increse_cars():
#     car3 = car + 1
#     print(car3)
# increse_cars() 

# NOTE THE DIFFERENCE between Variable and Constant variable are named with small letters while constant are named with capital letters
# car = 23 --- variable
# BUS = 30 --- constant

# from random import randint
# easy = 10
# hard = 5

# answer = randint(1,100)

# level = input('select game level E for easy or H for hard  ')
# print(level)
# def easy_level(): 
#     i = 1
#     while i <= easy:
#             playyer_answer =  int(input('guess a number  ')) 
#             if playyer_answer == answer:
#                  print('you won hurray!!!')
#                  break
#             else:
#                  if answer > playyer_answer:
#                       print(f'Answer greater than {answer} try again')
#                  else :
#                       print(f'Answer lower than {answer} try again')   
#             if i == 5:
#                  print ('game over you lost')
#             i += 1    

# def hard_level():
#     i = 1
#     while i <= hard:
#             playyer_answer =  int(input('guess a number  ')) 
#             if playyer_answer == answer:
#                  print('you won hurray!!!')
#                  break
#             else:
#                  if answer > playyer_answer:
#                       print(f'Answer greater than {answer} try again')
#                  else :
#                       print(f'Answer lower than {answer} try again')   
#             if i == 5:
#                  print ('game over you lost')
#             i += 1    


# if level =='e':
#     easy_level()

# elif level == 'h':
#     hard_level()  
# else:
#     print('select game level E for easy or H for hard  ') download pep 8 on vscode
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column('POKEMON',['dog', 'picachu','cat'], align='r')
# table.add_column('powers',['water', 'electric','fire'])
# print(table.align)
# print(table)

#CLASSES PYTHON
#  methods are functions that are allocated to a class while attribute are datas that are allocated to a particular class

class Employee:
    
    num_of_emps = 0
    raise_pay = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def fullname(self):
        return self.first, self.last   
    
    def apply_rasie(self):
        self.pay = int(self.pay * self.raise_pay or Employee.raise_pay)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
   
    @classmethod   
    def set_apply_rasie(self,boy):
        self.boy = boy
        return boy
    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp1 = Employee('Morris','Akunne',10000)
emp2 = Employee('john','peter', 15000,)

emp2.raise_pay = 1.06
name = Employee.set_apply_rasie('ade')
print(emp1.raise_pay  ) 
print(emp2.raise_pay  ) 
print(emp2.num_of_emps)
print(name)
# classmethod is a method or function that is bound to the class rather than it instance it is defined using @classmethod b4 the name of the method
# static method is a method that belongs to class but do not use the instance or the class itself. it is define using using @staticmethod.

emp_str1 = 'john-doe-70000'
emp_str2 = 'steve-smith-30000'
emp_str3 = 'jane-doe-90000'

new_emp = Employee.from_string(emp_str1)

print(new_emp) 

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_working(my_date))