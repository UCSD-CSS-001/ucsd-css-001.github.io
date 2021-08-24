#!/usr/bin/env python
# coding: utf-8

# # Lecture 7: Objects and classes

# ## Why objects?
# 
# Data and methods are often conceptually bundled.  Consider something as simple as a date.  How should we represent/store it?  How do we want to use it?

# In[1]:


today = "August 24, 2021"
today = (2021, 8, 24)
today = {'year': 2021, 'month': 8, 'day': 24}
today = 2021*365 + 8*30 + 24
today_year = 2021
today_month = 8
today_day = 24


# In[2]:


# print it nicely?
# print it in different formats.  2021-08-24, 08/24/2021, 24/8/2021
# subtraction.  how many days between today and new year?

def date_print_words():
    
def date_print_american():

def date_print_rest():

def date_subtract():


# In[3]:


from datetime import date

today = date(2021, 8, 24)


# In[4]:


today.isoformat()


# In[5]:


dir(today)


# **objects are bundles of related attributes (data) and methods (functions)**

# ## Defining classes, creating instances
# 
# ### Defining classes
# 
# **a class is an object template.**

# In[6]:


class UselessObject:
    x = 10
    def print(self):
        print('my value of x is: ', self.x)


# In[7]:


useless_1 = UselessObject()
useless_2 = UselessObject()


# In[8]:


useless_1.print(4)


# #### class attributes
# 
# #### class methods 
# 
# **all class methods have `self` as the first argument**.  `self` is never *explicitly* passed in a method call, but is inserted implicitly.  This can yield confusing error messages.

# ### Instances, constructor, and self
# 
# #### __init__
# 
# **the `__init__` method is the *constructor*, setting up instance attributes**

# In[9]:


class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def speak(self):
        print(f'Hi, my name is {self.name}, ' + 
              f'and I weight {self.weight} lbs')


# In[10]:


dog1 = Dog('rover', 67)
dog2 = Dog('sparky', 15)


# In[11]:


dog2.name


# In[12]:


dog1.speak()


# In[13]:


dog2.speak()


# In[14]:


dog1.name = 'foo'

dog1.speak()
dog2.speak()


# #### instances
# 
# **an instance of a class is a specific object made from that class template**
# 
# #### self
# 
# **`self` is the conventional name assigned to the first class method argument, which always points to the instance itself** 
# 
# Why do we need `self`?

# In[15]:


class Student:
    # name
    # id
    # year of enrollment
    # course_history: dictionary of classes.
    def __init__(self, name, student_id, enrollment_year):
        self.name = name
        self.student_id = student_id
        self.enrollment_year = enrollment_year
        self.course_history = dict()
    
    def take_course(self, course_name, course_grade):
        self.course_history[course_name] = course_grade
    
    def gpa(self):
        grades = self.course_history.values()
        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return None
    


# In[16]:


student1 = Student('ed vul', 'a0156474', 2010)
print(student1.name, student1.student_id, student1.course_history)


# In[17]:


student1.take_course('css1', 2.8)
student1.take_course('css2', 3.5)
student1.take_course('psyc1', 4.0)
student1.take_course('econ1', 4.0)
student1.take_course('cogs1', 4.0)


# In[18]:


x = [1, 2, 3]
x.append(4)


# In[19]:


student1.course_history


# In[20]:


student1.gpa()


# In[21]:


student2 = Student('erik', '8', 2018)

student2.take_course('css1', 2.8)
student2.take_course('css2', 2.4)
student2.take_course('econ3', 3.4)
student2.take_course('econ5', 4.4)
student2.take_course('econ100', 100.4)


# In[22]:


student2.gpa()


# In[ ]:





# In[23]:


student1_name
student1_id
student1_enrollment_year
student1_course_history

def gpa(course_history):


# In[ ]:





# In[24]:


students = [Student('ed', 'id34', 2010), 
            Student('erik', 'id61234', 2018)]


# In[25]:


for student in students:
    student.take_course('psyc1', 3.5)


# In[26]:


for student in students:
    print(student.name, student.course_history['psyc1'])


# In[27]:


# bank account class
# attributes?  number, balance, name
# methods?  withdraw, deposit, statement

from random import randint

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.number = str(randint(10**9, 10**10-1))
        self.transactions = []
    
    def deposit(self, amount):
        """takes amount and adds to balance"""
        
        if amount > 0:
            # add amount to balance
            self.balance += amount
            self.transactions.append(['deposit',amount])
        else:
            print("Can only deposit positive money")
    
    def withdraw(self, amount):
        """subtracts amount from balance..."""
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(['withdraw',amount])
    
    def statement(self):
        summary = f'Bank Account # {self.number}\n' +                f'Owner: {self.name}\n' +                f'Balance: {self.balance}'
        transaction_history = ''
        for transaction in self.transactions:
            transaction_history += f'\n {transaction[0]} {transaction[1]}'
            
        return(summary + transaction_history)


# In[28]:


checking = BankAccount('ed vul')
savings = BankAccount('erik')
checking.deposit(100)
print(checking.balance)
print(savings.balance)


# In[29]:


savings.balance


# In[30]:


print(f'{checking.name=}, {checking.number=}, {checking.balance=}')


# In[31]:


checking.deposit(100)
print(f'{checking.name=}, {checking.balance=}')
checking.withdraw(20)
print(f'{checking.name=}, {checking.balance=}')
checking.withdraw(20)
print(f'{checking.name=}, {checking.balance=}')
checking.withdraw(20)
print(f'{checking.name=}, {checking.balance=}')
checking.deposit(200)
print(f'{checking.name=}, {checking.balance=}')
checking.withdraw(240)
print(f'{checking.name=}, {checking.balance=}')
checking.deposit(300)
print(f'{checking.name=}, {checking.balance=}')
checking.withdraw(500)
print(f'{checking.name=}, {checking.balance=}')


