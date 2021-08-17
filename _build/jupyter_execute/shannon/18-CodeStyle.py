#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL8** due Wednesday
# - **A5** due next Monday (5/31)

# **Q&A**
# 
# Q: I think I am still partially confused about how pytest finds our unit tests and performs its functions.  
# A: `pytest` "looks" for functions that start with `test_`, executes them, and then gives you a readout as to whether or not they passed silently or failed (did not pass silently)
# 
# Q: How often should we be writing tests in our code?  
# A: Ideally, every "piece" (function, class method) of your code should be tested. For the final project, however, the requirement is that you have at least 3 test functions, which test the functionality of the three new/unique required functions/methods for the project.
# 
# Q: I haven't looked much into the final project grading criteria, but does the info on the course website cover all the requirements for the coding project? I ask this because a lot of things have been mentioned in class.  
# A: Yes! https://cogs18.github.io/projects/overview.html (with a FAQ also available: https://cogs18.github.io/projects/faq.html)
# 

# # Code Style
# 
# - PEP8
# - spacing
# - line length
# - comments

# Or: How to be Pythonic

# Reasons to be Pythonic:
# - user friendly for humans
# - extra work up-front on the developers (pays off on the long run)
# - best to practice this early on (I promise!)

# ## Style Guides

# <div class="alert alert-success">
# Coding style refers to a set of conventions for how to write good code. 
# </div>

# Consistency is the goal. Rules help us achieve consistency.

# Much of this will apply to other programming languages, so it's good to learn...regardless of language.
# 
# Some of these Code Style notes will be more specific to Python, however.

# ## The Zen of Python

# In[1]:


import this


# ### Program Errors vs. Stylistic Issues
# 
# - Programmatic Error: something that breaks the code
# - Stylistic Issue: something that doesn't break the code, but is considered bad style - makes your code harder to understand

# ## Picking a Style Guide
# 
# - Code style is (at least partly) subjective
# - Consistency is key. It's easier to recognize & read consistent style

# ## Python Enhancement Proposals (PEPs)

# <div class="alert alert-success">
# Python PEPs are proposals for how something should be / work in the Python programming language. 
# </div>

# These are written by the people responsible for the Python Programming language.

# PEP are voted on before incorporation.

# ## PEP8

# <div class="alert alert-info">
# <b><a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a></b> is an accepted proposal that outlines the style guide for Python.
# </div>

# Defines the style guide for Pythonistas (people who code in Python).

# ## General Concepts

# - Be Explicit & Clear
#     - Prioritize Readability over 'Cleverness'
# - There should be specific, standard ways to do things
#     - Use them
# - Coding Style are guidelines, designed to help the code
#     - They are not laws

# ## Specific Guidelines - Structure
# 
# - blank lines
# - indentaion
# - spacing 
# - length
# - imports

# ### Blank Lines
# 
# - Use 2 blank lines between functions & classes, and 1 between methods
# - Use 1 blank line between segments to indicate logical structure

# This allows you to - at a glance - identify what pieces of code are there.

# In[2]:


# Badness
def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output


# In[3]:


my_func()


# In[4]:


# Goodness
def my_func():
    
    my_nums = '123'
    output = ''
    
    for num in my_nums: 
        output += str(int(num) + 1)
    
    return output


# Note that documentation here is missing (as are comments). This is to highlight the spacing. You'll need documentation and comments.
# 
# I promise it's better to comment as you go along rather than coming along after you've written all the code and adding comments.
# 
# Similar to writing: write comments -> write code -> review code & comments

# #### Clicker Question #1
# 
# Which of these is best - A, B, or C?

# In[5]:


# Option A
def squared(input_number):
    val = input_number
    power = 2    
    output = val ** power
    return output


# In[6]:


# Option B
def squared(input_number, power=2):
    
    output = input_number ** power
    
    return output


# In[7]:


# Option C
def squared(input_number):
    
    val = input_number
    power = 2
    
    output = val ** power
    
    return output


# ### Indentation
# 
# Use spaces to indicate indentation levels, with each level defined as 4 spaces. 

# In[8]:


# Badness
if True:
  print('Words.')


# In[9]:


# Goodness
if True:
    print('Words.')


# ### Spacing
# 
# - Put one (and only one) space between each element
# - Index and assignment don't have a space between opening & closing '()' or '[]'

# In[10]:


# Badnesses
my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]


# In[11]:


# Goodnesses
my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]


# #### Clicker Question #2
# 
# Which of the following uses PEP-approved spacing?
# 
# - A) `my_list=[1,2,3,4,5]`
# - B) `my_list = [1,2,3,4,5]`
# - C) `my_list  =  [1, 2, 3, 4, 5]`
# - D) `my_list=[1, 2, 3, 4, 5]`
# - E) `my_list = [1, 2, 3, 4, 5]`

# ### Line Length
# 
# - PEP8 recommends that each line be at most 79 characters long

# Computers used to require this.
# 
# But, super long lines are hard to read at a glance.

# ### One Statement Per Line
# 
# - While you *can* condense multiple statements into one line, you usually shouldn't.

# In[12]:


# Badness
for i in [1, 2, 3]: print(i**2 + i%2)


# In[13]:


# Goodness
for i in [1, 2, 3]:
    print(i**2 + i%2)


# ### Multi-Line

# In[14]:


