#!/usr/bin/env python
# coding: utf-8

# # Let's put the "fun" in functions! 🕺 💃

# ## Today's lecture
# 
# 1. Why we need functions
# 2. What is a function
# 3. How to **construct** a function in python
# 4. How to **call** a function in python
# 5. Extending function definitions: how to make your functions lit 🔥
# 6. Function danger zone: passing by assignment

# # Why we need functions
# 
# 1. To avoid repeating ourselves
# 2. To reduce clutter (clutter makes errors!)

# In[1]:


# This code is super repetitive! 
# Repetitive code takes longer to write, is confusing, and increases your odds of making mistakes along the way


name = "Edward vul#$^&%"
title = "associate Prof325%.6essor"
course = "computational so&^%#cial SCiEnce"


# The below removes all non-space and non-alphanumeric characters from name, title, and course
# Then it converts name, title, and course to "title case"

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


# # What is a function?
# 
# A function solves the problems above by isolating code that performs a particular task. It's like the Container Store for your code. 
# 
# Functions are used to solve problems in virtually all coding languages. Though their syntax differs across languages, they all have most of the same ingredients and are there for the same reasons: to simplify and organize.
# 
# NOTE: you don't need to understand everything happening below (at first), as long as you appreciate why these functions are improving the code above.

# In[2]:


# This code does the exact same thing as the repetitive code above. But it's much easier to understand!

name = "Edward vul#$^&%"
title = "associate Prof325%.6essor"
course = "computational so&^%#cial SCiEnce"

# This is our new function!
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


# 
# 
# ----------------------------------------------------------------------------------------------------------------------
# 
# 

# # How to construct a function in python

# ## Recipe for a python function
# 
# **Ingredients**
# 
# - `def` tells python that you're declaring a function (it's short for "define")
# - `my_function` or some other **name**: that's how the rest of your code will "call" the function. NOTE: there's a lot more to say about naming but your function name should say exactly what your function *does*. The python style guide recommends underscores and lowercase.
# - `()` and `:` at the end of the function name: the parentheses `()` are where you declare any *parameters* your function needs (more on this later) and the colon `:` is similar to when we use it in for loops. It tells python that everything after that is part of your function.
# - `return`: this is where your function gives you back the thing it has organized for you. NOTE: not all functions have a `return` (it's not required like the colon `:`), but in practice, most functions will return something.

# In[3]:


# Here's an example using all the ingredients above
# This function returns the string "Hello world"

def get_hello_world_string():
    my_str = "Hello, world"
    return my_str

print(get_hello_world_string())


# In[4]:


# When I call the function above, I get back the string "Hello, world"
foo = get_hello_world_string()

print(foo)
print(type(foo))
foo = foo.replace('H', 'y')
print(foo)


# **Here's a more complicated example of life in Function Land.**
# 
# Instead of just returning a string, the function below reads in a series of data files from an online experiment. It processes that data, removes stuff it doesn't need, and saves the data to a dictionary.
# The function returns the dictionary with all the experimental data in it.
# 
# NOTE: you don't need to understand what's happening below, this is just to illustrate what a function like `get_hello_world_string` above looks like in more realistic settings. 
# 
# Here, you can see all the same ingredients as in the example above, just with more additional seasoning (incl. familiar characters like `for` loops and `split`)

# In[5]:


def get_data():
    data_path = "rps/data" # path to data files
    files = [f for f in listdir(data_path) if f.endswith(".json")]
    files.sort()
    # read JSON file contents and add data to all_data dict
    all_data = dict()
    for f in files:
        with io.open(join(data_path, f), "r", encoding = "utf-8", errors = "ignore") as readfile:
            f_split = f.split("_")
            client_id = f_split[0]
            if client_id[-4:] in ["f99a"]:
                continue
            trial = f_split[1].split(".")[0]
            content = readfile.read()
            parsed_data = json.loads(content)
            all_data["client_" + client_id]["trial_" + trial] = parsed_data

    return all_data


# ## Adding parameters to your functions
# 
# Often, we use functions to manipulate variables like dictionaries that exist *outside* the function. Or, we want to be able to use the function in a few different ways to avoid writing repetitive (but slightly different) code. 
# 
# For this, we need **parameters** in our functions. A parameter is a variable you "pass into" your function to allow your function to "access" it during its execution. In other words, it's an object or a piece of information your function needs in order to do its job.
# 
# In python functions, you declare your parameters inside the parentheses `()` at the beginning of your function declaration.
# 
# **You should pass in parameters for *any* information the function is going to need to execute.**

# In[6]:


# Here's an example of a function that needs parameters in order to avoid repetitive code
# The parameters are `numerator` and `denominator` inside the parentheses

def safe_divide(numerator, denominator):
    if denominator != 0 and isinstance(numerator, (int, float)) and isinstance(denominator, (int, float)):
        return numerator / denominator
    else:
        return None


# Note, the function above has **more than one** `return` statement. That's A-okay! 
# 
# Functions can return different things under different conditions. That's part of what makes them useful.

# In[7]:


# Now, I can use the function above to divide any set of numbers by passing those numbers in as parameters
# This avoids repetitive code! 
print(safe_divide(2, 5))
print(safe_divide(5, 2))
print(safe_divide(5, 0))
print(safe_divide(2, '2'))

# And, if I'm calling this function in lots of places, I don't have to worry about division errors
print(5 / 0)


# 
# 
# ----------------------------------------------------------------------------------------------------------------------
# 
# 

# ## How to call a function in python 

# You've already seen this in the examples above, but here we'll walk through it explicitly.
# 
# To execute a function in python, you call the function's name with parentheses `()` afterwards.
# 
# NOTE: if the function returns a variable (a string, a dictionary, etc.), you need to declare a variable that stores the value that the function is returning for you.

# In[8]:


# Same fxn as above
def get_hello_world_string():
    return "Hello, world"


# Bad: this calls the function, but there's no variable to store the string that gets returned
get_hello_world_string()

# Good: this calls the function and stores the string that gets returned by it in a variable called `greeting`
greeting = get_hello_world_string()
print(greeting)

# That way you can do other stuff with the return value
greeting = greeting.replace('world', 'students')
# greeting = 7
print(greeting)


# **WARNING:** if you don't include the parentheses `()` when you call the function, python thinks you're asking for the function itself, rather than trying to execute it.

# In[9]:


# Bad: no parentheses
greeting = get_hello_world_string

# Watch what happens when we print
print(greeting)


# ### Calling functions with parameters
# 
# When the function expects parameters, you need to include those inside the parentheses `(param1, param2)` when you call the function.

# In[10]:


# Good: including parameters inside the parentheses
pi_approx = safe_divide(355, 113)
print(pi_approx) 
# # Fun fact: 355/113 is the best rational approximation of pi with a denominator less than 30,000!



# Bad: when you don't include parameters in your function call, python has a meltdown
pi_approx = safe_divide()


# ### Using parameter names in your function call
# 
# In addition to the above, you can also use the parameter names themselves when you call a function. 
# 
# *Why do this?* It means you don't have to worry about the order of the parameters in the function call.

# In[11]:


# When I don't include the parameter names, python assigns them in the order that matches the function "declaration"
yes_pi = safe_divide(355, 113)
no_pi = safe_divide(113, 355)
# The above will give me two different values because of the order of the parameters in the function calls
print(yes_pi)
print(no_pi)
print('\n\n')


# The below avoids this problem by using the parameter names inside the function call. 
# Now, the order of the paramters doesn't matter!
more_pi = safe_divide(numerator=355, denominator=113)
also_pi = safe_divide(denominator=113, numerator=355)
print(more_pi)
print(also_pi)
print('\n\n')


# But, be careful. If you include the parameter names in the function call, they need to match exactly!
# error_pi = safe_divide(numerator=355, denom=113)


# Use parameter names when it's helpful for you or another person looking at your code later
from operator import itemgetter
my_map = {'a': 1, 'b': 2, 'c': 3}
my_sorted_map = sorted(my_map.items(), key=itemgetter(1), reverse=True)
print(my_sorted_map)
my_sorted_map = sorted(my_map.items(), itemgetter(1), True)


# 
# 
# ----------------------------------------------------------------------------------------------------------------------
# 
# 

# # Extending function definitions
# 
# Now that you've got the basics, there are two additional things you might need when declaring functions: **parameter defaults** and **variable arguments**.

# ## Adding defaults to your parameters
# 
# A **default value** is the value that python assigns to your *function parameters* if the function call doesn't include a value for that parameter.
# 
# *Why do this?*
# - Assigning default values for your parameters lets somebody call your function without having to know what all the parameters do. 
# - It's also useful when your function *usually* runs in a certain way and the parameters are just there for extra flexibility.
# 
# **To include a default parameter value, use `=` after the parameter in your function declaration.**

# In[12]:


"""
In the function below, we return base^exp.
However, the most common case of raising a number to an exponent is squaring it.
So we set the DEFAULT VALUE for the `exp` parameter to be 2.
"""
def power(base, exp=2):
    return base ** exp


# Now when I call the `power` function, I only need to provide the `base` parameter. 
print(power(3)) # when I don't provide an `exp` parameter value, the `power` function uses the default of 2


# But, I can still call this function just like any other with a `base` AND an `exp` parameter value.
print(power(2, 3)) # when I provide both parameters, the `power` function uses the values I gave it and ignores the default


# print(power(2, base=2))


# ## Adding variable arguments
# 
# A parameter with a **variable number of arguments** lets you declare functions that take in an arbitrary number of parameter values. 
# 
# *Why do this?*
# - This isn't *super common*, but it can be useful when you're writing a function that may operate over an unspecified number of values or items
# 
# **To include a variable argument parameter, use `*` before the parameter name in your function declaration**

# In[13]:


# Here's an example of a function you've seen already that uses this
print('hello', 'hi', 'I\'m a dog', 'I follow you everywher', 'please pet me')


# In[14]:


"""
In the function below, we find the maximum value among a set of 0 or more *args
We check that each element in *args is actually a number and ignore it if it isn't
"""
def safe_max(*args):
    max_val = float('-inf')
    if args:
        for arg in args: # NOTE we can iterate over the *args values just like a list! Neat!
            if isinstance(arg, (int, float)) and arg > max_val:
                max_val = arg
        return max_val
    else:
        return None


# Now, I can call the safe_max function with any number of different parameter values passed in
print(safe_max(2))
print(safe_max(2, 3))
print(safe_max(2, 3, 5, -10, 100))
print(safe_max())
print('\n\n')

# I can even pass in nonsense values because of the checks in my function, which is better than the default `max`
print(safe_max(1600, 1601, None))
print(safe_max(1600, 1601, 'c'))
print(max(1600, 1601, None))


# **NOTE:** Variable argument parameters aren't the only way to pass in multiple things. You can also just pass in whole lists or dictionaries as parameters for similar effect (example below).

# In[15]:




def get_dictionary_max(input_dict):
    return dict(sorted(input_dict.items(), key=itemgetter(1), reverse=True))



count_dict = {
    'cancer': 1,
    'aquarius': 1,
    'gemini': 2,
    'leo': 2,
    'sagittarius': 3
}

# Here, we're passing in the whole dictionary as a parameter. This is super common.
sorted_counts = get_dictionary_max(count_dict)
print(sorted_counts)

# Here, we're actually constructing the dictionary when we call the function! 
# This is not super common but it's an option.
sorted_counts = get_dictionary_max(
    {
        'cancer': 1,
        'aquarius': 1,
        'gemini': 2,
        'leo': 2,
        'sagittarius': 3
    }
)
print(sorted_counts)




# In[ ]:





# 
# 
# ----------------------------------------------------------------------------------------------------------------------
# 
# 

# # 🚨 Function Danger Zone: passing by assignment 🚨

# ### Quick aside: are function parameters the same as variables outside the function?
# 
# Most coding languages make a distinction between passing variables **by reference** and passing variables **by value**.
# - Passing variables by reference means you pass *that exact variable* into the function. Any changes to the variable inside the function change the variable everywhere.
# - Passing variables by value means you pass *the value of that variable* into the function, essentially making a copy of the variable. Any changes to the variable inside the function only change the copy, but not the variable itself.
# 
# *So what does python do?*
# - python actually takes a third course, called passing variables **by assignment**. There's a nice explanation of how this works at the link below. 
# - All you need to know is that changes to variables inside functions will typically change the variable *everywhere* if the variable is *mutable* and will only change it *inside the function* if it's *immutable*.
# 
# passing by assigment: https://medium.com/school-of-code/passing-by-assignment-in-python-7c829a2df10a

# To see this in action, take a look at the below. 

# In[16]:


# What will the two print statements below print out (what numbers)?

a = 12

def fun(x):
    x += a
    print(x)


fun(a)

print(a)


# In the function above, the parameter `x` essentially gets a *copy* of `a`. Changes to `x` inside the function **do not** change `a`. This is what passing by value looks like.

# In[17]:


# What will the two print statements below print out?

a = [12]

def fun(x):
    x.append(3)
#     x[0] += 3 # same idea
    print(x)


fun(a)

print(a)


# The function above is really similar to the first one, but now, changes to the parameter `x` inside the function **do** change `a`. This is what passing by reference looks like.
# 
# The difference is that since lists are **mutable**, they behave like passing by reference. Since the int in the first function is **immutable**, passing it to a function is more like passing by value.

# To see how tricky this stuff can be, take a look at the function below. *What do you think will happen?*

# In[18]:


# What will this print statement say?
a = 12

def fun(x):
    x += 2*a
    print(a, x)

fun(a)


# *What about this one?*

# In[19]:


# What will this print statement say?
a = 12

def fun(x):
    a += 2*x
    print(a, x)

fun(a)


# This is really similar to the function above it! *Why did this one have a problem?*
# 
# In this case, python doesn't think we're talking about the `a` outside the function when we try to assign it a value inside the function. Spooky. 

# # Don't Panic!
# 
# There's a pretty easy solution to the brain teasers above.
# 
# 1. When you **write a new function**, *return a variable* that stores the object the function changed.
# 2. When you **call a function**, declare a variable that you assign to whatever the function returns.
# 3. Don't use **global variables** inside functions. Any information that the function needs should be passed in as a parameter!
# 
# If you do the above, calling functions on strings and lists and any other object will all look about the same. This will take care of 90% of the problems introduced by the code above. The rest you'll learn as you go :)
