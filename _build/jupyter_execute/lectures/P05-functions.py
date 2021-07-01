#!/usr/bin/env python
# coding: utf-8

# # P05: functions
# - **Concepts**: abstraction, functions, scope, mutable/immutable
# - **Python functions**: writing, scope, pass by reference implications
# 
# ## Concepts
# 
# ### Abstraction into procedures
# 
# ### Variable scope in functions
# 
# ## Python functions
# 
# ### reading through function calls

# In[1]:


def print_einstein():
    print("                               mMNM&%w")
    print("                         mkMH$MUMFPM,NM#Z%%")
    print("                     :!.:x )!!X)$MMWWMM$**$$Nx~~`")
    print("                    !<!*R@@MNR$$$B$WWXXtdn.\"?XT!:")
    print("                   :~` tH!~!!MBT5$$$$$$$WRHb!\"! !.")
    print("                    .<.$f <!!HR$$$$$$$$$$$X?`>!)X?~(")
    print("                   ~-!#@\~/!!!@$$$$$$$$$$$R! `<!M>-!%.")
    print("                    .!!\"X  !XXM$$$$$$$$$$$R!! !X!!i\"~ `:")
    print("                   :!t! <: !?X***$$$$$$$***~!  ??>X    `")
    print("                  '  `!~~:  ~x.  !R$$$$* . x   W`   - >")
    print("                        ~! ::\" `L?X#$F.uC\"L\" . $      `n")
    print("                     %   ~<%!.#mT$\"<$k\"$$Q?:xW \"      '")
    print("                      ~   4BhU@$W$?!$$ \"$$WdN\"'.")
    print("                           R$$$$$$* $$k'$$$$$ !&!x")
    print("      Albert               !T$$$$6n'$$$ $$$(T  .?\"")
    print("     Einstein              @!M$$$$ec.\")d$$$$!   `.")
    print("                           !!8$f\"` \"   `^T$!~")
    print("                           !!R$  :xxox..o:d\"")
    print("                            \" #@!$WN@W$$$~\"  \\")
    print("                               \"~R$$$$$$\"     N.")
    print("                    .             \"#\"\"\"\" :X   `Wmu.")
    print("               '<:<!!                  .u$M    $!$$$bou.")
    print("            .:!!!~!!?         .     :ud$$$!   ~@XR$$$$$$$eu.")
    print("           <!!!!RnL`\"% ~\    X~ti   `$RM$R~ :`  #W$$$R$$$T$$$c")
    print("         <!!!!XX?*> ~    .-`  `% XxU@$R~  ~: . ^*$M\"$$B$$$\"$!:Mm")
    print("        m!!!!!M8X!   :`.:L      ~UT?8$F .!-.x!:  \"N `9$$$\":\"$LFDSA")
    print("       HDFB<FLOYDXM  ~:X. `\"X:.   '*$$\" :?ud$RW:~<x %'$$$# $s$EYNRBx")

def print_greeting():
    print("hello there!")
    print("Glad to make your acquaintance.")

def send_pic():
    print("Let me show you a picture of myself (SFW, I promise!)")
    print_einstein()


picture = False
print_greeting()
if picture:
    send_pic()
else:
    print("I will show you a picture anyway, I like it so much:")
    print_einstein()


# ### arguments
# 

# In[2]:


def double(x):
    return x*2

double(5)


# 
# #### position vs keyword
# 
# #### default values
# 
# #### variable arguments

# In[3]:


def everything(*args, **kwargs):
    for arg in args:
        print(arg)
    for k,v in kwargs.items():
        print(f'{k}:{v}')

everything('a', 'abra', [1, 2, 3, ], falafel = 'large', fries = 'small', soda='diet')


# #### required arguments
# 
# ### return
# 
# ### variable scope, call by assignment

# In[4]:


def dostuff(a, b, c):
    a = a + ' addition'  # immutable string, therefore assign, therefore local
    b.append('addition') # mutable list, being mutated.  change is global
    c = c + ['addition'] # mutable list, but being assigned, so change is local.
    print("Inside function: ")
    print(a, b, c)

a = 'string '
b = ['string in list', ]
c = ['string in list', ]

print("Before function call: ")
print(a, b, c)

dostuff(a, b, c)

print("After function call: ")
print(a, b, c)



# Functions I

- defining a function
    - `def`
    - `return`
- executing a function
    - parameters
    - separate namespace


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

# In[5]:


# you've seen functions before
# here we use the type() function
my_var = [3, 4, 5]
type(my_var)


# In[6]:


# the function len() doesn't depend on type()
# but they can both be used on the same variable
len(my_var)


# ## Function Example I
# 
# When you use `def` you are creating a **user-defined function**.

# In[7]:


# define a function: double_value
# num is a parameter for the function
def double_value(num):

    # do some operation
    doubled = num + num

    # return output from function
    return doubled


# In[8]:


# excecute a function by calling function by name
# adding input within parentheses
double_value(num=6)


# In[9]:


# equivalent function call
# without specifying parameter
double_value(6)


# ## Function Example II
# 
# Something _slightly_ more interesting than just adding a value with itself

# In[10]:


def add_two_numbers(num1, num2):

    # Do some operations on the input variables
    answer = num1 + num2

    # Return the answer
    return answer


# In[11]:


add_two_numbers(1, 2)


# In[12]:


# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)


# ## Function Example III
# 
# We aren't limited to a single operation within a function. We can use multiple operations and all of the concepts we've used previously (including loops and conditionals).

# In[13]:


# determine if a value is even or odd
def even_odd(value):
    if (value % 2 == 0):
        out = "even"
    else:
        out = "odd"

    return out


# In[14]:


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

# In[15]:


def remainder(number, divider):

    r = number % divider

    return r


# Given the function above, what will the code below print out?

# In[16]:


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

# In[17]:


## YOUR CODE HERE
def greet(name):
    output = 'Hello ' + name + '. Good morning!'
    return output


# In[18]:


greet(name='Shannon')


# ## Function Namespace I

# In[19]:


# Remember, you can check defined variables with `%whos`
get_ipython().run_line_magic('whos', '')


# ## Function Namespaces II

# In[20]:


# Return a dictionary containing the current scope's local variables.
# locals?


# In[21]:


def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    local_values = locals()

    return local_values


# In[22]:


# Functions don't `see` everything
check_function_namespace(1)


# In[23]:


# Functions don't `see` everything
check_function_namespace(True)


# In[24]:


# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # define a variable within function
    new_var = 5

    # Check what is defined and available inside the function
    local_values = locals()

    return local_values


# In[25]:


# returning what each input is storing
check_function_namespace2(1, True)


# ## Function Namespaces III
# 
# Names defined inside a function only exist within the function.

# In[26]:


# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

print(check_function_namespace(my_var))

print(my_var)


# ### Function - Execution Order

# In[27]:


def change_var(my_var):
    my_var = 'I am something else'

    return my_var


# In[28]:


# my_var in the global namespace
my_var


# In[29]:


# my_var within the function
change_var(my_var)


# In[30]:


# my_var in the global namespace remains unchanged
my_var


# In[31]:


print('Outside, before function: \t', my_var)
print(change_var(my_var))
print('Outside, after function: \t', my_var)


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

# In[32]:


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

# In[33]:


# Create a function, that has a default values for a parameter
def exponentiate(number, exponent=2):
    return number ** exponent


# In[34]:


# Use the function, using default value
exponentiate(3)


# In[35]:


# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)


# In[36]:


# you can always state this explicitly
exponentiate(number=2, exponent=3)


# ## Positional vs. Keyword Arguments

# <div class="alert alert-success">
# Arguments to a function can be indicated by either position or keyword.
# </div>

# In[37]:


# Positional arguments use the position to infer which argument each value relates to
exponentiate(2, 3)