my_long_list = [1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]


# In[15]:


# Note: you can explicitly indicate a new line with '\'
my_string = 'Python is ' +             'a pretty great language.'


# ### Imports
# 
# - Import one module per line
# - Avoid `*` imports
# - Use the import order: standard library; 3rd party packages; local / custom code

# In[16]:


# Badness
from numpy import *

import os, sys


# In[17]:


# Goodness
import os
import sys

import numpy as np


# Note: If you don't know how to import a local/custom module, figure that out this week in Coding Lab or office hours.

# ## Specific Guidelines - Naming

# ### Valid Names
# 
# - Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

# In[18]:


# Badness
a = 12
b = 24


# In[19]:


# Goodness
n_filters = 12
n_freqs = 24


# Find + Replace also works better when you have specific variable names 

# ### Naming Style
# 
# - CapWords (leading capitals, no separation) for Classes
# - snake_case (all lowercase, underscore separator) for variables, functions, and modules

# In[20]:


# Badness
def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass


# In[21]:


# Goodness
def my_func():
    pass


class MyClass():
    def __init__():
        pass


# Note: snake_case is easier to read than CapWords, so we use snake_case for the things (variables, functions) that we name more frequently.

# #### Clicker Question #3
# 
# If you were reading code and came cross the following, which of the following would you expect to be a class?
# 
# - A) `Phillies_Game`
# - B) `PhilliesGame`
# - C) `phillies_game`
# - D) `philliesgame`
# - E) `PhIlLiEsGaMe`

# #### Clicker Question #4
# 
# If you were reading code and came cross the following, which of the following would you expect to be a function or variable name?
# 
# - A) `Phillies_Game`
# - B) `PhilliesGame`
# - C) `phillies_game`
# - D) `philliesgame`
# - E) `PhIlLiEsGaMe`

# ### Indicating Scope
# 
# - Leading underscores indicate a 'private' attribute or method of the class, meaning it is an internal value, not expected to be accessed by the user.

# In[22]:


class MyClass():
    def __init__():
        self.public = None
        self._private = None


# The leading underscore indicates to the user that this attribute shouldn't be changed/modified by the user.
# 
# `import *` will not import underscored attributes (private attributes).

# ## Specific Guidelines - String Quotes

# In Python, single-quoted strings and double-quoted strings are the same. 
# 
# This PEP does not make a recommendation for this. **Pick a rule and stick to it.** 
# 
# When a string contains single or double quote characters: use the other one to avoid backslashes in the string. It improves readability.
# 
# 

# In[23]:


# Badness
my_string = 'Prof\'s Project'


# In[24]:


# Goodness
my_string = "Prof's Project"


# #### Clicker Question #5
# 
# Which of the following would not cause an error in Python and would store the string *You're so close!*  ?
# 
# - A) `my_string = "You're so close!"`
# - B) `my_string = "You"re so close!"`
# - C) `my_string = 'You''re so close!'`
# - D) `my_string = "You\\'re so close"`
# - E) `my_string = 'You're so close!'`

# In[25]:


# my_string = "You're so close!"
# my_string = "You"re so close!"
# my_string = 'You''re so close!'
# my_string = "You\\'re so close!"
my_string = 'You're so close!'
my_string


# ## Specific Guidelines - Comments

# Out-of-date comments are worse than no comments at all.
# 
# Keep your comments up-to-date.

# #### Block comments
# - apply to some (or all) code that follows them
# - are indented to the same level as that code. 
# - Each line of a block comment starts with a # and a single space

# In[26]:


# Badness
import random

def week_9():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_9()


# In[27]:


# Goodness
def week_9():
    
    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

week_9()


# #### Inline comments
# - to be used sparingly
# - to be separated by at least two spaces from the statement
# - start with a # and a single space

# In[28]:


# Badness
week_9()#words of encouragement


# In[29]:


# Goodness
week_9()  # words of encouragement


# ## Specific Guidelines - Documentation
# 
# - Write a descriptive docstring for all functions & classes

# Note: If you're borrowing functions from an assignment, you should add documentation to these functions.

# Comments within the functions you've borrowed noting that you've borrowed it as well as a general note in your project description will suffice for attribution.
# 
# If you've modified/edited the code from the assignment, state that you modified.

# ## Linters

# <div class="alert alert-success">
# A linter is a tool that analyzes code for both programmatic errors and stylistic issues. 
# </div>

# In[30]:


get_ipython().system('pip install --user pylint')


# `pylint` is available from Anaconda to check this for you. (Not available on datahub.)

# #### Clicker Question #6
# 
# How many PEP8 violations can you find in this code?

# In[31]:


def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq


# - spacing in the list
# - function name capitatlization (should be sanke case)
# - indentation errors
# - not indenting the conditional (single line issue)
# - variable name ambiguous

# - A) None
# - B) 1 or 2 
# - C) 3 or 4 
# - D) 5 or 6
# - E) 7 or more

# ### list here
# 

# In[32]:


# Let's fix this code
def divide_list(input_num):
    
    my_list = [0, 1, 2, 3]
    
    if 1 in my_list: 
        ind = 1
    else:
        ind = 0
    
    output_list = []
    for val in my_list [ind:]:
        output_list.append(input_num/val)
    
    return output_list


# In[33]:


# check using pylint
get_ipython().system('pylint linter_example.py')
