#!/usr/bin/env python
# coding: utf-8

# **Course Anouncements**
# 
# **Due Dates**:
# - **[Mid-Course Survey](https://docs.google.com/forms/d/e/1FAIpQLScE182NPFjsKn78p2MqzsQtxxVgCyw8tPYKToDF4J_4YybmAw/viewform?usp=sf_link)** "due" Mon 5/3 (*optional*; link also on Canvas)
# - **A3** due 5/10 (Mon of Wk 7)
#     - whatever you submit by 5/3 (this Mon; wk 6), we'll "grade" it & release feedback (*optional*)
# 
# **Notes**:
# - **E1** scores havee been released
#     - check score on canvas; feedback on datahub; answer key on website
#     - *regrades* open until Monday at 9AM 
#         - Prof Ellis handles all regrades
#         - She will regrade your entire exam - score can go up, down, or stay the same
# - **E2** is Monday of wk 7 (just an FYI)

# **Q&A**
# 
# Q: I'm still confused why `lowest = None` in our `sort_array`. Doesn't that mess up the loop?  
# A: Remember that `lowest = None` happens *before* the loop, so `lowest = None` the first time through the loop. Try stepping through that example with a short list going through each iteration in your head/on paper. Then, try to do it without the `lowest = None` in the code. If still uncertain, we can discuss in OH!
# 
# Q: Since there are numbers associated with the letters and the emojis you said last time are the same as well, would that mean things like emojis can also be sorted that way?  
# A: Yup! Try this out: `ord('😃')`
# 
# Q: In the sort_array loop, how is the variable lowest=None changed to lowest=item? I thought these were immutable.  
# A: Great question! They *are* immutable, which means *part* of the variable cannot be changed. However, you *can* overwrite what's stored in the variable by assigning a new value to the variable. That's what's happening here.

# # Functions II
# 
# - more on user-defined functions
#     - default values
# - methods
#     - string, list, & dictionary
#     - in place vs not in place
#     - relationship to functions

# #### Clicker Question #1
# 
# What will the following code snippet print?

# In[1]:


def my_func(my_dictionary):
    
    output = []

    for item in my_dictionary:
        value = my_dictionary[item]
        output.append(value) #append method adds an item to end of a list
    
    return output

# create dictionary and execute function
dictionary = {'first' : 1, 'second' : 2, 'third' : 3}
out = my_func(dictionary)

print(out)


# - A) ['first', 'second', 'third'] 
# - B) {1, 2, 3}
# - C) ['first', 1, 'second', 2, 'third', 3] 
# - D) [1, 2, 3] 
# - E) None

# ## Default Values

# <div class="alert alert-success">
# Function parameters can also take <b>default values</b>. This makes some parameters optional, as they take a default value if not otherwise specified.
# </div>

# #### Default Value Functions
# 
# Specify a default value in a function by doing an assignment within the function definition.

# In[2]:


# Create a function, that has a default values for a parameter
def exponentiate(number, exponent=2):  
    return number ** exponent


# In[3]:


# Use the function, using default value
exponentiate(3)


# In[4]:


# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)


# In[5]:


# you can always state this explicitly
exponentiate(number=2, exponent=3)


# ## Positional vs. Keyword Arguments

# <div class="alert alert-success">
# Arguments to a function can be indicated by either position or keyword.
# </div>

# In[6]:


# Positional arguments use the position to infer which argument each value relates to
exponentiate(2, 3)


# In[7]:


# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number=2, exponent=3)


# In[8]:


# discouraging flipping the order of parameters
# even if python allows it
# avoids confusion for the humans
exponentiate(exponent=3, number=2)


# In[9]:


# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number=2, 3)


# Reminder, setting a default value for parameters is allowed during function *definition*.
# 
# (This may look like what we did above, but here we are including a default value for one parameter during function definition. During function *execution*, you can't mix and match using positional vs. keywords)

# In[10]:


def exponentiate(number, exponent=2):    
    return number ** exponent


# #### Clicker Question #2
# 
# What will the following code snippet print?

# In[11]:


def exponentiate(number, exponent = 2):    
    return number ** exponent

# avoid doing this
exponentiate(exponent=3, number=2)

# keep same order
exponentiate(number=2, exponent=3)


# - A) 8
# - B) 9
# - C) SyntaxError
# - D) None
# 

# Note: when using Keyword arguments position/order no longer matters

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

# In[12]:


# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# The method `append()` is called directly on the list `my_list`

# In[13]:


# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')


# In[14]:


# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()


# In[15]:


# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()


# ## String Methods
# 
# There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.

# In[16]:


# Make a string all lower case
'aBcDE'.lower()


# In[17]:


# Make a string all upper case
'aBc'.upper()


# In[18]:


# Capitalize a string
'python is great'.capitalize()


# In[19]:


# Find the index of where a string starts 
'Hello, my name is'.find('name')


# #### Clicker Question #3
# 
# What will the following code snippet print out?

# In[20]:


inputs = ['fIx', 'tYpiNg', 'lIkE', 'tHiS']
output = ''

for element in inputs:
    output = output + element.lower() + ' '

output.capitalize()


# - A) 'fix typing like this ' 
# - B) ['fix', 'typing', 'like', 'this'] 
# - C) 'Fix typing like this '  
# - D) 'Fix typing like this'  
# - E) 'Fixtypinglikethis'