# In[38]:


# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number=2, exponent=3)


# In[39]:


# discouraging flipping the order of parameters
# even if python allows it
# avoids confusion for the humans
exponentiate(exponent=3, number=2)


# In[40]:


# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number=2, 3)


# Reminder, setting a default value for parameters is allowed during function *definition*.
# 
# (This may look like what we did above, but here we are including a default value for one parameter during function definition. During function *execution*, you can't mix and match using positional vs. keywords)

# In[41]:


def exponentiate(number, exponent=2):
    return number ** exponent


# #### Clicker Question #2
# 
# What will the following code snippet print?

# In[42]:


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

# In[43]:


# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# The method `append()` is called directly on the list `my_list`

# In[44]:


# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')


# In[45]:


# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()


# In[46]:


# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()


# ## String Methods
# 
# There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.

# In[47]:


# Make a string all lower case
'aBcDE'.lower()


# In[48]:


# Make a string all upper case
'aBc'.upper()


# In[49]:


# Capitalize a string
'python is great'.capitalize()


# In[50]:


# Find the index of where a string starts
'Hello, my name is'.find('name')


# #### Clicker Question #3
# 
# What will the following code snippet print out?

# In[51]:


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

# In[52]:


get_ipython().run_line_magic('pinfo', 'list.sort')


# In[53]:


# sort sorts integers in numerical orders
ints = [16, 88, 33, 40]
ints.sort()
ints


# In[54]:


ints.sort(reverse=True)
ints


# In[55]:


# append adds to the end of a list
ints.append(2)
ints


# In[56]:


# remove value from list
ints.remove(40)
ints


# In[57]:


get_ipython().run_line_magic('pinfo', 'list.remove')


# In[58]:


# reverse order of list
ints.reverse()
ints


# #### Clicker Question #4
# 
# What will the following code snippet print out?

# In[59]:


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

# In[60]:


car = {
  "brand": "BMW",
  "model": "M5",
  "year": 2019
}

# keys() returns the keys of a dictionary
car.keys()


# In[61]:


# get returns the value of a specified key
mod = car.get('model')

# equivalent
mod2 = car['model']

print(mod)
print(mod2)


# In[62]:


# previously done this by indexing
print(car['model'])


# In[63]:


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

# In[64]:


# Reverse a list
my_list = ['a', 'b', 'c']
my_list.reverse()

print(my_list)


# In[65]:


# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)


# #### Dictionary methods that are not in place

# In[66]:


car


# In[67]:


# Return the keys in the dictionary
out = car.keys()


# In[68]:


# print keys
print(type(out))
print(out)


# In[69]:


# car has not changed
print(type(car))
print(car)


# In[70]:


# Return the values in the dicionary
car.values()


# ## Finding Methods

# Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.

# In[71]:


# Define a test string
my_string = 'Python'


# In[72]:


# See all the available methods on an object with tab complete
my_string.


# Using the function `dir()` returns all methods available

# In[73]:


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

# In[74]:


my_float = 11.0

# Method call
print(my_float.is_integer())

# Function call
#   Note: `is_integer` is part of the float variable type, which is why we access it from there
print(float.is_integer(my_float))


# In[75]:


# method documentation
get_ipython().run_line_magic('pinfo', 'float.is_integer')


# In[76]:


# function documentation
get_ipython().run_line_magic('pinfo', 'type')


# #### `is_integer`
# 
# You _could_ write a function to check whether a float was an integer and use it as a function (rather than the method `.is_integer()`) ...and we know how to do that!

# In[77]:


def is_integer(my_float):

    if my_float % 1 == 0:
        is_int = True
    else:
        is_int = False

    return is_int


# In[78]:


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

# In[79]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False

    return answer


# to use that function, you would execute `is_odd(value)` ....something like `is_odd(value = 6)`

# In[80]:


out = is_odd(6)
out


# Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.

# In[81]:


def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output


# In[82]:


new_function([1,2,3,4])

