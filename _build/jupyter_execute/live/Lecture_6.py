#!/usr/bin/env python
# coding: utf-8

# # functions
# 
# ## why write functions / procedures?
# 
# DRY principle

# In[1]:


name = "Edward vul#$^&%"
title = "associate Prof325Ffessor"
course = "computational so&^%#cial SCiEnce"

# convert it title case
# remove all non-space and non-alphanumeric characters

new = ''
for c in name:
    if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
        new += c
name = new.title()


new = ''
for c in title:
    if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
        new += c
title = new.title()



new = ''
for c in course:
    if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
        new += c
course = new.title()

print(name)
print(title)
print(course)


# In[2]:


name = "Edward vul#$^&%"
title = "associate Prof325Ffessor"
course = "computational so&^%#cial SCiEnce"

list_of_vars = [name, title, course]
for i in range(len(list_of_vars)):
    new = ''
    for c in list_of_vars[i]:
        if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
            new += c
    list_of_vars[i] = new.title()

name, title, course = list_of_vars

print(name)
print(title)
print(course)

ta = "Jiaying *(#$%^*$&^*&^ Xu)"


# In[3]:


name = "Edward vul#$^&%"
title = "associate Prof325Ffessor"
course = "computational so&^%#cial SCiEnce"

def cleanString(string):
    new = ''
    for c in string:
        if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
            new += c
    string = new.title()
    return string

name = cleanString(name)
title = cleanString(title)
course = cleanString(course)


print(name)
print(title)
print(course)

ta = "Jiaying *(#$%^*$&^*&^ Xu)"

ta = cleanString(ta)
print(ta)


# ## function basics
# 
# ### def function():

# In[4]:


def printSignature():
    print("Cheers,")
    print("Edward Vul")
    print("Associate Professor of Psychology")
    print("Director Computational Social Science")


print('first line')

printSignature()

print('Hello')

printSignature()


# ### arguments

# In[5]:


def printSignature(message):
    print(message)
    print("Edward Vul")
    print("Associate Professor of Psychology")
    print("Director Computational Social Science")
    
printSignature("Best,")

printSignature("Cheers,")

printSignature("Adios,")


# In[6]:


def multiply(num1, num2):
    print(num1*num2)
    
multiply(4, 5)
multiply(12, 10)


# In[7]:


multiply(4)


# ### position and keyword

# In[8]:


def exponentiate(base, exponent):
    print(base ** exponent)
    
exponentiate(3, 2)
# base=3
# exponent=2
# print(base ** exponent)
exponentiate(2, 3)
exponentiate(exponent = 2, base = 3)


# ### reading through function calls
# 
# ### return.
# 

# In[9]:


def cleanString(string):
    # remove all non space and non alphabetic characters.
    new = ''
    for c in string:
        if c.lower() in ' abcdefghijklmnopqrstuvwxyz':
            new += c
    return new

new_string = cleanString('HGJSKFGH7&^%&S^%DFasfg')

print(new_string)


# In[10]:


print(new_string)


# - def to define a function()
# - function(argument1, argument2, ...)
# - return X yields X 

# ## function subtleties
# 
# ## variable scope

# In[11]:


a = 3

def add(a,b):
    print(locals())
    print(a+b)

add(4,5)


# In[12]:


a = 3
x = 10

def add(x,b):
    #print(locals())
    print(a+b)

add(4,5)


# In[13]:


a = 3

def add(x,b):
    a = x + b
    #print(locals())
    print(a+b)

add(4,5)
print(a)


# In[14]:


a = 3

def add(x,b):
    print(a)
    a = x + b
    #print(locals())
    print(a+b)

add(4,3)
print(a)


# In[15]:


def add(a,b):
    a = a + b
    print(a+b)

add(4,3)


# ### Local vs global variables
# 
# - access vs assignment vs access and assignment
# 
# - Better just not rely on globals, even though you can access them.
# 
# ### pass by assignment
# 
# - implications for mutable and immutable objects

# In[16]:


a = 12

def fun(x):
    print(x)
    x = 23
    print(x)

fun(a)
print(a)


# In[17]:


a = 12

def fun(x):
    print('inside function x:', x)
    print('inside function id(x):', id(x))
    x = 23
    print('inside function x:', x)
    print('inside function id(x):', id(x))
    

print('outside function a:', a)
print('outside function id(a):', id(a))
fun(a)
print('outside function a:', a)
print('outside function id(a):', id(a))


# In[18]:


a = [1, 2, 3]
b = a
print(a)
print(b)
b.append(4)
print(b)
print(a)
print(id(a))
print(id(b))
b = 'burrito'
print(b)
print(a)
print(id(a))
print(id(b))


# In[19]:


a = [1, 2, 3]

def fun(x):
    print('inside function x : ',  x)
    x.append(4)
    print('inside function x: ',  x)

print('outside function a', a)
fun(a)
print('outside function a', a)


# ## arguments
# 
# 
# ### default values

# In[20]:


def calculate(base, exponent, multiplier, verbose=False):
    #"multiplier * base ** exponent"
    if verbose:
        print(f'calculating {multiplier} * {base}**{exponent}')
    return(multiplier * base ** exponent)

calculate(3, 2, 5)
# we assign base=3, exponent=2, multiplier=5
# default assignment verbose=False


calculate(3, 2, 5, True)
# we assign base=3, exponent=2, multiplier=5, verbose=True
# default assignment does nothing


# ### variable number of arguments

# In[21]:


def addNumbers(*nums):
    print(locals())
    return a+b+sum(nums)+c

addNumbers(1, 2, 3, 4, 56, 6,7, 89,678, 45, 457, 346, 456, 45, 457, 45, 4)


# ### variable number of keyword arguments.

# In[22]:


def allthearguments(required_positional, *args, required_keyword, **kwargs):
    print(locals())
    
allthearguments(1, 2, 3, a=5, b=6, c=7, required_keyword=10)


# ## docstring

# In[23]:


def calculate(base, exponent, multiplier, verbose=False):
    """
    returns multiplier * base ** exponent 
    
    optional verbose argument prints things out as it goes
    """
    if verbose:
        print(f'calculating {multiplier} * {base}**{exponent}')
    return(multiplier * base ** exponent)


# In[24]:


get_ipython().run_line_magic('pinfo', 'allthearguments')


# ## type annotation
# 
# 

# In[25]:


def repeatString(string: str, multiplier: int) -> str:
    """
    returns string*multiplier
    """
    return string * multiplier


# In[26]:


repeatString('a', 4)


# In[27]:


get_ipython().run_line_magic('pinfo', 'repeatString')


# In[28]:


# write a function that returns the range of the list: max(list) - min(list)

def rangeOfList(lst):
    return max(lst) - min(lst)

rangeOfList([5, 20, 5, 7])


# In[ ]:




