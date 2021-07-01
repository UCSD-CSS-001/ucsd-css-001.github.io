#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A4** due tonight
# - **CL7** due Wednesday
# 
# **Notes**
# - Prof Ellis' new OH: 
#     - Mon: 10-11 AM; 2-3 PM
#     - Wed: 10-11 AM
#     - Fri: 2-3 PM
# - Have the option to attend lecture live at 8AM or 11AM (same zoom link)
# - Additional OH and coding lab times added to main canvas page

# **Q&A**
# 
# Q: Is the final exam going to be cumulative? How difficult will it be?  
# A: It will be cumulative, but will focus on the material after the second midterm. Students typically find it more difficult than the first midterm but less difficult than the second. This is b/c there is less code to write on the final overall. We'll discuss details soon.
# 
# Q: What does minimal viable product and modular design mean?  
# A: Minimal viable product means the simplest product that you can make that still works. Making a product that is *simple* without additional features guarantees you have a functioning product. Then, using modular design, were you can add in additional pieces/features (think of each "piece" of your project as a function or class, for example) without breaking the original product, and instead, just incorporating the new piece.
# 
# Q: Would doing a chatbox for a certain topic/person be a good idea?  
# A: Yup! That would work.

# # Modules & Scripts
# 
# - namespaces & scope
# - modules
# - `import`
#     - `from`
#     - `as`

# ## Namespaces & Scope

# <div class="alert alert-success">
# A <b>namespace</b> is a 'place' with a set of names and their corresponding objects.
# </div>

# Each Jupyter Notebook has its own Namespace.
# 
# If you have two notebooks open at the same time, they don't know about eachother or what variables have been created in the other.

# Names that are defined and available in a given namespace are in **scope**.

# That is, the *scope* of an object is where it is available to / from. 

# In[1]:


# see what's stored in global namespace
a = 3
b = 15
get_ipython().run_line_magic('whos', '')


# ## Modules & Packages

# <div class="alert alert-success">
# A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
# </div>

# Modules are stored in Python files (.py). We can import these files into our namespace, to gain access to the module within Python.

# In A3 you had to import the package: `nltk`: 
# 
# - **package** is a whole bunch of modules
# - a **module** stores python (.py) files
# - when imported, we have access to its functionality

# ## `import`

# <div class="alert alert-success">
# <code>import</code> is a keyword to import external code into the local namespace.
# </div>

# Why do it this way (importing modules)? 
# 
# 1. Minimize startup costs
# 2. Functions in different packages could have the same name - break programs

# ### `import` example: math module

# For something not yet in your Namespace...

# In[2]:


# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)


# In[3]:


# Import the math module
import math


# In[4]:


# Check the type of math
type(math)


# In[5]:


# By the way - modules are objects
isinstance(math, object)


# In[6]:


# Using code from our math module
# remember to tab complete or use dir(math)
math.sqrt(9)


# ### `import` example: random module

# In[7]:


import random


# In[8]:


# Random is also a module
type(random)


# In[9]:


# Explore what is available in random
dir(random)


# In[10]:


# working with random
random.


# In[11]:


## access documentation
get_ipython().run_line_magic('pinfo', 'random.choice')


# In[12]:


## access underlying code
get_ipython().run_line_magic('pinfo2', 'random.choice')


# ### `random` Example

# In[13]:


# random.sample() documentation
get_ipython().run_line_magic('pinfo', 'random.sample')


# In[14]:


# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)


# ## Imports: `from` & `as`

# <div class="alert alert-success">
# <code>from</code> and <code>as</code> allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
# </div>

# In[15]:


# Import a specific object from a module
from random import choice


# In[16]:


## do NOT have to type module name 
## using this approach
## to call this
choice(to_choose_from)


# In[17]:


# Import a module with a specific name in our namespace
# used when module names are long
import collections as cols


# In[18]:


## collections is not defined
## this code will fail
collections.


# In[19]:


# this is how you would do it
cols.


# In[20]:


# putting it all together
# Import a specific thing and give it a specific name
from string import punctuation as punc


# #### Clicker Question #1
# 
# Which of the following is NOT a valid Python import statement?
# 
# - A) `import collections as col`
# - B) `from statistics import mean as average`
# - B) `from os import path`
# - D) `from random import choice, choices`
# - E) `import ascii_letters from string`

# #### Clicker Question Answer

# In[21]:


# Check our imports
# import collections as col
# from statistics import mean as average
# from os import path
# from random import choice, choices
import ascii_letters from string


# In[22]:


from string import ascii_letters


# In[23]:


get_ipython().run_line_magic('pinfo', 'ascii_letters')


# In[24]:


ascii_letters


# In[25]:


from string import punctuation


# In[26]:


punctuation


# ## Importing Custom Code I

# Why do this? 
# 
# Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.
# 
# Also, they're not reusable later without copying them into your new notebook. 
# 
# Modules avoid this!

# ## module: `remote.py`
# 
# If you want to practice using import with the `remote` example in lecture, store the code in the next cell in a text file saved as `remote.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[27]:


def my_remote_function(input_1, input_2):
    """A function from far away.
    
    This function returns the sum of the two inputs.
    """
    
    return input_1 + input_2

def choice(list_to_choose_from):
    """Choose and return an item from a list. 
    
    Notes: I am a custom choice function: I am NOT from `random`.
    
    Hint: my favorite is the last list item.
    """
    
    return list_to_choose_from[-1]

class MyNumbers():
    
    kind_of_thing = 'numbers'
    
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        
        return self.num1 + self.num2
    
    def subtract(self):
        
        return self.num2 - self.num1


# In[28]:


# Import some custom code
from remote import my_remote_function


# In[29]:


# Investigate our imported function
get_ipython().run_line_magic('pinfo', 'my_remote_function')


# In[30]:


# Run our function
my_remote_function(2, 1)


# ## Importing Custom Code II

# In[31]:


# Import a class class from an external module
from remote import MyNumbers


# In[32]:


# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)


# In[33]:


# Check 
nums.add()


# In[34]:


# Check the definition of the code we imported
get_ipython().run_line_magic('pinfo2', 'nums.add')


# ## Name Conflicts

# In[35]:


from random import choice


# In[36]:


# choice is currently from random module
get_ipython().run_line_magic('pinfo', 'choice')


# In[37]:


choice([1, 2, 3, 4, 5])


# In[38]:


from remote import choice 


# In[39]:


# now it's from my remote module
get_ipython().run_line_magic('pinfo', 'choice')


# In[40]:


choice([1, 2, 3, 4, 5])


# While you _can_ have functions with the same name in two different places...do your best to avoid this.
# 
# It's Python legal but bad for your nerves.

# ## A note on `*`
# 
# If you see `from module import *` this means to import everything (read as 'from module import everything'). 
# 
# This is generally considered not to be the best, as it is then unclear in your code exactly where the functionality came from.

# In[41]:


# avoid doing this
# unclear in code when used
# where functions came from
from random import *


# In[42]:


# a valid way to import
from random import choice
choice([2,3,4])


# In[43]:


# a valid way to import
import random
random.choice([2,3,4,])


# ## script: `remote_script.py`
# 
# 
# If you want to run your own script example in lecture, store the code in the next cell in a text file saved as `remote_script.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[44]:


from remote import MyNumbers
nums = MyNumbers(2, 3)
print("nums value: ", nums)
print("nums type: ", type(nums))


# In[45]:


# run the script
get_ipython().system('python remote_script.py')


# <h1 align="center">We have finished Python!</h1>
# 
# 

# <h3 align="right">well, kind of.</h3>
