#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - Final Project/Exam (Fri 6/11 at 11:59 PM)
#     - Practice Final exam now available on datahub (answer key will be posted this weekend)
# 
# Notes:
# - Please fill out your CAPEs (+1% if >=85% response rate) - current: ~30%
# - Coding Labs - nothing to turn in; ~OH; get your questions answered
# - Additional OH will be Wed of Finals Week 
#     - 10 min slot by appt
#     - 9AM-noon; 2-3 PM
#     - details are be pinned on Campuswire 
#     - will use a different zoom link than normal

# **Q&A**
# 
# Q: I’m confused in differences of the project organization (notebook vs module vs script) and how to decide which one to use  
# A: We'll discuss this a bit more today, but here's the simplest approach: 1) Functions/classes get stored in a module (.py) file, 2) Notebook includes brief description of your project and demonstration of how project works (import from module and demonstrate use of code), and 3) script not necessary unless you have some code you want to execute from top to bottom.

# # Advanced Python
# 
# - string formatting (`format`)
# - sets
# - `collections`
# - args & kwargs
# - list comprehensions
# - map
# - APIs
# - overloading operators

# ...or: a day of shortcuts
# 
# Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

# It's hard to search for things you don't know exist.
# 
# Today's goal : let you know these things exist.
# 
# NOT today's goal : teach you all the details.

# You do *not* need to incorporate these into your project, but if they'll help you, go for it!

# In[1]:


import antigravity


# ## String Formatting

# Use the `format` method to manipulate and format strings.

# In[2]:


# class question about including an attribute from a class
myobj = MyClass()

"Hello! My name is {}. My job is {}, and I work on {}".format(myobj.attr_name, job, topic)


# In[2]:


name = "Shannon"
job = "Assistant Teaching Professor"
topic = "Python"

"Hello! My name is {}. My job is {}, and I work on {}".format(name, job, topic)


# ## Sets 

# Sets are a variable type that store **only unique entries**.

# In[3]:


my_set = set([1, 1, 2, 3, 4])
my_set


# Like lists, they are iterable & mutable.

# In[4]:


my_set.add(6)
my_set


# #### Clicker Question #1
# 
# How many values would be in the following set?

# In[5]:


clicker_set = set([1, 1, 2, 2, 3, 4])
clicker_set.add(6)
clicker_set.add(1)
clicker_set


# - A) 0
# - B) 4
# - C) 5
# - D) 6
# - E) ¯\\\_(ツ)\_/¯

# Reminder that if you add a value that is already in the set...the set will not change

# ## Collections

# The `collections` module has a number of useful variable types, with special properties. 

# "Special editions" of collections we've discussed before (lists, tuples, and dictionaries).

# In[6]:


from collections import Counter


# In[7]:


# count how many elements there are in collection
# return values in a dictionary
Counter([1, 0, 1, 2, 1])


# In[8]:


import collections


# In[9]:


collections.Counter([1, 0, 1, 2, 1])


# In[10]:


# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")


# Think back to our encryption scheme! 
# 
# The most common letter in the English language is 'e'.
# 
# If you just move each letter over by 1 position, you can just use a Counter to crack the code.
# 
# Why we moved to a variable encoder!

# ## `any` & `all`

# `any` and `all` evaluate collections for whether elements evaluate as True. 

# In[ ]:


my_bool_list = [True, False, True]


# In[ ]:


any(my_bool_list)


# In[ ]:


all(my_bool_list)


# #### Clicker Question #2
# 
# What would the following return?

# In[ ]:


my_list = [True, True, False, True]
any(my_list)


# - A) `True`
# - B) `False`
# - C) `[True, True, True]`
# - D) `[False]`
# - E) ¯\\\_(ツ)\_/¯

# ## `getattr` & `setattr`

# `getattr` and `setattr` can be used to get and set attributes, respectively. 

# Flexibly return and define instance attributes.

# In[ ]:


class MyClass():
    
    def __init__(self):        
        self.var_a = 'string'
        self.var_b = 12

# create instance 
instance = MyClass()


# In[ ]:


instance.var_a


# In[ ]:


# Get a specified attribute
# define var_a as an input
getattr(instance, 'var_a')


# In[ ]:


# Set a specified attribute
setattr(instance, 'var_b', 13)
print(instance.var_b)


# ## `args` & `kwargs`
# 
# - allow you to pass a variable number of arguments to a function
#     - `*args` - allow any number of extra arguments (including zero)
#     - `**kwargs` - allow any number of *keyword* arguments to be passed (as a dictionary)

# ### `*args`

# In[ ]:


# use *arguments to demonstrate args
def tell_audience(*arguments):
    for arg in arguments:
        print(arg)


# In[ ]:


tell_audience('asdf')


# In[ ]:


tell_audience("Hello!", 
              "My name is Shannon.", 
              "My job is Assistant Teaching Professor.")


# ### `**kwargs`

# In[ ]:


def tell_audience_kwargs(**info):
    print("type: ", type(info), '\n')
    
    for key, value in info.items():
        print("key: ", key)
        print("value: ", value, "\n")


# In[ ]:


tell_audience_kwargs(first='Shannon', 
                     last='Ellis', 
                     email='sellis@ucsd.edu')


# ## List Comprehensions

# List comprehensions allow you to run loops and conditionals, *inside lists*.

# The general format is :
# 
# `[ expression for item in list if conditional ]`
# 

# In[ ]:


# NOT a list comprehension
# how we've been doing it
input_list = [0, 1, 2]
output_list = []

for ind in input_list:
    output_list.append(ind + 1)
    
# look at output
output_list


# In[ ]:


# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]


# In[ ]:


# You can also include conditionals inside a list comprehension
my_list = [1, 2, 3, 4, 5]
my_list2 = [val for val in my_list if val % 2 == 0]


# In[ ]:


print(my_list)
print(my_list2)


# #### Clicker Question #3
# 
# What would the following return?

# In[ ]:


list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1] 
multiplied


# - A) `True`
# - B) `False`
# - C) `[9, 12, 15]`
# - D) `15`
# - E) ¯\\\_(ツ)\_/¯

# Note: there are also tuple & dictionary comprehensions. They're just used less frequently.

# ## Regular Expressions

# Regular expressions allow you to work with **specified patterns in strings**.

# In[ ]:


import re


# In[ ]:


my_string = "If 12 Python programmers try to complete 14 tasks in 16 minutes, why?"


# In[ ]:


# can just search for a letter
re.findall('o', my_string)


# In[ ]:


# but the patterns are where these shine
re.findall('\d\d', my_string)


# ## filter

# `filter` is a function that takes in another function, and a collection object, and **filters the collection with the function**. 

# In[ ]:


def is_bool(val):
    if isinstance(val, bool):
        return True
    else:
        return False


# In[ ]:


#filter?


# In[ ]:


out = []

for val in [1, False, 's', True]:
    out.append(is_bool(val))

out


# In[ ]:


# apply function to every element of list
# function to apply is first input to filter
list(filter(is_bool, [1, False, 's', True]))


# ## Lambda Functions

# Lambda functions are small, anonymous functions. 
# 
# Can define them in line.

# In[ ]:


increment = lambda a: a + 1


# In[ ]:


increment(1)


# In[ ]:


# not a lambda function
def lambda_equivalent(a):
    
    output = a + 1
    
    return output


# In[ ]:


lambda_equivalent(1)


# #### Clicker Question #4
# 
# What would the following return?

# In[ ]:


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list


# - A) `[1, 5, 11, 3]`
# - B) `[1, 3, 5, 11]`
# - C) `[4, 6, 8, 12]`
# - D) `[1, 5, 4, 6, 8, 11, 3, 12]`
# - E) ¯\\\_(ツ)\_/¯

# ## map

# `map` applies a given function to each element in a collection. 

# In[ ]:


# create a function
def double(val):
    return val * 2


# In[ ]:


# map function to each element of list
my_list = [1, 2, 3, 4]
list(map(double, my_list))


# In[ ]:


# Note - we can use lambda functions with map
list(map(lambda x: x *2, my_list))


# ## Conditional Assignment

# You can use a conditional within an assignment, to manipulate what gets assigned given some condition. 

# In[ ]:


# variable assignment
condition = False
my_var = 1 if condition else 2


# In[ ]:


print(my_var)


# ## Unpacking

# You can unpack collection objects with `*`, and key, value pairs with `**`. 

# In[ ]:


def my_func(xx, yy, zz):
    print(xx, yy, zz)


# In[ ]:


# create list
my_list = [1, 2, 3]


# In[ ]:


# this will error
my_func(my_list)


# In[ ]:


# unpack the list
my_func(*my_list)


# In[ ]:


# create dictionary
my_dict = {'xx' : 1, 'yy' : 2, 'zz' : 3}


# In[ ]:


# unpack the dictionary
my_func(**my_dict)


# ## Application Programming Interface

# <div class="alert alert-success">
# An <b>API</b> is a programmatic interface to an application - a software to software interface, or way for programs to talk to other programs. 
# </div>

# If you are pointing and clicking on computer applications, that is _not_ an API.
# 
# If you are writing code to interact with software and get information, that _IS_ an API.

# ### Module APIs

# Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

# ### Web APIs

# APIs are an interface to interact with an application, _designed for programmatic use_ :
# - They allow systematic, controlled access to (for example) an applications database and procedures
# - They can be used to request data and/or to request that the the application perform some procedure

# ### RESTful API
# 
# (Representational State Transfer API) 
# 
# An approach to interact with web addresses

# ## Twitter API

# In[ ]:


# to use this on your computer
# uncomment and run following line
# !pip install tweepy


# Then, follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) for authetication of tweepy with Python.

# In[ ]:


# Accessing Twitter API from Python
#  Note: to run this, you will have to fill in stw.py with your OAuth credentials.
#    You can do that here: https://apps.twitter.com/

# Import tweepy to access API
import tweepy
from tweepy import OAuthHandler

# Import my API credentials
from stw import *

# Twitter API requires Authentification with OAuth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object to access Twitter
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.user.name)
    print(status.text, '\n')


# ## Overloading Operators

# In other words: Nothing in Python is sacred.

# Operators and special operations for objects are defined by double underscore methods, which we can overload to change how the object acts. 

# In[ ]:


class Language():
    
    def __init__(self, name):
        self.name = name.lower()
    
    # Overload what the printed representation of the object as a string
    def __repr__(self):
        return "The programming language " + self.name
    
    # Overload the greater than symbol
    def __gt__(self, other):
        return True if self.name == 'python' else False


# Reminder: "dunder" is how we refer to those double underscore methods

# In[ ]:


python = Language('python')
perl = Language('perl')


# In[ ]:


print(python)


# In[ ]:


python > perl