# ## List Methods
# 
# There are also a bunch of list methods, all described [here](https://www.w3schools.com/python/python_ref_list.asp). You've seen some of these before, but we'll review a few of the most commonly used here.

# In[21]:


get_ipython().run_line_magic('pinfo', 'list.sort')


# In[22]:


# sort sorts integers in numerical orders
ints = [16, 88, 33, 40]
ints.sort()
ints


# In[23]:


ints.sort(reverse=True)
ints


# In[24]:


# append adds to the end of a list
ints.append(2)
ints


# In[25]:


# remove value from list
ints.remove(40)
ints


# In[26]:


get_ipython().run_line_magic('pinfo', 'list.remove')


# In[27]:


# reverse order of list
ints.reverse()
ints


# #### Clicker Question #4
# 
# What will the following code snippet print out?

# In[28]:


list_string = ['a', 'c', 'd', 'b']
list_string.sort()
list_string.reverse()
list_string


# - A) ['a', 'c', 'd', 'b']
# - B) ['a', 'b', 'c', 'd']
# - C) ['d', 'c', 'b', 'a']  
# - D) ['d', 'b', 'a', 'c']  
# - E) ['d', 'a', 'b', 'c']

# ## Dictionary Methods
# 
# As with string and list methods, there are many described [here](https://www.w3schools.com/python/python_ref_dictionary.asp) that are helpful when working with dictionaries.
# 

# In[29]:


car = {
  "brand": "BMW",
  "model": "M5",
  "year": 2019
}

# keys() returns the keys of a dictionary
car.keys()


# In[30]:


# get returns the value of a specified key
mod = car.get('model')

# equivalent
mod2 = car['model']

print(mod)
print(mod2)


# In[31]:


# previously done this by indexing
print(car['model'])


# In[32]:


# update adds a key-value pair
car.update({"color": "Black"})

print(car) 


# #### Clicker Question #5
# 
# Assuming `dictionary` is a dictionary that exists, what would the following accomplish:
# 
# ```python
# 
# dictionary.get('letter')
# 
# ```
# 
# - A) Return the key for the value 'letter' from `dictionary`
# - B) Add the key 'letter' to `dictionary`
# - C) Add the value 'letter' to `dictionary`
# - D) Return the value for the key 'letter' from `dictionary`
# 

# #### Clicker Question #6
# 
# Which method would you use to add a new key-value pair to a dictionary?
# 
# - A) `.append()`
# - B) `.get()`
# - C) `.keys()` 
# - D) `.update()`
# 

# ### Methods: In Place vs Not In Place

# <div class="alert alert-success">
# Some methods update the object directly (in place), whereas others return an updated version of the input. 
# </div>

# #### List methods that are in place

# In[33]:


# Reverse a list
my_list = ['a', 'b', 'c']
my_list.reverse()

print(my_list)


# In[34]:


# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)


# #### Dictionary methods that are not in place

# In[35]:


car


# In[36]:


# Return the keys in the dictionary
out = car.keys() 


# In[37]:


# print keys
print(type(out))
print(out)


# In[38]:


# car has not changed
print(type(car))
print(car)


# In[39]:


# Return the values in the dicionary
car.values()


# ## Finding Methods

# Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.

# In[40]:


# Define a test string
my_string = 'Python'


# In[41]:


# See all the available methods on an object with tab complete
my_string. 


# Using the function `dir()` returns all methods available

# In[42]:


# For our purposes now, you can ignore any leading underscores (these are special methods)
dir(my_string)


# ## Correspondance Between Functions & Methods

# Note that:
# 
# ```python
# my_variable.method_call()
# ```
# 
# acts like:
# 
# ```python
# function_call(my_variable)
# ```
# 
# A function that we can call directly on a variable (a method) acts like a shortcut for passing that variable into a function. 

# ### Method / Function Comparison Example

# In[43]:


my_float = 11.0

# Method call
print(my_float.is_integer())

# Function call
#   Note: `is_integer` is part of the float variable type, which is why we access it from there 
print(float.is_integer(my_float))


# In[44]:


# method documentation
get_ipython().run_line_magic('pinfo', 'float.is_integer')


# In[45]:


# function documentation
get_ipython().run_line_magic('pinfo', 'type')


# #### `is_integer`
# 
# You _could_ write a function to check whether a float was an integer and use it as a function (rather than the method `.is_integer()`) ...and we know how to do that!

# In[46]:


def is_integer(my_float):
    
    if my_float % 1 == 0:
        is_int = True
    else:
        is_int = False
        
    return is_int


# In[47]:


print(my_float)
is_integer(my_float)


# ### Functions: Points of Clarification
# 
# Additional notes included here to clarify points we've already discussed. Not presented in class, but feel free to review and gain additional clarificaiton.
# 
# 1. `def` defines a function
# 2. `function_name()` - parentheses are required to execute a function
# 3. `function_name(input1)` - input parameters are specified within the function parentheses 
# 4. `function_name(input1, input2)` - functions can take multiple parameters as inputs
#     - `input1` and `input2` can then be used within your function when it executes
# 5. To store the output from a function, you'll need a `return` statement

# #### For example....
# 
# If you write a function called `is_odd()` which takes an input `value`, 

# In[48]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer


# to use that function, you would execute `is_odd(value)` ....something like `is_odd(value = 6)`

# In[49]:


out = is_odd(6)
out


# Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.

# In[50]:


def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output
            


# In[51]:


new_function([1,2,3,4])

