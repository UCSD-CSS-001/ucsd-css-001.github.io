#!/usr/bin/env python
# coding: utf-8

# ![GWC](img/GWC_Logo_2020.png)
# 
# GWC (Girls Who Code) College Loops: [Officer Applications](https://urldefense.com/v3/__https://forms.gle/nXASsZ2huQPXbSR38__;!!Mih3wA!VCPf_NbZe3FHa9u_KpFgX74Evoo7uOEIycX5otpbZUkxGraHtSXCC4EIZYRctw$)

# **Course Anouncements**
# 
# Due Dates:
# - **CL5** due today (11:59 PM)
# - **[Mid-Course Survey](https://docs.google.com/forms/d/e/1FAIpQLScE182NPFjsKn78p2MqzsQtxxVgCyw8tPYKToDF4J_4YybmAw/viewform?usp=sf_link)** "due" Mon 5/3 (*optional*; link also on Canvas)
# - **A3** due 5/10 (Mon of Wk 7)
#     - whatever you submit by 5/3 (next Mon; wk 6), we'll "grade" it & release feedback (*optional*)
# 

# **Q&A**
# 
# Q. What was `locals()` again?  
# A. While this is not something you'll be tested on, what `locals()` does is returns a dictionary of all variables currently "in scope" - think of this as all things python can currently "see" and access. So, within a funcion, `locals()` can only "see" the variables passed in as arguments or those defined within the function. Outside of the function, `locals()` can "see" all of the variables/functions/etc. you've defined in that notebook. It returns what's in your current namespace - but keep in mind fucntions have their own namespace.
#  
# Q. What is `pass`?  <br>
# A. It's a way to tell python to "move along" without there being any code. (I only use it in examples when I'm trying to highlight a specific syntax; there's no reason you'd need it in your code.)
# 
# Q. Is it possible to design functions that work for both lists and integers as inputs? Is that possible?  
# A. It is possible. You could, for example have a conditional that checks the type of the input and if it's an integer do one thing and if it's a list do another, for example! At the end of today's notes, see the extra bit about type checking!

# # Algorithms
# 
# What are the sorts of things that we should do with computers? What are things that are easy to compute? Hard to compute? Impossible to compute?

# ## Algorithms

# <div class="alert alert-success">
# An <b>algorithm</b> is a formal description of how to complete a procedure, typically taking inputs and returns some output.
# </div>

# If you can write the steps down, you can write an algorithm.
# 
# Algorithms are computable.

# Computers cannot read between the lines. They are very literal.

# ## Algorithm Example: Making a Sandwich

# #### Clicker Question #1
# 
# Can you write an algorithm to make a ham and cheese sandwich. 
# 
# - A) Yes 
# - B) No
# - C) I don't know

# ## Algorithm for making a ham & cheese sandwich
# 
# - take bread
# - put ham on bread
# - put cheese on ham
# - put bread on cheese

# Humans are pretty good at making sandwiches. Computers may struggle a bit.

# ## Algorithm Example: Sorting
# 
# Given a list of numbers, how can we sort it into the correct order?

# In[1]:


# Define a list of numbers
list_of_numbers = [2, 1, 3]  


# #### Clicker Question #2

# **array**: a collection of items, where each item can be accessed by its index.

# Can you write an algorithm to sort an array?
# 
# - A) Yes 
# - B) No
# - C) I don't know

# Y'all Google is *really* good at sorting.
# 
# - ranking: rate a site as how related
# - sort: given a list of good sites, determine order to present to user
# 
# ...and do this on all the things

# ## `sort_array`
# 
# A version of a **selection sort**:
# - loop through current list
# - find lowest item
# - put that at the front of your sorted list
# - remove lowest item from current list
# - wash, rinse, repeat

# In[2]:


def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to store sorted values
     
    while not is_sorted:

        lowest = None
        for item in array_to_sort:
            if lowest == None:         # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines use new methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
            is_sorted = True
    
    return sorted_array


# In[3]:


test_list = [4, 3, 6]


# In[4]:


sort_array(test_list)


# ## Using `sort_array`

# In[5]:


# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# In[6]:


# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# #### Clicker Question #3
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[7]:


data = ['a', 'c', 'b'] 
sort_array(data)


# - A) ['a', 'c', 'b']
# - B) ['a', 'b', 'c']
# - C) [97, 98, 99]
# - D) None
# - E) This code will fail

# ### How Python evaluates strings

# In[8]:


'a' < 'b'


# In[9]:


ord('a')


# In[10]:


ord('b')


# #### Clicker Question #4
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[11]:


data = [True, False, True]
sort_array(data)


# - A) [False, True, True] 
# - B) [True, False, True] 
# - C) [0, 1, 1]
# - D) [True, True, False] 
# - E) This code will fail

# ### How Python evaluates Booleans

# In[12]:


True < False


# In[13]:


bin(True)


# In[14]:


bin(False)


# #### Clicker Question #5
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[15]:


data = [[1, 4], [1, 2]]
sort_array(data)


# - A) [[1, 4], [1, 2]]  
# - B) [1, 1, 2, 4] 
# - C) [[1, 2], [1, 4]]
# - D) None 
# - E) This code will fail

# ## SideNote: `sorted`

# In[16]:


# Sort a list, with `sorted`
data = [7, 4, 6]
sorted(data)


# In[17]:


# what about a list of strings?
sorted(['asdf','abcd'])


# In[18]:


# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[1, 4], [1, 2]]))


# ## Algorithmic Complexity

# <div class="alert alert-success">
# The complexity of an algorithm characterizes the relationship between the input size and the number of steps of an algorithm.
# </div>

# ## Algorithmic Complexity 
# 
# Things we might care about:
# - The number of steps it takes to complete our algorithm
#     - Usually defined in relation of the size of the input
# - The amount of memory it will take to run our algorithm

# ## Properties of our sorting algorithm
# 
# - It will require $n^2$ steps, where $n$ is the length of the list
# - It will require ~double the memory of the original list

# ## Computability

# Things that computers can do are things that we can write down an algorithm to do.
# 
# Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.

# ## Variable Type Checking
# 
# **Note**: The rest of the noteook includes notes to answer a student's in class question. You are not expected to know this, but you are free to learn and use the information!
# 

# To check on an input variable's type, you can use the following approach:
# 
# ```python
# isinstance(object, classinfo) 
# ```
# 
# `isinstance()` takes two parameters:
# - `object` : variable/object to be checked
# - `classinfo` : class, type, or tuple of classes and types

# For example, using the `string_manipulator` function from earlier, note that I've added the following two lines: 
# 
# ```python
# if not isinstance(string, str):
#     print("Warning: please provide a string as input")
# ```
# 
# This checks to see if the input is anything other than a string. If it is, the function prints a warning.

# In[19]:


def string_manipulator(string):
    
    if not isinstance(string, str):
        print("Warning: please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[20]:


# use function with a string
string_manipulator('hello!')


# In[21]:


# print warning if not a string
string_manipulator(5)


# However, sometimes, you want it to raise an error rather than just print something. Here we use `raise` instead of print. In this case, an error will be returned (with our specified message) to the user if the wrong variable type is provided:

# In[22]:


def string_manipulator(string):
    
    if not isinstance(string, str):
        raise ValueError("Please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[23]:


# raise error instead of print message
string_manipulator(5)
