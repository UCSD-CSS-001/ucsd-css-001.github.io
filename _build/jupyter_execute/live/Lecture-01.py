#!/usr/bin/env python
# coding: utf-8

# # CSS1 Lecture 1

# ## Computational Social Science
# 
# - Who am I?
# 
# - What is CSS?

# ## Computer Programming
# 
# - what is it?
# 
# - why does it require practice?
# 
# - why is it frustrating?
# 
# - lots of variability in starting conditions

# ## This class
# 
# - goals, and why this class may not be different from other social science classes.
# 
# - syllabus
# 
# - class website
# 
# - campuswire
# 
# - datahub

# ## Our environment
# 
# ### Datahub
# 
# - logging in and launching image
# 
# - navigating your files
# 
# - creating notebooks
# 
# - fetching and submitting assignments
# 
# ### Jupyter notebooks.
# 
# - cells and cell types
# 
# - markdown
# 
# - kernel (will revisit)

# ## Python
# 
# ### Comments
# this is some text
# In[1]:


# this is a comment
# so I can write whatever in a comment, and it will be ignored

# assigning the value 4 to x
x = 4
# printing x
print(x)


# In[2]:


# print the number 5


# ### Arithmetic operators
# 
# - python as calculator

# In[3]:


4 + 4


# In[4]:


5 - 3


# In[5]:


5*3


# In[6]:


5/3


# In[7]:


3**2


# In[8]:


-4


# In[9]:


(4 + 5)*3


# In[10]:


4 + 5*3


# In[11]:


4 + 


# In[12]:


5 + 'abracadabra'


# In[13]:


5 * (4+3


# In[14]:


'computational' + ' social science'


# ### Errors and Exceptions

# ### Parsing Expressions and syntax
# 
# #### Operators

# In[15]:


456.5


# In[16]:


'word and other string contents'


# In[17]:


True


# In[18]:


False


# In[19]:


'word' * 3


# In[20]:


('word' + 'boo') * 3

('word' + 'boo') * 3

A * B

A :  ('word' + 'boo') ->'wordboo'
B:  3

A:  C + D -> 'wordboo'
C: 'word'
D: 'boo'
# #### Literals
# 
# - number (ignoring int vs float for now)
# 
# - string
# 
# - boolean

# #### Names

# In[21]:


y


# In[22]:


x


# In[ ]:





# #### Calling Functions

# In[23]:


print(x+5, 'second argument', 5)


# In[24]:


x(3)


# In[ ]:





# #### White space

# In[25]:


print(34)
    print(45)


# #### Summary:
# 
# - interpreter must parse your instructions into a hierarchy of expressions, and then evaluates them from the inside out.

# ### Types
# 
# 
# #### Looks can be deceiving, check!

# In[26]:


print(4)
print(4.0)
print('4')


# In[27]:


print('4' + '4')
print(4 + 4)
print(4 * 4)
print('4' * 4)
print('4' * 4.0)


# - `type()`

# In[28]:


print(type(4))
print(type(4.0))
print(type('4'))


# - `isinstance()`

# In[29]:


x = 45

isinstance(x, int)


# In[30]:


type(x) == int


# #### Type casting

# In[31]:


type(4)


# In[32]:


type(4.0)


# In[33]:


int(4.0)


# In[34]:


int('34')


# In[35]:


int('thirty four')


# In[36]:


str(45)


# In[37]:


float(4)


# In[38]:


str(4.2454574567)


# In[39]:


int('4356.4')


# ### Variables, and memory state

# In[40]:


variable = (54 + 27*3 )/2
string_variable = 'ed made a string'


# In[41]:


get_ipython().run_line_magic('whos', '')


# In[42]:


print(variable)


# In[43]:


radius = 3
print(radius**2 * 3.14159)
print(radius*2 * 3.14159)


# In[44]:


area = radius**2 * 3.14159
circumference = radius*2 * 3.14159


# #### Values
# 
# - basics
# 
# - using variables
# 
# - naming things

# In[45]:


tw346457_4543 = 5


# In[46]:


for = 5


# In[47]:


# print = 5


# In[48]:


get_ipython().run_line_magic('whos', '')


# #### Order of execution and reading code.

# In[49]:


x = 4
# {x: 4}
y = x + 3
# {x: 4, y: 7}
x = 5
# {x: 5, y: 7}
z = x + 2
# {x: 5, y: 7, z: 7}
print(x, y, z)


# In[50]:


w = x+5
print(w)


# In[51]:


x = 100


# #### Notebooks, cells, and memory state
# 
# #### Print debugging
# 
# ### Operators
# 
# #### Arithmetic
# 
# #### Logical
# 
# #### Assignment
# 
# #### Precedence
# 
# #### Overloading

# In[ ]:




