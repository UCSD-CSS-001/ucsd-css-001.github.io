#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - A1 due tonight (11:59 PM)
#     - should run from top to bottom (Kernel > Restart + Run all OR Validate)
# - CL3 due Wed (4/14)
# - A2 now available (due Mon 4/19)
# - Just putting it on your radar: 1$^{st}$ midterm is Friday of *next* week (week 4; 4/23)

# **Q&A**
# 
# Q: On one of the print statements, you wrote \n before the actual statement, within the print input. What is that \n?  
# A: That `\n` is a special character that is known as a "newline" character. Whenver Python sees that in a string, it will print a newline (meaning put whatever comes after it on its own line)
# 
# Q: I am curious about the running sum list, but I know it will make more sense later.  
# A: We'll talk about lists today and for loops this Wednesday! At that point, that example will make sense!
# 
# Q: How will exams be formatted? Will they be in Jupyter notebook?  
# A: We're going to discuss this more this week. They will be Jupyter notebooks. They will be on datahub. They will look similar to assignments (but will be shorter and completed completely individually).
# 
# Q: I think I am still confused on the difference between = and ==.  
# A: I think the best suggestion I have here is any time you see `=` read it out loud to yourself as "take the thing on the right and put it in the thing on the left". Whenever you see `==`, read it out loud to yourself as "is the thing on the left exactly equal to the thing on the right". Hopefully this helps!

# # Collections
# 
# - Lists
#     - Indexing
#     - Mutating
# - Tuples

# ## Collections: Lists 

# <div class="alert alert-success">
# A <b>list</b> is a mutable collection of ordered items, that can be of mixed type. Lists are created using square brackets.
# </div>

# ### List examples

# In[1]:


# Define a list
lst = [1, 'a', True]


# In[2]:


# Print out the contents of a list
print(lst)


# In[3]:


# Check the type of a list
type(lst)


# #### Clicker Question #1
# 
# Which of the following specifies a list of 4 items?

# In[4]:


item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]


# - A) item_A
# - B) item_B
# - C) item_C
# - D) item_D
# - E) item_E

# ### Indexing

# <div class="alert alert-success">
# <b>Indexing</b> refers to selecting an item from within a collection. Indexing is done with square brackets.
# </div>

# In[5]:


# Define a list 
my_lst = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']


# In[6]:


# Indexing: Count forward, starting at 0, with positive numbers
print(my_lst[1])


# In[7]:


# Indexing: Count backward, starting at -1, with negative numbers
print(my_lst[-1])


# In[8]:


# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(my_lst[2:4]) 


# In[9]:


# can determine type in list
type(my_lst[2])


# In[10]:


my_lst[2:-1]


# In[11]:


# indexing to end of list
print(my_lst[2:])


# In[12]:


# Indexing from beginning of list
print(my_lst[:4])


# In[13]:


# slicing by skipping a value [start:stop:step]
print(my_lst[0:4:2])


# ### Index Practices

# In[14]:


# Define a list for the examples
example_lst = [1, 2, 3, 4, 5]


# In[15]:


example_lst[2]


# In[16]:


example_lst[-3]


# In[17]:


example_lst[1:3]


# #### Clicker Question #2
# 
# What will be the output of the following piece of code:

# In[18]:


q2_lst = ['a', 'b', 'c','d']
q2_lst[-3:-1]


# - A) ['a', 'b', 'c']
# - B) ['c', 'b', 'a']
# - C) ['c', 'b']
# - D) ['b', 'c', 'd']
# - E) ['b', 'c']

# Note: The following has been added to the notes due to student questions in previous iterations. This and the following two cells are *not* someting you'll be tested on. Including as an FYI for those curious.
# 
# You *can* return ['c','b'] but it combines two different concepts.
# 
# 1. the `start:stop` now refers to indices in the reverse.
# 2. `-1` is used as the step to reverse the output.
# 
# More details about `step`:  
# `step`: the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.

# In[19]:


# slice in reverse
q2_lst[-2:-4:-1]


# In[20]:


# you can use forward indexing
# makes this a little clearer
q2_lst[2:0:-1]


# #### Clicker Question #3
# 
# What would be the appropriate line of code to return `['butter', '&', 'jelly']`?

# In[21]:


q3_lst = ['peanut', 'butter', '&','jelly']


# - A) `q3_lst[2:4]`
# - B) `q3_lst[1:3]`
# - C) `q3_lst[:-2]`
# - D) `q3_lst[-3:]`
# - E) `q3_lst[1:4:2]`

# ### Reminders

# - Python is zero-based (The first index is '0')
# - Negative indices index backwards through a collection
# - A sequence of indices (called a slice) can be accessed using `start:stop`
#     - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
#     - To skip values in a sequence use `start:stop:step`

# ### SideNote: But why is it like this...

# <div class="alert alert-success">
# Starting at zero is a convention (some) languages use that comes from how variables are stored in memory
# , and 'pointers' to those locations.
# </div>

# ### Length of a collection

# In[22]:


# Define a new list
another_lst = ['Peter', 'Hind', 'Jack', 'Pam', 'Barbara', 'Colin', 'Felix']

# Get the length of the list, and print it out
len(another_lst)


# ## The `in` Operator

# <div class="alert alert-success">
# The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
# </div>

# In[23]:


# Define a new list to work with
lst_again = [True, 13, None, 'apples']


# In[24]:


# Check if a particular element is present in the list
True in lst_again


# In[25]:


# The `in` operator can also be combined with the `not` operator
'19' not in lst_again


# ### Practice with `in`

# In[26]:


# Define a list to practice with
practice_lst = [1, True, 'alpha', 13, 'cogs18']


# In[27]:


13 in practice_lst


# In[28]:


False in practice_lst


# In[29]:


'True' in practice_lst


# In[30]:


#searching partial strings
'cogs' in practice_lst


# In[31]:


'cogs18' not in practice_lst


# #### Clicker #4
# 
# After executing the following code, what will be the value of `output`?

# In[32]:


ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst
print(bool_1)
print(bool_2)

output = bool_1 and bool_2

print(output)


# - a) True
# - b) False
# - c) This code will fail
# - d) I don't know

# ### Reminder

# - The `in` operator checks whether an element is present in a collection, and can be negated with `not`

# ## Mutating a List

# <div class="alert alert-success">
# Lists are <i>mutable</i>, meaning after definition, you can update and change things about the list.
# </div>

# In[33]:


# Define a list
updates = [1, 2, 3]


# In[34]:


# Check the contents of the list
print(updates)


# In[35]:


# Redefine a particular element of the list
updates[1] = 0


# In[36]:


# Check the contents of the list
print(updates)


# #### Clicker Question #5
# 
# What would the following code accommplish?

# In[37]:


lst_update = [1, 2, 3, 0, 5]
lst_update[3] = 4 


# In[38]:


print(lst_update)


# - A) replace 0 with 4 in `lst_update`
# - B) replace 4 with 0 in `lst_update`
# - C) no change to `lst_update`
# - D) produce an error
# - E) I'm not sure

# ## Collections: Tuples 

# <div class="alert alert-success">
# A <b>tuple</b> is an <i>immutable</i> collection of ordered items, that can be of mixed type. Tuples are created using parentheses.
# </div>

# ### Tuple Examples

# In[39]:


# Define a tuple
tup = (2, 'b', False)


# In[40]:


# Print out the contents of a tuple
print(tup)


# In[41]:


# Check the type of a tuple
type(tup)


# In[42]:


# Index into a tuple
tup[0]


# In[43]:


# Get the length of a tuple
len(tup)


# ### Tuples are Immutable

# In[44]:


# Tuples are immutable - meaning after they defined, you can't change them
# This code will produce an error.
tup[2] = 1


# #### Clicker Question #6
# 
# Which of the following specifies a tuple of 4 items?

# In[45]:


item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]


# - A) item_A
# - B) item_B
# - C) item_C
# - D) item_D
# - E) item_E

# ## Aside: Aliases
# 
# Note: This was introduced in the Variables lecture.

# In[46]:


# Make a variable, and an alias
a = 1
b = a
print(b)


# Here, the value 1 is assigned to the variable `a`.  
# 
# We then make an **alias** of `a` and store that in the variable `b`. 
# 
# Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

# What if we change the value of the original variable (`a`) - what happens to `b`?

# #### Clicker Question #7
# 
# After executing the following code, what will the values stored in `a` and `b` be?

# In[47]:


# Make a variable & an alias
# change value of original variable
a = 1
b = a
a = 2

print(a)
print(b)


# - A) `a` and `b` both store 1
# - B) `a` and `b` both store 2
# - C) `a` stores 2 `b` stores 1
# - D) `a` stores 1 `b` stores 2
# - E) No clue

# Reminder: integers are **immutable**.

# ### Alias: mutable types
# 
# What happens if we make an alias of a **mutable** variable, like a list?

# In[48]:


first_list = [1, 2, 3, 4]
alias_list = first_list
alias_list


# In[49]:


#change second value of first_list
first_list[1] = 29
first_list


# In[50]:


# check alias_list
alias_list


# In[51]:


# works in both directions
# if you update alias_list
# first_list also updated
alias_list[2] = 929
alias_list


# In[52]:


first_list


# For *mutable* type variables, when you change one, both change.

# #### Clicker Question #8
# 
# After executing the following code, what will the second value stored in `second_tuple`?

# In[53]:


# Make a variable & an alias
# change value of original variable
my_tuple = (1, 2, 3, 4)
second_tuple = my_tuple
my_tuple[1] = 29 


# In[54]:


second_tuple[1]


# - A) 1
# - B) 2
# - C) 29
# - D) This will Error
# - E) I'm lost.

# ### Why allow aliasing? 
# 
# Aliasing can get confusing and be difficult to track, so why does Python allow it?
# 
# Well, it's more efficient to point to an alias than to make an entirely new copy of a a very large variable storing a lot of data. 
# 
# Python allows for the confusion, in favor of being more efficient.

# ## Strings as Collections

# <div class="alert alert-success">
# Strings act similarly to ordered collections of homogenous elements - specifically characters. But, they are <b>immutable</b>.
# </div>

# In[55]:


# Define a string
my_str = 'TheFamousFive'


# In[56]:


# Index into a string
my_str[2]


# In[57]:


# Ask if an item is in a string
'Fam' in my_str


# In[58]:


# Check the length of a string
len(my_str)


# In[59]:


# Index into a string
# This code will produce an error
my_str[1:3] = 'HE'


# ### SideNote: using counters

# In[60]:


# Initialize a counter variable
counter = 0 
print(counter)


# In[61]:


counter = counter + 1
print(counter)


# In[62]:


counter = counter + 1
print(counter)


# ## Pulling it Together: Collections, Membership & Conditionals

# #### Clicker Question #9
# 
# What will be the value of `counter` after this code is run?

# In[63]:


len(things_that_are_good)


# In[64]:


things_that_are_good = ['python', 'data', 'science', 'tacos']

counter = 0

if 'python' in things_that_are_good:
    counter = counter + 1

if len(things_that_are_good) == 4:
    counter = counter + 1
    
if things_that_are_good[2] == 'data':
    counter = counter + 1 
    
print(counter)


# <pre> A) 0   B) 1   C) 2   D) 3   E) 4 </pre>

# #### Clicker Question #10
# 
# What will be printed out from running this code?

# In[65]:


lst = ['a', 'b', 'c']
tup = ('b', 'c', 'd')

if lst[-1] == tup[-1]:
    print('EndMatch')
elif tup[1] in lst:
    print('Overlap')
elif len(lst) == tup:
    print('Length')
else:
    print('None')


# <pre> A) EndMatch   B) Overlap   C) Length   D) Overlap & Match   E) None </pre>
