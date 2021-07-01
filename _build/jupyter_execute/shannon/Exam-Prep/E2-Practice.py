#!/usr/bin/env python
# coding: utf-8

# # Exam #2 Practice Questions
# 
# To practice for the second exam, read through each of these questions and try and answer the question _before_ you run the code.
# 
# Since this is a notebook, you can also then run this code to check what it does. 
# 
# Make sure you understand why each thing does what it does!
# 
# Also, remember that the concepts from Exam #1 are still important. Be sure to quickly review those concepts.

# ## Exam #1 Topics to Review
# 
# - Variables & Data Types
# - Operators
# - Conditionals
# - Loops

# ### Variables & DataTypes
# 
# Types:
# - strings, integers, floats, Booleans, None
# - Collections
#     - Lists
#     - Tuples
#     - Dictionaries
# 
# Concepts:
# - Mutable vs. Immutable
# - Indexing

# ### Operators
# 
# - assignment : `=`
# - math: `+`, `-`, `/`, `*`, `**`, `//`
# - comparison : `==`, `!=`, `<`, `>`, `<=`, `>=`
# - logic: `and`, `or`, `not`
# - identity: `is`, `is not`
# - membership : `in`, `not in`

# ### Conditionals
# 
# - `if`, `elif`, & `else`

# ### Loops
# 
# - loops: `for` and `while`
#     - `continue`, `break`, `pass`

# ## Exam #2: New Topics
# 
# - Functions & Algorithms
# - Errors & Debugging
# - Classes & Obejcts

# ## Functions & Algorithms

# ### Functions 1
# 
# What will the following code print: 
# 
# A) ‘abcde’	B) ‘zzcde’	C) ‘zzzzz’	D) ‘zz’	E) ‘’

# In[1]:


def string_manipulator(string):
    
    output = ''
    
    for char in string:
        if char is 'a' or char is 'b':
            char = 'z'
            output = output + char
    
    return output

variable = 'abcde'
manipulated_string = string_manipulator(variable)
print(manipulated_string)


# ### Functions 2
# 
# What will the following piece of code print out?

# In[2]:


def manipulate_three(num1, num2, num3):

    answer = num1**num2%num3

    return answer

manipulate_three(3, 2, 5)


# ### Functions 3
# 
# What will the following piece of code print out?
# 
# A) 0 | B) 1 | C) 2 | D) 3 | E) 4

# In[3]:


def count_bool(list_of_bools):
    
    counter = 0
    
    for it in list_of_bools:
    
        if isinstance(it, bool):
            counter = counter + 1
    
    return counter

count_bool([True, 3, None, False, False])


# ## Errors & Debugging
# 
# For each of the following, answer:
#     - Why does this raise an error? (You won't have to specify the error type on an exam, but it's good to know.)
#     - How would you fix it?

# ### Errors 1
# 
# A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 

# In[4]:


my_string = "My favourite number is " + 27


# ### Errors 2
# 
# A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 

# In[5]:


print('My favorite number is' + str(3+5)


# ### Errors 3
# 
# A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 

# In[6]:


my_list = [1, 3, max]


# ## More Errors
# 
# Each of the code blocks below have something wrong with them. 
# 
# Identify the error, figure out how you would fix this could to run properly.

# In[7]:


print'5 plus six')


# In[8]:


int('six')


# In[9]:


100/0


# In[10]:


my_list = [4,5,2]
print(my_list[3])


# In[11]:


my_dict = {'this':100, 'that':200}
my_dict['there']


# ## Classes & Objects 

# ### Objects 1
# 
# Given the following object:
# 
# - Identify which parts are a class attribute, an instance attribute, and a method. 

# In[12]:


class Shannon():
    
    current_job = 'instructor'
    
    def __init__(self, current_project):
        self.current_project = current_project
    
    def do_new_thing(self, new_thing):
        self.current_project = new_thing
        print("I have a new project now!")
        
    def print_project(self):
        print("My current project is: ", self.current_project)        


# Using the object from above, what will each of the following code cells (executed in order) do / print out?

# In[13]:


shannon = Shannon('Teaching')


# In[14]:


shannon.print_project()


# In[15]:


shannon.do_new_thing('Research')


# In[16]:


shannon.print_project()


# ### Combining Things: Flow Control with Booleans

# We're going to define a few functions that return booleans. 

# In[17]:


def foo1():
    return True

def foo2():
    return False

def foo3(val):
    result = val > 10
    return result


# For each of the following cells, given the function above, what will they print out?

# In[18]:


result1 = (True and foo1()) or (False or foo2())
print(result1)


# In[19]:


result2 = (False and foo1()) or (True or foo2())
print(result2)


# In[20]:


result3 = (False and foo1()) or (False or foo2()) or (True and foo3(11))
print(result3)


# In[21]:


result4 = (False and foo1()) or (False or foo2()) or (True and foo3(1))
print(result4)

