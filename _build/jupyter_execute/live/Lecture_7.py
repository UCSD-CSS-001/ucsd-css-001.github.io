#!/usr/bin/env python
# coding: utf-8

# # Classes, Objects, etc.
# 
# ## High level
# 
# ### What is an object?  What is a class?
# 
# - `type()`

# In[1]:


x = 'hello world'
type(x)


# In[2]:


x.upper()


# In[3]:


dir(x)


# ### peeking inside objects
# 
# - Example: dictionary
# 
# - `dir()`
# 
# - `vars()`  (mostly for home-made classes)
# 
# 
# ### Why Object Oriented Programming
# 
# - aligns with our conception of the stuff we want to work with.
# 
# - e.g., courses, courses have instructors, courses have students.  each has particular properties, and particular operations we might want to do on them.  organizing our code accordingly makes life easier.
# 
# ## Defining a class

# In[4]:


class Person():
    def __init__(self, birthyear, name, birthmonth, birthday):
        self.birthyear = birthyear
        self.name = name
        self.birthmonth = birthmonth
        self.birthday = birthday
    
    def getAge(self, year):
        return year-self.birthyear
    
    def summary(self):
        return f'{self.name} was born in {self.birthyear}'
    
    def greet(self, year, month, day):
        if month == self.birthmonth and day == self.birthday:
            return f'Happy birthday {self.name}, today you are {year-self.birthyear+1} years old!'
        else:
            return f'Hi {self.name}'

ed = Person(1982, 'Ed Vul', 1, 10)
alice = Person(1998, 'Alice Aardvark', 2, 12)
bob = Person(2004, 'Bob Beaver', 3, 18)


# In[5]:


ed.greet(2020, 1, 10)


# In[6]:


bob.summary()


# In[7]:


type(ed)


# In[8]:


vars(ed)


# In[9]:


dir(ed)


# In[10]:


ed.getAge(2031)


# In[11]:


ed.summary()


# - class attributes vs instance attributes

# In[12]:


class Dog():
    sound = 'woof'
    def __init__(self, name):
        self.name = name
    
    def introspect(self):
        print(vars(self))
        
    def speak(self, n):
        print(self.name, 'says', self.sound*n)

rover = Dog('rover dogface')
spike = Dog('spike dog')

rover.speak(2)
spike.speak(1)


# - `__init__()` constructor.
# 
# - `self` 

# In[13]:


# attributes of a student
# student.courses list of completed courses, and their associated units, and grades
# student.name 
# student.id student id
# student.enrollment_year

# methods of a student
# addCourse()  add a course to courses.
# getGPA()  get unit-weighted gpa of courses
# getStanding(year)   returns freshman, sophomore, junior, senior, supersenior

class Student():
    def __init__(self, name, student_id, enrollment_year):
        self.name = name
        self.student_id = student_id
        self.enrollment_year = enrollment_year
        self.courses = dict()
    
    
    def __repr__(self):
        return f'Student({repr(self.name)}, {repr(self.student_id)}, {repr(self.enrollment_year)})'
       
    
    def addCourse(self, course_name, units, grade):
        self.courses[course_name] = [units, grade]
        
    def getGPA(self):
        # sum(grade * unit) / sum(unit)
        grade_units = 0
        units = 0
        for k,(u,grade) in self.courses.items():
            units += u
            grade_units += grade*u
        if units == 0:
            return None
        else:
            return grade_units / units
        
    def getStanding(self, year):
        if (year - self.enrollment_year) == 0:
            return "freshman"
        elif (year - self.enrollment_year) == 1:
            return "sophomore"
        elif (year - self.enrollment_year) == 2:
            return "junior"
        elif (year - self.enrollment_year) == 3:
            return "senior"
        elif (year - self.enrollment_year) > 3:
            return "supersenior"
    
    def getTranscript(self, year):
        print(f'Transcript of {self.name}')
        print(f'Enrolled since {self.enrollment_year}')
        print(f'Current standing is {self.getStanding(year)}')
        for course_name,(units,grade) in self.courses.items():
            print(f'{course_name} ({units} units) grade: {grade}')
        print(f'Total GPA: {self.getGPA()}')
        


# In[14]:


ed = Student(name = 'Ed Vul', student_id = '1234', enrollment_year = 2019)
ed.addCourse('CSS1', 4, 3.33)
ed.addCourse('CSS2', 4, 3.67)
ed.addCourse('COGS18', 4, 3)
ed.addCourse('ECON 5A', 6, 2.67)

alice = Student('Alice', '1432', 2018)
alice.addCourse('CSS1', 4, 4.0)
alice.addCourse('CSS2', 4, 3.337)
alice.addCourse('COGS18', 4, 3)
alice.addCourse('ECON 5A', 6, 3.67)
alice.addCourse('MATH 18', 4, 4)


# In[15]:


ed.getGPA()


# In[16]:


alice.getTranscript(2020)


# In[17]:


ed.addCourse('PSYC 199', 2, 4)


# In[18]:


ed.getTranscript(2021)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


vars(alice)


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


ed.getTranscript(2020)


# In[80]:





# In[21]:


alice.getGPA()


# In[22]:


vars(alice)


# In[23]:


alice.getStanding(2021)


# ### Creating instances
# 
# ### Methods
# 
# ## Everything is an object

# In[24]:


x = 4
x.denominator


# In[25]:


x.numerator


# In[26]:


x = ' '
x.join(['a', 'b'])


# In[27]:


x = {'a':3, 'b':4}


# In[28]:


print(ed)


# In[29]:


ed


# In[30]:


repr(x)


# ### Dunder methods and duck typing
# 
# - __repr__()
# 
# - __add__()
# 

# In[31]:


class Dog():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Dog("{self.name}", {self.weight})'
    
    def speak(self):
        if self.weight > 40:
            return "woof"
        else:
            return "arf"

rover = Dog('rover dogface', 50)


# In[32]:


str(45)


# In[33]:


class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __repr__(self):
        return f'Rectangle({self.height}, {self.width})'
    
    def __add__(self, other_rectangle):
        return Rectangle(self.height+other_rectangle.height, self.width+other_rectangle.width)
    
    def area(self):
        return self.height*self.width


# In[34]:


r1 = Rectangle(4, 3)
r2 = Rectangle(10,20)

r1 + r2


# In[35]:


dir('2345')


# In[36]:


len('1234')


# In[ ]:





# # Practice
# 
# Class: BankAccount
# 
# Attributes:  
# - balance
# - owner_name
# - number
# - type
# 
# Methods:
# - deposit
# - withdraw
# - getHistory
# 

# In[37]:


from random import randint

class BankAccount():
    def __init__(self, owner_name, account_type):
        self.owner_name = owner_name
        self.account_type = account_type
        self.balance = 0
        self.number = randint(100, 999)
        self.transactions = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append("deposit: " + str(amount))
        return True
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append("withdraw: " + str(amount))
            return True
        else:
            print("Insufficient Funds")
            return False
        
    def getStatement(self):
        print(f'{self.account_type}(#{self.number}) of {self.owner_name} ')
        for transaction in self.transactions:
            print(transaction)
        print("Final Balance: " + str(self.balance) )
        return None
    


# In[38]:


account = BankAccount('Ed Vul', 'checking')

account.deposit(1000)
account.deposit(500)
account.withdraw(750)
account.withdraw(75)

account.balance

account.getStatement()


# In[39]:


account2 = BankAccount('Ed Vul', 'savings')


# In[40]:


account2.getStatement()


# In[41]:


account2.deposit(88)


# In[42]:


account2.getStatement()


# In[ ]:




