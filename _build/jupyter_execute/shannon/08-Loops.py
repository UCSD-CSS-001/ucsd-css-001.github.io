#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - CL3 due tonight (11:59 PM)
# - A2 due Monday (4/19)
# 
# **Notes**
# - A1 will be graded on Friday (all assignments graded ~1wk from due date)
# - E1 (1$^{st}$ midterm) is *next* Friday

# **Q&A**
# 
# Q: I am still confused on the purpose of the Tuples. Why do we need to separate the collection to tuples and list?  
# A: Whenever you do not want to allow users or your code to change values in a collection, you'll want to use a tuple, as this avoids inadvertent changes. The opposite, when you want to be able to update part of a collection, is when you'll want to use a list.
# 
# Q: I like to take notes on datahub after updating my lecture notes from the Canvas. if I update my lecture notes from the link on Canvas after I edit the files, will that overwrite my own notes and change all the files to default (notes from class without my own notes)?  
# A: Nope - your notes will still be there!
# 
# Q: What does -1 mean as a step? Skip every element?  
# A: Nope. 1 means show every element. -1 actually reverses the output, so the output return the slice in the reverse order.
# 
# Q: Are `range()` objects mutable or immutable?  
# A: They are immutable.

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

# In[1]:


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

# In[2]:


number = -5

while number < 0:
    print(number)
    number = number + 1


# ### While Loop Example I

# In[3]:


connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break


# ### While Loop Example II

# In[4]:


has_user_input = False

while not has_user_input:
    
    # Ask for user input (placeholder code)
    print('Asking for user input...')
    
    break


# #### Clicker Question #1
# 
# How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?

# In[5]:


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

# In[6]:


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

# In[7]:


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

# In[8]:


# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)
    
print('\tLast value: ', my_item)


# ### For Loop Example II
# 
# Looping through a string

# In[9]:


# Loop across items in a string
for char in 'python': 
    print(char)


# #### Clicker Question #3
# 
# What will the following loop print out:

# In[10]:


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

# In[11]:


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

# In[12]:


for ind in [0, 1, 2, 3, 4]:
    print(ind)


# In[13]:


# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))


# In[14]:


# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)


# In[15]:


# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)


# In[16]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')


# #### Clicker Question #5
# 
# How many values would this loop print and what would be the last value printed? 

# In[17]:


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

# In[18]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        continue
    
    print(item)


# In[19]:


courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue
  
    print(course)
    print(course + '!')


# In[20]:


string = 'python'

for char in string: 
    
    if char == 'p' or char == 'y':
        continue
        
    print(char)


# #### Clicker Question #6
# 
# What will be the value of `counter` after this code has run:

# In[21]:


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

# In[22]:


connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break


# ### `break` examples

# In[23]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        break
    
    print(item)


# In[24]:


courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break
  
    print(course)


# In[25]:


string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)


# In[26]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
        break


# #### Clicker Question #7
# 
# What will the following code print out:

# In[27]:


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

# In[28]:


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

# In[29]:


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

# In[30]:


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

# In[31]:


'A' in ['A', 'E', 'I', 'O', 'U']


# In[32]:


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
