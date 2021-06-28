#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL5** due Wed (11:59 PM)
# - **A3** due 5/10 (Mon of Wk 7)
#     - if you submit it by 5/3 (next Mon; wk 6)
#         - we'll "grade" it & release feedback
#         - this will give you the opportunity to fix mistakes
# 
# Notes:
# - A2 grades & feedback released
# - E1 grading is underway

# # Functions I
# 
# - defining a function
#     - `def`
#     - `return`
# - executing a function
#     - parameters
#     - separate namespace

# ## Functions
# 
# <div class="alert alert-success">
# A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
# </div>

# Copy + Pasting the same/similar bit of code is to be avoided.
# 
# **Loops** were one way to avoid this.
# 
# **Functions** are another!

# ## Modular Programming
# 
# <div class="alert alert-success">
# Modular programming is an approach to programming that focuses on building programs from indendent modules ('pieces'). 
# </div>

# ## Functions for Modular Programming

# - Functions allow us to flexibly re-use pieces of code
# - Each function is independent of every other function, and other pieces of code
# - Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
#     - This allows us to build up arbitrarily complex, well-organized programs

# In[1]:


# you've seen functions before
# here we use the type() function
my_var = [3, 4, 5]
type(my_var)


# In[2]:


# the function len() doesn't depend on type()
# but they can both be used on the same variable
len(my_var)


# ## Function Example I
# 
# When you use `def` you are creating a **user-defined function**.

# In[3]:


# define a function: double_value
# num is a parameter for the function
def double_value(num):

    # do some operation
    doubled = num + num
    
    # return output from function
    return doubled    


# In[4]:


# excecute a function by calling function by name
# adding input within parentheses
double_value(num=6) 


# In[5]:


# equivalent function call
# without specifying parameter
double_value(6) 


# ## Function Example II
# 
# Something _slightly_ more interesting than just adding a value with itself

# In[6]:


def add_two_numbers(num1, num2):
    
    # Do some operations on the input variables
    answer = num1 + num2
    
    # Return the answer
    return answer


# In[7]:


add_two_numbers(1, 2)


# In[8]:


# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)


# ## Function Example III
# 
# We aren't limited to a single operation within a function. We can use multiple operations and all of the concepts we've used previously (including loops and conditionals).

# In[9]:


# determine if a value is even or odd
def even_odd(value): 
    if (value % 2 == 0): 
        out = "even"
    else: 
        out = "odd"
        
    return out


# In[10]:


# Execute our function
even_odd(-1)


# With functions, the logic behind our code no longer requires it to be executed from top to bottom of the notebook.
# 
# The cost of potential confusion is *definitely* offset by the benefits of writing functions and using modular code.

# ## Function Properties

# - Functions are defined using `def` followed by `:`, which opens a code-block that comprises the function
#     - Running code with a `def` block *defines* the function (but does not *execute* it)

# - Functions are *executed* using parentheses - `()`
#     - This is when the code inside a function is actually run

# - Functions have their own namespace
#     - They only have access to variables explicitly passed into them

# - Inside a function, there is code that performs operations on the available variables

# - Functions use the special operator `return` to exit the function, passing out any specified variables

# - When you use a function, you can assign the output (whatever is `return`ed) to a variable

# #### Clicker Question #1

# In[11]:


def remainder(number, divider):
    
    r = number % divider
    
    return r


# Given the function above, what will the code below print out?

# In[12]:


ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

print(ans_1 + ans_2)


# - A) 0
# - B) 2
# - C) 4
# - D) '2r.2 + 1'
# - E) ¯\\\_(ツ)\_/¯

# #### Clicker Question #2
# 
# Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.
# 
# - A) I did it!
# - B) I think I did it.
# - C) I tried but am stuck.
# - D) Super duper lost

# In[13]:


## YOUR CODE HERE
def greet(name):
    output = 'Hello ' + name + '. Good morning!'
    return output


# In[14]:


greet(name='Shannon')


# ## Function Namespace I

# In[15]:


# Remember, you can check defined variables with `%whos`
get_ipython().run_line_magic('whos', '')


# ## Function Namespaces II

# In[16]:


# Return a dictionary containing the current scope's local variables.
# locals?


# In[17]:


def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    local_values = locals()
    
    return local_values


# In[18]:


# Functions don't `see` everything
check_function_namespace(1)


# In[19]:


# Functions don't `see` everything
check_function_namespace(True)


# In[20]:


# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # define a variable within function
    new_var = 5 
    
    # Check what is defined and available inside the function
    local_values = locals()
    
    return local_values


# In[21]:


# returning what each input is storing
check_function_namespace2(1, True)


# ## Function Namespaces III
# 
# Names defined inside a function only exist within the function.

# In[22]:


# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

print(check_function_namespace(my_var))

print(my_var)


# ### Function - Execution Order

# In[23]:


def change_var(my_var):
    my_var = 'I am something else'
    
    return my_var


# In[24]:


# my_var in the global namespace
my_var


# In[25]:


# my_var within the function
change_var(my_var)


# In[26]:


# my_var in the global namespace remains unchanged
my_var 


# In[27]:


print('Outside, before function: \t', my_var)
print(change_var(my_var))
print('Outside, after function: \t', my_var)

