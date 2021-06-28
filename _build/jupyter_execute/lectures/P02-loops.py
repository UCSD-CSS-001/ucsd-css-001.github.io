#!/usr/bin/env python
# coding: utf-8

# # P02: Control flow and logic
# 
# Computer programs become very powerful once we can command their flow of execution.  This is done via two primary control structures:
# 
# - Conditionals (`if...elif...else`) statements that allow the program execution to *branch*, and
# - Loops (`for` and `while`) that allow the program execution to *repeat*.

# ## Lists
# 
# So far we have dealt with *atomic* data types.  We will also want to work with compound data types that contain lots of things.  The most common compound data type in Python is a **list**.  A list is a **sequence** of objects, which can be created with square brackets: `[1, 2, 3]`

# In[1]:


my_list = [1, 2, 'a', 3]
print(my_list)


# we will talk much more about lists and sequences later, but for the sake of this week's problem set, we need to learn how to *add* items to a list, and how to *loop* through a list.
# 
# ### adding to a list
# 
# We can add to an existing list with the `.append()` method.

# In[2]:


print(my_list)
my_list.append('cow')
print(my_list)


# ## for loop iteration over a list
# 
# If we want to do something to each member of a list, we want to *iterate* over that list in a *for* loop.   To accomplish this, we will use the `for` loop control structure:
# 
# ```python
# for x in iterable:
#     do stuff
#     do more stuff
# ```
# 
# What this notation is doing is generating a "loop", which iterates over all the elements in `iterable`.  On each iteration it assigns the next item from the iterable to `x`, and then executes the for loop code block (indicating by indentation).

# In[3]:


my_list = [1, 2, 'a', 3]
for item in my_list:
    print(item)


# ### range()
# 
# It is very common to run a for loop over some sequence of integers.  So it would be helpful to have a function that defines a sequence of integers for us.
# 
# The command `range` does that.
# 
# The syntax for the range command is
# `range(first, last_plus_one)`
# 
# and it generates an *iterable* that we can *iterate* over (such as in a for loop) with the integers starting with `first` and ending at `last_plus_one`-1 (in steps of 1 -- default if no 3rd argument is provided)

# In[4]:


for i in range(5, 21):
    print(i)


# Note that 21 was not printed!
# 
# If we provide only one argument, it assumes that `first=0` and treats the argument we provide as `last_plus_one`.

# In[5]:


for i in range(10):
    print(i)


# Note that 10 was not printed!
# 

# # Control Flow - Loops
# 
# - `while`
# - `for`
#     - `range`
#     - `continue`
#     - `break`

# ## Loops

# <div class="alert alert-success">
# A <b>loop</b> is a procedure to repeat a piece of code.
# </div>

# ### Avoid copy + pasting
# 
# For repetitive actions, if you find yourself copying + pasting, rethink your strategy.
# 
# Loops are one way to avoid this.

# In[6]:


lst = ['you@yahoo.com', 'them@bing.com']

email = lst[0]

email = lst[1]


# ## While Loops

# <div class="alert alert-success">
# A <b>while loop</b> is a procedure to repeat a piece of code while some condition is still met.
# </div>

# `while` loops always have the structure:
# 
# ```python
# while condition:
#     # Loop contents
# ```
# 
# While condition is true, execute the code contents.
# 
# Repeat until condition is no longer True.

# ## While Loops

# In[7]:


number = -5

while number < 0:
    print(number)
    number = number + 1


# ### While Loop Example I

# In[8]:


connected = False

while not connected:

    # Try and establish connection (placeholder code)
    print('Establishing Connection...')

    break


# ### While Loop Example II

# In[9]:


has_user_input = False

while not has_user_input:

    # Ask for user input (placeholder code)
    print('Asking for user input...')

    break


# #### Clicker Question #1
# 
# How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?

# In[10]:


temperature = 115

while temperature > 112:
    print(temperature)
    temperature = temperature - 1

print('The tea is cool enough.')


# - A) 1
# - B) 2
# - C) 3
# - D) 4
# - E) Infinite
# 

# #### Clicker Question #2
# 
# What will be the value of `counter` after this loop is run:

# In[11]:


keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1

    if counter > 3:
        keep_looping = False

print(counter)


# <pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre>

# ### Stepping Through the Loop
# 
# (Note: We skip this in class.) This is the same code as above with `print()` statements to explain what's going on at each step. If you're confused by the class example, walk through it here with the `print()` statements to guide you.

# In[12]:


keep_looping = True
counter = 0

while keep_looping:
    print('START LOOP')
    print('\tStart counter: ', counter)

    counter = counter + 1

    print('\tMid counter: ', counter)

    if counter > 3:
        keep_looping = False

    print('\tEnd counter: ', counter)

print('\nFinal counter: ', counter)


# ## For Loops

# <div class="alert alert-success">
# A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
# </div>

# ### For Loop Example I
# 
# Looping through a list

# In[13]:


# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)

print('\tLast value: ', my_item)


# ### For Loop Example II
# 
# Looping through a string

# In[14]:


# Loop across items in a string
for char in 'python':
    print(char)


# #### Clicker Question #3
# 
# What will the following loop print out:

# In[15]:


my_lst = [0, 1, 2, 3, 4]

for item in my_lst[0:-2]:
    print(item + 1)


# - A) 0, 1, 2
# - B) 0, 1
# - C) 1, 2
# - D) 2, 3
# - E) 1, 2, 3

# #### Clicker Question #4
# 
# How many values will be output from this `for` loop before it *first* prints "The tea is too hot!"?

# In[16]:


temperatures = [114, 115, 116, 117, 118]

for temp in temperatures:
    print(temp)

    if(temp > 115):
        print('The tea is too hot!')


# - A) 1
# - B) 2
# - C) 3
# - D) 4
# - E) Infinite
# 

# ## `range`

# <div class="alert alert-success">
# <code>range</code> is an operator to create a range of numbers, that is often used with loops.
# </div>

# ### `range` Examples

# In[17]:


for ind in [0, 1, 2, 3, 4]:
    print(ind)


# In[18]:


# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))


# In[19]:


# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)


# In[20]:


# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)


# In[21]:


# using range in example above
for temp in range(114, 119):
    print(temp)

    if(temp > 115):
        print('The tea is too hot!')


# #### Clicker Question #5
# 
# How many values would this loop print and what would be the last value printed?

# In[22]:


for ind in range(1, 10, 3):
    print(ind)


# - A) values printed: 3; last value: 7
# - B) values printed: 3; last value: 9
# - C) values printed: 4; last value: 9
# - D) values printed: 7; last value: 7
# - E) values printed: 7; last value: 9
# 

# ## `continue`

# <div class="alert alert-success">
# <code>continue</code> is a special operator to jump ahead to the next iteration of a loop.
# </div>

# ### `continue` examples

# In[23]:


lst = [0, 1, 2, 3]

for item in lst:

    if item == 2:
        continue

    print(item)


# In[24]:


courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue

    print(course)
    print(course + '!')


# In[25]:


string = 'python'

for char in string:

    if char == 'p' or char == 'y':
        continue

    print(char)


# #### Clicker Question #6
# 
# What will be the value of `counter` after this code has run:

# In[26]:


counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item in my_lst:
        continue
    else:
        counter = counter + 1

print(counter)


# - A) 0
# - B) 1
# - C) 2
# - D) 3
# - E) 4

# ## `break`

# <div class="alert alert-success">
# <code>break</code> is a special operator to break out of a loop.
# </div>

# In[27]:


connected = False

while not connected:

    # Try and establish connection (placeholder code)
    print('Establishing Connection...')

    break


# ### `break` examples

# In[28]:


lst = [0, 1, 2, 3]

for item in lst:

    if item == 2:
        break

    print(item)


# In[29]:


courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break

    print(course)


# In[30]:


string = "love python"

for char in string:
    if char == "p" or char == "y":
        break

    print(char)


# In[31]:


# using range in example above
for temp in range(114, 119):
    print(temp)

    if(temp > 115):
        print('The tea is too hot!')
        break


# #### Clicker Question #7
# 
# What will the following code print out:

# In[32]:


number = 1

while True:
    if number % 3 == 0:
        break

    print(number)

    number = number + 1


# - A) 1
# - B) 1 2
# - C) 1 2 3
# - D) Something else
# - E) This code prints forever

# #### Clicker Question #8
# 
# For how many `temp` will output be printed from this for loop?
# 
# (In other words, how many times in this `for` loop will something be printed out?)

# In[33]:


# using range in example above
for temp in range(114, 119):

    if(temp < 116):
        continue
    elif(temp == 116):
        print('The tea is too hot!')
    else:
        break


# - A) 0
# - B) 1
# - C) 3
# - D) 5
# - E) 6

# #### Clicker Question #9
# 
# What will be the value of `counter` after this code has run:

# In[34]:


counter = 0
my_lst = [False, True, False, True]


for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1

print(counter)


# - A) 0
# - B) 1
# - C) 2
# - D) 3
# - E) 4

# ## Loops Practice

# ### Loops Practice #1
# 
# Write a loop that adds all the *odd* numbers between 1 and 1000 together.

# In[35]:


# YOUR CODE HERE
# loop through values from 1 to 1000:
output = 0

for val in range(1,1000):
    # if odd:
    if val % 2 != 0:
        # add value to variable
        output = output + val

print(output)

# could also use range(1,1000,2) to
# skip every other value


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Loops Practice #2
# 
# Store your name as a string in a variable called `my_name`.
# 
# Write a loop that will loop through all the letters in `my_name` and count all the vowels in your name.

# In[36]:


'A' in ['A', 'E', 'I', 'O', 'U']


# In[37]:


# YOUR CODE HERE
my_name = 'Shannon'
counter = 0
vowels = ['A', 'E', 'I', 'O', 'U',
          'a', 'e', 'i', 'o', 'u']

# loop each letter through my_name:
for letter in my_name:
    # if letter is vowel:
    if letter in vowels:
        # increase counter by 1
        counter = counter + 1

print(counter)


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.