# In[32]:


print(checking.statement())


# ### Summary
# 
# object: bundle of attributes and methods
# 
# class: is a template
# 
# instance of a class: 

# ## Advanced 
# 
# ### Everything in Python is an object
# 
# `dir`

# In[33]:


isinstance(BankAccount, object)


# In[34]:


dir([1, 2, 3])


# In[35]:


x = [1, 2, 3]
y = [4, 5, 6]
x.append(100)
print(x, y)


# ### class attributes vs instance attributes
# 
# - again, difference between mutable and immutable, like local vs global variables in functions
# 
# - if it will change, it should probably be an instance attribute.

# ### Double underscore methods

# In[36]:


class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Dog("{self.name}", {self.weight})'
    
    def __add__(self, other_dog):
        return [Dog('puppy1', 5), Dog('puppy2', 10)]
        
    def speak(self):
        print('woof')


# In[37]:


dog1  = Dog('rover', 66)
dog2 = Dog('sparky', 15)
puppies = dog1 + dog2
for pup in puppies:
    print(pup.name)


# In[38]:


dog1


# In[39]:


x = [1, 2, 3, 4]


# In[40]:


f'{dog1=}'


# In[41]:


str(dog1)


# In[42]:


x = [1, 2, 3]
x + [4, 5, 6]


# In[43]:


dir(x)


# ### Duck typing
# 
# if it quacks like a duck...

# In[44]:


class Brood:
    def __init__(self, names):
        self.puppies = []
        for name in names:
            self.puppies.append(Dog(name, 5))
            
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.puppies):
            self.n += 1
            return self.puppies[self.n-1]
        else:
            raise StopIteration
            
        
    
    


# In[45]:


group = Brood(['alice', 'bob', 'carol', 'dave'])


# In[46]:


for puppy in group:
    print(puppy.name)


# ### Inheritance

# In[47]:


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(height=side_length, width=side_length)

class Cube(Square):
    def __init__(self, side_length):
        super().__init__(side_length=side_length)
        self.depth = side_length
    
    def volume(self):
        return self.area() * self.depth
    


# In[48]:


obj = Cube(6)
obj.volume()


# In[ ]:





# In[49]:


table = Rectangle(4,20)
table.area()


# In[50]:


another_table = Square(5)


# In[51]:


another_table.area()


# In[52]:


another_table.perimeter()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Summary
# 
# **object** - a data structure that contains some data elements (called *attributes*) and some functions to interact with those data (called *methods*).  this design structure allows us to bundle all the relevant attributes and methods of a particular entity together, rather than storing them in a bunch of disjointed functions/variables.  e.g., `today = date(2021, 8, 24)`, `today` is an object that contains month, day, year, and methods for dealing with that date, like printing it in various formats, asking about the weekday, adding/subtracting, etc.
# 
# **class** - a template for creating objects of a certain type.  All objects of a given type are *instances* of the class.  e.g., the class definition of `date` specifies what kinds of information any given *instance* of date ought to contain (year, month, day), and the methods for interacting with those values.  
# 
# **instance** of a class - a specific object that is a member of a class.  `today` is an instance of the `date` class.  Every instance has its own values for the attributes of a class.  For example, after we define `today = date(2021, 8, 24)` and `new_year = date(2021, 12, 31)`, `today` and `new_year` are both *instances* of the `date` class, so they both have a year, month, and day attribute (and a bunch of associated methods), however the values of those attributes are different, because those objects represent different dates.
# 
# **attributes** - are variables that store the properties of an object instance.  All instances of a class have the same attributes, but different values for those attributes. `today` and `new_year` both have the attributes year, month, and day; however the values of those attributes differ between the two instances, because those objects represent different dates.
# 
# **methods** - are functions that are part of an object, and are typically used to interact with the attributes of the objet somehow (e.g., by printing a nicely formatted date string, given the attributes of a particular date object).  Methods are defined when defining the object class.  
# 
# **constructor** - the `__init__()` method of a class, which is called when we create a new instance of that class, and is responsible for setting all the relevant instance attributes.
# 
# ## Advanced concepts
# 
# **object-oriented programming** - an approach to programming that places a priority on defining and using objects, so as to more effectively compartmentalize data and methods.  Python is a particularly pure case, because *everything* is an object.
# 
# **inheritance** - classes may be defined as specific case (subclass) of some other *parent* class (or super class), and will thus *inherit* the methods and attributes of the parent.  For instance, a `square` class might be a subclass of `rectangle` and might inherit methods such as `get_area()` which returns `self.height * self.width`.  
# 
# **double underscore methods** - in Python, the double underscore methods of a class (such as `__init__`, or `__str__`, or `__add__`, etc.) define what common operations like `str(x)` or `x + y` do for members of that class.  This allows the same surface operations, to do different, class-appropriate things for objects of different types.
# 
# **type** - the *interface* of an object, describing what kinds of things can be done with members of that class, and what those operations do.  For instance `+` does different things to string types than integer types.  `*` is allowed for the combination of string and integer, but not string and float, etc. 
# 
# **duck typing** - the double underscore methods define whether an object can behave as a certain type -- if it quacks like a duck, then its a duck; it doesnt matter whether it was explicitly defined as being an instance of some duck super class.  For instance, an *iterable* type is something that you can iterate over (i.e., do the `for i in x` iteration operation).  In python, any object is iterable so long as it has defined `__iter__` and `__next__` methods.

# In[ ]:




