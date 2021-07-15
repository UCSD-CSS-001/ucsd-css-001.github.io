#!/usr/bin/env python
# coding: utf-8

# # P06: functions
# - **Concepts**: abstraction, functions, scope, mutable/immutable
# - **Python functions**: writing, scope, pass by reference implications
# 
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

# 

# ## Function Namespace I

# In[11]:


# Remember, you can check defined variables with `%whos`
get_ipython().run_line_magic('whos', '')


# ## Function Namespaces II

# In[12]:


# Return a dictionary containing the current scope's local variables.
# locals?


# In[13]:


def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    local_values = locals()

    return local_values


# In[14]:


# Functions don't `see` everything
check_function_namespace(1)


# In[15]:


# Functions don't `see` everything
check_function_namespace(True)


# In[16]:


# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # define a variable within function
    new_var = 5

    # Check what is defined and available inside the function
    local_values = locals()

    return local_values


# In[17]:


# returning what each input is storing
check_function_namespace2(1, True)


# ## Function Namespaces III
# 
# Names defined inside a function only exist within the function.

# In[18]:


# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

print(check_function_namespace(my_var))

print(my_var)


# ### Function - Execution Order

# In[19]:


def change_var(my_var):
    my_var = 'I am something else'

    return my_var


# In[20]:


# my_var in the global namespace
my_var


# In[21]:


# my_var within the function
change_var(my_var)


# In[22]:


# my_var in the global namespace remains unchanged
my_var


# In[23]:


print('Outside, before function: \t', my_var)
print(change_var(my_var))
print('Outside, after function: \t', my_var)


# ## pass by assignment
# 
# Variables in python are passed to functions by *assignment*.
# 
# Recall that we can assign two names to the same object:

# In[24]:


a = 'hello'
b = a
print(id(a))
print(id(b))


# when we pass something to a function, we are effectively assigning a new (local) name to that same object.

# In[25]:


def func(x):
    print(id(x))
a = "hello"
print(id(a))
func(a)


# This is nice, because we don't have to allocate more memory to store a *copy* of that object when we pass it into a function.  However, weird things might happen, depending on what we do to that object.
# 

# In[26]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x = 'boo'
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = "hello"
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))


# So what happened here is that `x` inside the function started off pointing to the same object as `a` globally, but then, when we reassigned a new string to `x`, these two variables pointed to different objects, and the local changes to `x` did not alter the object referred to by the global name `a`.
# 
# This happens because we *reasigned* a value to `x`.  Some objects we can alter in place, and as a consequence, local changes will also carry over to the global variable.
# 
# 

# In[27]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x.append('boo')
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = ["hello"]
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))


# Here, we used a list variable, which is *mutable*, and we called a method of that object that mutates that variable in place.  The consequence is that we changed the object, that the global and local variables pointed to, and the changes we made inside the function persisted outside the function.
# 
# If we instead changed the variable inside the function via reassignment, then those changes would stay local.  (This is a case in which `x += [a]` behaves differently from `x = x + [a]` because the `+=` operator uses an inplace method to append).

# In[28]:


def func(x):
    print('enter function')
    print('    x:', x)
    print('    id(x)', id(x))
    x = x + ['boo']
    print('    x:', x)
    print('    id(x)', id(x))
    print('exit function')

a = ["hello"]
print('a:', a)
print('id of a globally', id(a))
func(a)
print('a:', a)
print('id of a globally', id(a))


# 
# # Functions II
# 
# - more on user-defined functions
#     - default values

# 
# ## Default Values

# <div class="alert alert-success">
# Function parameters can also take <b>default values</b>. This makes some parameters optional, as they take a default value if not otherwise specified.
# </div>

# #### Default Value Functions
# 
# Specify a default value in a function by doing an assignment within the function definition.

# In[29]:


# Create a function, that has a default values for a parameter
def exponentiate(number, exponent=2):
    return number ** exponent


# In[30]:


# Use the function, using default value
exponentiate(3)


# In[31]:


# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)


# In[32]:


# you can always state this explicitly
exponentiate(number=2, exponent=3)


# ## Positional vs. Keyword Arguments

# <div class="alert alert-success">
# Arguments to a function can be indicated by either position or keyword.
# </div>

# In[33]:


# Positional arguments use the position to infer which argument each value relates to
exponentiate(2, 3)


# In[34]:


# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number=2, exponent=3)


# In[35]:


# discouraging flipping the order of parameters
# even if python allows it
# avoids confusion for the humans
exponentiate(exponent=3, number=2)


# In[36]:


# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number=2, 3)


# Reminder, setting a default value for parameters is allowed during function *definition*.
# 
# (This may look like what we did above, but here we are including a default value for one parameter during function definition. During function *execution*, you can't mix and match using positional vs. keywords)

# In[37]:


def exponentiate(number, exponent=2):
    return number ** exponent


# ## Variable arguments
# 
# You can specify a *variable* number of positional arguments to a function with the special `*` prefix:
# 
# the function definition `def func(a, b, *vars)` will assign the first (positional) argument to a, the second to b, and all the rest will be elements of the tuple `vars`.
# 

# In[38]:


def myfunction(a, b, *vars):
    print('a', a)
    print('b', b)
    print('vars', vars)

myfunction(1, 2)

myfunction(1, 2, 'something else')

myfunction(1, 2, 3, 4, 'five!')


# You can also capture an arbitrary number of *keyword* arguments with the special prefix `**`.

# In[39]:


def myfunction(a, b, **kwargs):
    print('a', a)
    print('b', b)
    print('kwargs', kwargs)

myfunction(1, 2)

myfunction(1, 2, x=4, y=5, z=6)

# **kwargs does not capture positional arguments!
myfunction(1, 2, 3)


# The catch-all function definition is (but you should rarely use this... better to have well defined functions with a specific *signature*.

# In[40]:


def myfunction(*args, **kwargs):
    print('args', args)
    print('kwargs',kwargs)


print('\nmyfunction()')
myfunction()

print('\nmyfunction(1, 2, x=4, y=5, z=6)')
myfunction(1, 2, x=4, y=5, z=6)

print('\nmyfunction(1, 2, 3)')
myfunction(1, 2, 3)

print('\nmyfunction(1, 2, 3, x=4, y=5, z=6)')
myfunction(1, 2, 3, x=4, y=5, z=6)


# Note that this definition captures all the positional arguments first, then captures the remaining keyword arguments.  For this reason there may be no positional arguments after a keyword argument.

# In[41]:


myfunction(1, 2, 3, x=4, y=5, z=6, 7)


# ## Function signatures and type annotation
# 
# Although it is possible to define all functions as a catchall function: `def f(*args, **kwargs):` that would be terrible in practice, because then it is nearly impossible to figure out what kind of input the function expects.  Consequently you ought to define functions in the most restrictive manner possible.  If you expect one argument, define the function accordingly.
# 
# In Python you can also add type **annotations** to your function definitions.  These are not used directly by the python interpreter, but are often used by the IDE to help you write code.  This is also good practice as it makes it clear what kind of arguments your function expects and returns.
# 

# In[42]:


def transformString(string: str) -> str:
    return string.lower()


# 
# ## Functions: Points of Clarification
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

# In[43]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False

    return answer


# to use that function, you would execute `is_odd(value)` ....something like `is_odd(value = 6)`

# In[44]:


out = is_odd(6)
out


# Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.

# In[45]:


def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output


# In[46]:


new_function([1,2,3,4])

