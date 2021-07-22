#!/usr/bin/env python
# coding: utf-8

# # P06: classes and objects
# 
# - objects
# - `class`
#     - attributes
#     - methods
# - instances
#     - `__init__`

# ## Objects
# 
# <div class="alert alert-success">
# Objects are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
# </div>

# ### Storing Dates (Motivation)

# In[1]:


# A date, stored as a string
date_string = '29/09/1988'
print(date_string)


# In[2]:


# A date, stored as a list of numbers
date_list = ['29', '09', '1988']
date_list


# In[3]:


# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)


# In[4]:


# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary


# Ways to organize data (variables) and functions together.

# ### Example Object: Date

# In[5]:


# Import a date object
from datetime import date


# In[6]:


get_ipython().run_line_magic('pinfo', 'date')


# In[7]:


# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)


# In[8]:


# Check what type of thing `my_date` is
type(my_date)


# ## Accessing Attributes & Methods

# <div class="alert alert-success">
# Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object.
# </div>

# ### Date - Attributes
# 
# Attributes look up & return information about the object.

# **attributes** maintain the object's state, simply returning information about the object to you

# In[9]:


# Get the day attribute
my_date.day


# In[10]:


# Get the month attribute
my_date.month


# In[11]:


# Get the year attribute
my_date.year


# ### Date - Methods
# 
# These are _functions_ that *belong* to and operate on the object directly.

# **methods** modify the object's state

# In[12]:


# Method to return what day of the week the date is
my_date.weekday()


# In[13]:


# Reminder: check documentation with '?'
get_ipython().run_line_magic('pinfo', 'date.weekday')


# It's also possible to carry out operations on multiple date objects.

# In[14]:


# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)


# In[15]:


# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365, "years") #in years


# ### Listing Attributes & Methods : `dir`

# In[16]:


# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.


# In[17]:


## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)


# ### Objects Summary
# 
# - Objects allow for data (attributes) and functions (methods) to be organized together
#     - methods operate on the object type (modify state)
#     - attributes store and return information (data) about the object (maintain state)
# - `dir()` returns methods & attributes for an object
# - Syntax:
#     - `obj.method()`
#     - `obj.attribute`
# - `date` and `datetime` are two types of objects in Python

# ## Classes

# <div class="alert alert-success">
# <b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
# </div>

# Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

# ## Example Class: Dog

# In[18]:


# Define a class with `class`.
# By convention, class definitions use CapWords (Pascal)
class Dog():

    # Class attributes for objects of type Dog
    sound = 'Woof'

    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        return self.sound * n_times


# A reminder:
# - **attributes** maintain the object's state; they lookup information about an object
# - **methods** alter the object's state; they run a function on an object

# **`class`** notes:
# 
# - classes tend to use **CapWords** convention (Pascal Case)
#     - instead of snake_case (functions and variable names)
# - `()` after `Dog` indicate that this is callable
#     - like functions, Classes must be executed before they take effect
# - can define **attributes** & **methods** within `class`
# - `self` is a special parameter for use by an object
#     - refers to the thing (object) itself
# - like functions, a new namespace is created within a Class
# 

# In[19]:


# Initialize a dog object
george = Dog()


# In[20]:


# george, has 'sound' attribute(s) from Dog()
george.sound


# In[21]:


# george, has 'Dog' method(s)
# remember we used `self`
george.speak()


# 

# ### Using our Dog Objects

# In[22]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# In[23]:


# take a look at this
pack_of_dogs


# In[24]:


# take a look at this
type(pack_of_dogs[0])


# In[25]:


for dog in pack_of_dogs:
    print(dog.speak())


# ## Instances & self

# <div class="alert alert-success">
# An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance.
# </div>

# In[26]:


# Initialize a dog object
george = Dog()


# From our example above:
# 
# - Dog is the Class we created
# - `george` was an _instance_ of that class
# - self just refers to whatever the _current_ instance is

# 
# ## Instance Attributes
# 
# An instance attribute specific to the instance we're on. This allows different instances of the same class to be unique (have different values stored in attributes and use those in methods).

# In[27]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# This creates four different `Dog` type objects and stores them in a list. But, up until now...every `Dog` was pretty much the same.

# <div class="alert alert-success">
# Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes.
# </div>
# 
# 
# ## Example Class: Dog Revisited
# 
# - Two trailing underscores (a `dunder`, or double underscore) is used to indicate something Python recognizes and knows what to do every time it sees it.
# - Here, we use `__init__` to execute the code within it every time you initialize an object.

# In[28]:


class Dog():

    # Class attributes for Dogs
    sound = 'Woof'

    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name

    def speak(self, n_times=2):
        return self.sound * n_times


# In[29]:


# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name='Gary')


# In[30]:


# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute


# In[31]:


# Check gary's methods
gary.speak()


# 
# ## Class example: Cat

# In[32]:


# Define a class 'Cat'
class Cat():

    sound = "Meow"

    def __init__(self, name):
        self.name = name

    def speak(self, n_times=2):
        return self.sound * n_times


# ## Instances Examples

# In[33]:


# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'),
        Cat('Picatso'), Dog('Ruffius')]


# In[34]:


for pet in pets:
    print(pet.name, ' says:')
    print(pet.speak())


# 
# ### Classes Review
# 
# - `class` creates a new class type
#     - names tend to use CapWords case
#     - can have attributes (including instance attributes) and methods
#         - `obj.attribute` accesses data stored in attribute
#         - `obj.method()` carries out code defined within method
# 

# - instance attributes defined with `__init__`
#     - `__init__` is a reserved method in Python
#     - This "binds the attributes with the given arguments"
#     - `self` refers to current instance

# - to create an object (instance) of a specified class type (`ClassType`):
#     - `object_name = ClassType(input1, input2)`
#     - `self` is not given an input when creating an object of a specified class

# ## Everything in Python is an Object!

# ### Data variables are objects

# In[35]:


print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))


# ### Functions are objects

# In[36]:


print(isinstance(sum, object))
print(isinstance(max, object))


# In[37]:


# Custom function are also objects
def my_function():
    print('yay Python!')

isinstance(my_function, object)


# ### Class definitions & instances are objects

# In[38]:


class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))


# ## Object-Oriented Programming

# <div class="alert alert-success">
# <b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge.
# </div>
# 
# 
# 
# ## Methods

# <div class="alert alert-success">
# <b>Methods</b> are functions that are defined and called directly on an object.
# </div>
# 
# <div class="alert alert-success">
# For our purposes, <b>objects</b> are any data variable.
# </div>

# ### Method Examples
# 
# A method is a function applied directly to the object you call it on.

# General form of a method:
# 
# ```python
# object.method()
# ```

# In other words: methods "belong to" an object.

# In[39]:


# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# The method `append()` is called directly on the list `my_list`

# In[40]:


# append is a method for lists
# this will error with a string
my_string = 'css1'
my_string.append('!')


# In[41]:


# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()


# In[42]:


# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()


# 
