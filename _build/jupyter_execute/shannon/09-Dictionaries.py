#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**
# - A2 due Monday
# - CL4 due next Wednesday
# - E1 is next Friday 
# 
# **Notes**
# - CL2 Scores have been posted
# - CL3 Answer key on website

# **Common Question**
# 
# Q: When you say "first element" or "first item" in the list...what do you mean?  
# A: I mean the first thing in the list, which is in the zeroth index. What I mean will be made *very* clear on the wording on any exams.

# In[1]:


# 'first item' is the first item/element here
# 'second element' is the 2nd item/element here
my_list['first item', 'second element']


# Q: Why did `range` only have an `*` in that one place?  
# A: The `*` "unpacks" the `range` object. Otherwise, if you try to `print()` out the contents of `range`, python will tell you it's a range type object...but not show you its contents. You'll never need to use the `*` with `range`
# 
# Q: What's the difference if `print()` is inside vs. outside the loop?  
# A: When it's inside the loop, the `print()` statement will `print()` something every time through the loop. When it's outside, it will only `print()` once, after the loop terminates.
# 
# Q: Help! I'm confused about stepping through the loop!  
# A: You're not alone - this is the most difficult concept we've discussed so far. We'll do more examples in class. And, CL3 should help! If that doesn't, two suggestions: 1) ask to step through a loop together in anyone's office hours and 2) "talk" to yourself (like, out loud) and explain what happens each time through the loop
# 
# Q: What values can go in `range`? Can we use floats?  
# A: Integers only! Floats will give you a TypeError (i.e. `range(0.3, 5.6)`).
# 
# Q: The loops in lecture were simple. What happens when they're more complicated? When we encounter an infinte loop?  
# A: See CL3 for how to handle infinite loops! And, we'll do some more complicated examples soon!
# 
# Q: Do `for` loops work on all collection types?  
# A: Yup! lists, tuples strings, `range`...and coming soon dictionaries!

# # Encodings & Dictionaries
# 
# - symbols & representations
# - Encodings
# - Dictionaries
# - `ord` & `chr`

# What is a human representaion? human encoding? 
# 
# How do computers encode information?

# ## Symbols

# <div class="alert alert-success">
# Symbols are characters (or 'signs') of arbitrary shape, that can refer to (or represent) something. 
# </div>

# ##  Representation

# <div class="alert alert-success">
# To represent means to stand in for something.
# </div>

# - **iconic representation** : the object looks like the thing it represents (i.e. a picture)
# - **symbolic representation** : the symbol does *not* look like the thing it represents (i.e. letters, numbers) 
# 

# ### Symbol Examples : concepts
# 
# - The symbol `2` represents the concept of `two-ness`. 
#     - This is arbitrary: there is nothing 'two-like' about `2`
#     - We need not use this symbol. The symbol `II` also represent `two-ness`.
#     - `2` and `II` are two different representations for the concept of two.
# - The symbol `b`, in english represents the sound `buh` (sort of). 
#     - There is nothing 'buh' like about the symbol `b`

# ### Symbol Examples : rules
# 
# Given the symbol `2`, or `b` we have systematic rules of things we can do with them. 
# - We can take `2` and add `1` and get a new symbol which represents the concept of `the value one bigger than two`
# - We can concatenate some, but not all, other letters (symbols) to `b` to start making rules
# - These rules are agnostic to what `2` or `b` represent, they are simply manipulations we can do with these symbols

# ## Digital Computers
# 
# Computers don't care about what the symbols look like. They don't care what symbols you use.
# 
# But, once a rule is established for a certain symbol, the computer will always follow that rule. 

# <div class="alert alert-success">
# Computation is symbol manipulation - using formal rules to manipulate symbols. 
# </div>

# Whenever we have symbols, and rules to manipulate them, we can do computation. 
# 
# When we use these symbols that represent meaningful things, we can use computers to make meaningful inferences.
# 
# Everything you think of as a computer (laptop, cell phone, etc.) works as a digital computer.

# ##  Encoding & Decoding

# <div class="alert alert-success">
# Encoding can be thought of as the process of 'changing representation', and decoding as the process of changing it back. 
# </div>

# Changing back and forth between using the symbol '2' and 'II' to represent the concept of two is an example of "changing representation."

# ## Aside: Binary
# 
# Fundamentally, digital computers can represent two states. Because of this, we say computers are / use binary. 
# 
# From binary, we can build up to store other things, that reduce down to binary representations.
# 
# We can then encode any value we would like to represent on our computer.  

# ### Binary in Code

# In[2]:


## The `bin` operator returns the binary representation of an integer
# encoding an integer
print(bin(1))


# In[3]:


print(bin(78))


# In[4]:


#possible to encode Booleans in binary
#encoding a boolean
bin(False)


# In[5]:


print(bool(0b0))


# In[6]:


# We can also convert binary back to integers with 
# decoding from binary
int(0b1011)


# ## Character Encodings

# Character encodings are a set of rules of how to represent a broad range of characters (symbols) in computers. 
# 
# We already have a way to represent numbers in binary.  
# 
# Using numbers, we can build a general procedure to encode characters as numbers.
# 
# We then have a way to represent characters, that we can reduce all the way to binary, that we can use that on computers.

# ## Example: Character Encoding

# As a simple example, let's assign a number to a series of characters we want to be able to represent. 
# 
# Every time we see that number, we can evaluate it to replace it with the character it represents. 

# ### Character Encoding in Code

# In[7]:


# Set the value we want to encode
character_encoding = 0

# Use conditional to interpret the character as a particular symbol
if character_encoding == 0:
    print('ñ')
elif character_encoding == 1:
    print('é')
elif character_encoding == 2:
    print('¿')


# ## Dictionaries
# 

# <div class="alert alert-success">
# A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
# </div>

# ### Dictionaries as Key-Value Collections

# In[8]:


# Create a dictionary
dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}


# In[9]:


# Check the contents of the dictionary
print(dictionary)


# In[10]:


# Check the type of the dictionary
type(dictionary)


# In[11]:


# Dictionaries also have a length
# length refers to how many pairs there are
len(dictionary)


# ### Dictionaries: Indexing & Looping

# In[12]:


# Dictionaries are indexed using their keys
dictionary['key_1']


# In[13]:


# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])


# In[14]:


# another approach that you will find if you Google
for key, val in dictionary.items():
    print('Loop Iteration')
    print('\tKey:\t', key)
    print('\tValue:\t', val)


# #### Clicker Question #1
# 
# Which of the following would create a dictionary of length 3?
# 
# - A) `{'Student_1' : 97, 'Student_2'}`
# - B) `{'Student_1', 'Student_2', 'Student_3'}`
# - C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`
# - D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`
# - E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`
# 

# #### Clicker Question #2
# 
# Fill in the '---' in the code below to return the value stored in the second key.

# In[15]:


height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict['height_2']


# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# ### Example Dictionaries

# In[16]:


student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails


# In[17]:


completed_coding_lab = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

completed_coding_lab


# In[18]:


mixed_types = {
    True  : [1, 2, 3],  
    False : None
}

mixed_types


# #### Clicker Question #3
# 
# Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.
# 
# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# In[19]:


# YOUR CODE HERE
car = {'make':'Hyundai', 
       'model':'Santa Fe',
       'year':2017}
car


# ### Dictionaries are mutable
# 
# This means that dictionaries, once created, values *can* be updated.

# In[20]:


# remember what dictionary we created above
completed_coding_lab


# In[21]:


# change value of specified key
completed_coding_lab['A5678'] = True
completed_coding_lab


# Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

# In[22]:


print(completed_coding_lab)
len(completed_coding_lab)


# In[23]:


## remove key-value pair using del
del completed_coding_lab['A5678']

print(completed_coding_lab)
len(completed_coding_lab)


# ### Dictionaries and operators
# 
# The operators we've discussed previously can be used when working with dictionaries.
# 
# To determine if a specified key is present in a dictionary we can use the `in` operator:

# In[24]:


if 'A1234' in completed_coding_lab:
    print('Yes, that student is in this class')


# ### Additional Dictionary Properties
# 
# - Only one value per key. No duplicate keys allowed. 
#     - If duplicate keys specified during assignment, the last assignment wins.

# In[25]:


# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}


# - **keys** must be of an immutable type (string, tuple, integer, float, etc)
# - Note: **values** can be of any type

# In[26]:


# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}


# - Dictionary keys are case sensitive.
# 

# In[27]:


{'Student' : 97, 'student': 88, 'STUDENT' : 91}


# #### Clicker Question #4
# 
# Why does the following code produce an error?

# In[28]:


student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : ['ada@analyticengine.com'],
    'Ada Lovelace' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}


# In[29]:


student_emails


# - A) duplicate keys
# - B) mutable key specified
# - C) keys are case sensitive 
# - D) mutable value specified 
# - E) ¯\\\_(ツ)\_/¯

# ## Character Encodings with Dictionaries

# In[30]:


# Define some character encodings
character_encodings = {
    0 : 'ñ',
    1 : 'é',
}


# In[31]:


# Use character encodings to use symbols we want - example 1
my_sentence = 'no hablo espa' + character_encodings[0] + 'ol'
print(my_sentence)


# In[32]:


# Use character encodings to use symbols we want - example 2
my_sentence = 'yo hablo ingl' + character_encodings[1] + 's'
print(my_sentence)


# ## Unicode

# <div class="alert alert-success">
# Unicode is a system of systematically and consistently representing characters. 
# </div>

# Every character has a unicode `code point` - an integer that can be used to represent that character. 
# 
# If a computer is using unicode, it displays a requested character by following the unicode encodings of which `code point` refers to which character. 

# ### ORD & CHR

# <div class="alert alert-success">
# <code>ord</code> returns the unicode code point for a one-character string.
# </div>
# 
# <div class="alert alert-success"> 
# <code>chr</code> returns the character encoding of a code point. 
# </div>

# ### ord & chr examples

# In[33]:


print(ord('a'))


# In[34]:


print(chr(97))


# ### Inverses
# 
# `ord` and `chr` are inverses of one another. 

# In[35]:


inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)


# In[36]:


ord('a')


# In[37]:


chr(97)


# **Course Announcements**
# 
# **Due Dates**
# - A2 due tonight
# - CL4 due Wednesday
# - E1 is Friday (released 8AM; due Sat 8AM)
#     - No Office Hours Friday
#     - No Lecture on Friday

# **Q&A**
# 
# Q: I know it was right at the end of the class but the ord and chr were confusing. I know that one gives an integer and the other a character but why? What is the integer part supposed to be? / How do we find which unicode represents a specific character?    
# A: `ord` returns the [unicode code points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) for any given character. It's a way to represent a character as a number. This allows characters to be interpreted consistently across computing systems.
# 
# Q: If we are building an app for python, how does the code interact with a user? How does the dictionary play a part of that?  
# A: This is a tougher question to answer here. One way, would be through a GUI (See `tkinter`, for example) where there is python code behind the scenes and the user enters information. The way a dictionary comes into play is if you wanted to store information about each user, for example. The user's name/ID could be the key and what you information wanted to store about that user would be its value.
# 
# Q: What does '+=' in CL 4?  
# A: `+=` is shorthand for "add the thing on the right to the variable on the left and store it back in the variable on the left. For example `a += 4` is the same as `a = a + 4`.
# 
# Q: Once we open the midterm will it be timed or do we have a 24hr window to complete it?  
# A: 24h window

# ## Extra Practice

# ### Extra Practice #1
# 
# Generate a dictionary called `about_me` that meets the following criteria:
# 
# - has three keys: 'name', 'favorite_game', and 'height'
# - stores _your_ `name` (string), `favorite_game` (string), and `height` (int) in inches as each key's value
# 

# In[38]:


# YOUR CODE HERE
about_me = {'name':'Shannon', 
            'favorite_game':'Coup', 
            'height':65}
about_me


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Extra Practice #2
# 
# Store your name in the variable `my_name`. Then, encode your  name, such that each letter is first replaced by the unicode code point for that letter plus 500 and then turned back into a character using `chr`. Store the new output in `out_name`.

# In[39]:


chr(ord('S') + 500)


# In[40]:


# YOUR CODE HERE
my_name = 'Shannon'
out_name = ''

for ltr in my_name:
    out_name = out_name + chr(ord(ltr) + 500)
#     print(out_name)

out_name


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.