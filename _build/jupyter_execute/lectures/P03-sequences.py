#!/usr/bin/env python
# coding: utf-8

# 
# ## Sequences and indexing
# 
# We have seen string types before, but strings are a special kind of "sequence" data type.  Specifically, a string is a sequence of characters.  Sequences are a list of many objects of the same type.

# In[1]:


sentence = 'This is a sentence about string sequences!'


# The string stored in `sentence` is represented as a sequence of characters.  We can get the *length* of that sequence using the `len()` function:

# In[2]:


len(sentence)


# ### Indexing
# 
# We can pull out elements of that sequence by indexing and slicing.
# Python has 0-indexed lists, which means that the first element has the index of 0, and the last element has an index of `len(x)-1`

# In[3]:


sentence[0]


# We can pull out any letter by referring to its index.  For instance, the 6th letter of the string ('i' in 'is') has the index 5:

# In[4]:


sentence[5]


# The last element of the sequence has an index of `len(x)-1`:

# In[5]:


sentence[len(sentence)-1]


# But we can also refer to it with the helpful shortcut of `-1`.  In general, we can refer to elements by indexing from the beginning (starting with 0), or indexing from the end, starting with -1.

# In[6]:


sentence[-1]


# ### Slicing
# 
# We often want to pull out multiple elements of a sequence, for instance, maybe we want all the characters between the 6th ('i') and 12th (first 'e' in 'sentence').  We can do this with the slicing notation `5:12`.

# In[7]:


sentence[5:12]


# Note that this slicing notation includes the first index (5) through the second index -1 (i.e., it pulls out index 5, 6, 7, 8, 9, 10, and 11, but not 12).  This is convenient because `0:len(x)` will yield the full sequence.  It is also useful that the number of elements in the slice defined by `start:stop` is equal to `stop-slice` (because `stop` defines the first element that is *not* included)

# #### Slice step
# 
# When slicing, we can also specify a 3rd argument, indicating how to increment the indices we include.  By default (when it is omitted) this value is 1.
# 
# The full way of writing out our slicing is `5:12:1` (which yields the indices `[5, 6, 7, 8, 9, 10, 11]`).
# 
# However, we could also replace the default of `1` with something else:
# 
# `5:12:2` will yield the indices `[5, 7, 9, 11]` -- every other letter.

# In[8]:


sentence[5:12:2]


# We can also increment in reverse.  But note that the second bound is still excluded, so we get slightly different behavior:
# 
# `5:12:1` yields `[5, 6, 7, 8, 9, 10, 11]`  while
# `12:5:-1` yields `[12, 11, 10, 9, 8, 7, 6]`.

# In[9]:


sentence[12:5:-1]


# #### Implicit start and stop.
# 
# The general slice syntax is `start:stop:step` which will return indices from `start` to `stop-1` incrementing by `step`.
# 
# If we are being completely explicit, slicing to get the full sequence would mean writing out: `0:len(x):1`.
# But all of these arguments are the defaults for their respective positions.
# Consequently, an equivalent statement is `0:len(x)` (as we saw above, because if `step` is omitted, Python uses the default of 1).
# Likewise, `0` is the default start argument.  Consequently `:len(x)` is equivalent.
# Furthermore, `len(x)` is the default stop argument.  So `:` is equivalent.

# In[10]:


sentence[0:len(sentence):1]


# In[11]:


sentence[:len(sentence):]


# In[12]:


sentence[0:]


# In[13]:


sentence[:]


# 
# In general it is customary to omit default arguments, so you will often see slicing like the following:
# `a[:5]`: get the first 5 elements of `a` (indices 0, 1, 2, 3, 4)
# `a[5:]`: get all the elements starting from 5 through the end.
# `a[:-3]`: get all the elements from the start until the 4th to last element.
# `a[-3:]`: get the last 3 elements

# In[14]:


sentence[:-3]


# This also means that an easy way to reverse a sequence is to just index it with a step size of -1"

# In[15]:


sentence[::-1]


# ## for loops
# 
# Given that we have a sequence, we might want to iterate through it, and do something to each element.  To accomplish this, we will use the `for` loop control structure:
# 
# `for x in iterable:
#     do stuff
#     fo more stuff
# `

# In[16]:


for letter in sentence:
    print(letter)


# What this notation is doing is generating a "loop", which iterates over all the elements in `sentence`.  On each iteration it assigns the next item from the sentence sequence to `letter`, and then executes the for loop code block (indicating by indentation).  Basically, this prints each letter in the sentence, one at a time.   But we could do a number of other things

# #### Caesar cipher
# 
# Here we will do some (really primitive) encryption with a "[Caeser cipher](https://en.wikipedia.org/wiki/Caesar_cipher)", or "shift cipher" -- basically a glorified encoder/decoder ring.  We will encrypt our sentence using a particular shift key.

# In[17]:


utf_min = 32
utf_range = 126 - utf_min
shift = 5465465

encrypted = ''

for letter in sentence:
    encrypted += chr(((ord(letter) - utf_min + shift) % utf_range) + utf_min)

print(encrypted)


# The core of this little program is the body of this for loop:
# 
# `for letter in sentence:
#     encrypted += chr(((ord(letter) - utf_min + shift) % utf_range) + utf_min)`
# 
# At an abstract level, what this is doing is, taking each letter from the string sequence `sentence` one at a time.  For each letter it:
# 
# 1. use the `ord()` command to obtain the utf-8 integer associated with that letter (see table [here](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec)).
# 1. add a constant offset (our encryption shift key) to that letter, then take the modulus of the sum to obtain an integer into one of the printable utf-8 characters (32 through 126 in that table)
# 1. use the `chr()` command to obtain the character associated with that new, shifted integer.
# 1. concatenate the new encoded character to the string `encoded` using the `+=` assignment operator.

# To really sort out how this works, let's break down that one line:
# 
# `encrypted += chr(((ord(letter) - utf_min + shift) % utf_range) + utf_min)`
# 
# The basic thing being done in this line is incrementally adding to `encrypted`:
# `encrypted += X`
# so on each iteration of the loop, we will add something to the `encrypted` string.
# 
# What will we add?  X:
# `chr(((ord(letter) - utf_min + shift) % utf_range) + utf_min)`
# which we can break apart into:
# `chr(Y)`
# so on each iteration we will add some character, specified by the integer Y.
# 
# What is that integer?
# `((ord(letter) - utf_min + shift) % utf_range) + utf_min`
# which we can break apart into more manageable chunks:
# `(Z % utf_range) + utf_min`
# we will take some other integer, calculate its modulus with respect to the range of printable utf characters, and then add an offset.  This particular pattern means that whatever integer `Z` starts off as, the particular transformation will yield an integer between 32 (`utf_min`) and 126 (`utf_min + utf_range`).
# Basically, this code is taking some integer, and via the modulus operation, projecting it onto the range of printable utf characters.
# 
# What is the integer that we project onto the range of printable utf characters?
# `ord(letter) - utf_min + shift`
# This is the integer encording of the original letter (`ord(letter)`) minus the lower bound of the printable utf range, plus an offset shift, which is our secret key.
# 
# To figure out what this code will do we have to work from the innermost execution, outward: consider the first letter of our string (`T`, when `encrypted=''`):
# `ord('T')` -> 84
# `(84 - utf_min + shift)` -> 5465517 (given our offset key of 5465465)
# `(5465517 % utf_range)` -> 75
# `75 + utf_min` -> 107
# `chr(107)` -> 'k'
# `encrypted += 'k'` ->  encrypted now = '' + 'k' (or just 'k')
# 
# We will do this for every letter, and incrementally concatenate them to the `encrypted` variable.
# 
# Below, we write this out again, but we unpack the line that'd doing all the work.  This is not very efficient (since we are creating a lot of unused variables), but it is much easier to read

# In[18]:


encrypted = ''

for letter in sentence:
    # get the utf-8 integer associated with the letter
    letter_integer = ord(letter)
    # add cipher shift (and subtract printable character min integer)
    shifted_letter_integer = letter_integer - utf_min + shift
    # rescale shifted integer to integer range corresponding to printable utf characters
    new_letter_integer = (shifted_letter_integer % utf_range) + utf_min
    # get the character representation associated with that new integer
    new_letter = chr(new_letter_integer)
    # append new letter to encrypted string
    encrypted += new_letter

print(encrypted)


# Finally, we can flip the offset sign to reverse our shift and extract the original text from the encrypted string.

# In[19]:


decrypted = ''

for letter in encrypted:
    decrypted += chr(((ord(letter) - utf_min - shift) % utf_range) + utf_min)

print(decrypted)


# ## Lists
# 
# We have dealt with strings, but a list is a more general type of sequence.  We can create a list with square brackets:

# In[20]:


x = [6, 12, 34, 22, 10]


# In[21]:


print(x)


# `x` is now a list of integers, and we can index and slice it the same way we did to a string (list of characters).

# In[22]:


x[2]


# In[23]:


x[-3:]


# ## Fibonacci variants
# 
# The fibonacci sequence starts with 0, 1, and then every subsequent number is the sum of the preceding two.  So $x_i = x_{i-1} + x_{i-2}$.  Let's write something that prints out the first 20 fibonacci sequence numbers.

# ### While loop
# 
# First, let's do this via a while loop, and no lists

# In[24]:


a, b = 0, 1
print(a, b, sep='\n')
i = 2
while(i < 20):
    a, b = b, (a+b)
    print(b)
    i += 1


# Here we have introduced two new maneuver:
# 
# `print(a,b,sep='\n')` passing multiple items to print via the comma allows us to print many variables at once.  the named `sep` argument tells Python what to print to separate the different items listed.  the string `'\n'` is a special "escape character" that means "newline".  So the command as a whole tells Python to print a, and b, and to separate them with a new line.
# 
# 
# `a,b = c,d` what this does is do multiple assignment simultaneously.  The sequence of operations Python undertakes are: evalute c, evaluate d, assign c to a and d to b.  This sequence of operations means that we can easily reassign variables, via a move like `a,b = b,a`.  Without this syntax, we would need to create a temporary variable to ensure that all information is preserved:
# `tmp = a
# a = b
# b = tmp`
# 
# Although the specific `a,b = c,d` syntax is fairly straight-forward, the algorithm as a whole might require some explanation:
# we start with a=0, b=1 -- the first two items of the sequence.
# the line `a, b = b, (a+b)` does three things simultaneously:
# - calculates the next item in the sequence `(a+b)`,
# - assigns the previous value of `b` to `a`,
# - assigns the next item in the sequence to `b`.
# thus, on the first pass through the body of the while loop, we end up with a=1, b=1.
# On the second pass, we end up with a=1, b=2.
# 
# After each pass, the current item in the sequence is stored in the variable `b`.
# 

# ### for loop, lists
# 
# now, let's do this using a for loop, and construct a list of the first 20 numbers.

# In[25]:


fib = [0, 1]

for idx in range(2, 20):
    fib += [ fib[idx-2] + fib[idx-1] ]

print(fib)


# Here we have introduced a few new maneuvers:
# 
# `range(start, stop, step)` creates an iterable sequence of numbers, and works just like the slice notation we had previously used.   So the very common command `for i in range(start,stop):` iterates for all values of idx from `start` to `stop-1`.
# 
# `list1 += list2` appends list2 to list1, so that if list1=[1, 2, 3], and list2=[4, 5, 6], after the line shown list1 will be [1, 2, 3, 4, 5, 6].  In our case, we calculate the current list item by summing the two prior list items, and then we append that item to the list.
# 
# 
# 
# ## While loops
# 
# The next control structure we ought to master is the `while` loop.  A while loop is a block of code with a condition, and that block of code is executed over and over and over again  so long as the condition is satisfied.  While loops create an opportunity for an infinite loop.  If you are using a while loop and your code is running for a long time, try to think through when you expect the while condition to turn false, and why it may not be doing so.

# In[26]:


x = 0

while x < 10:
    print(x)
    x = x + 1


# **Note** here we are using the `+=` assignment operator, which is a convenient shorthand.  `A += B` is equivalent to writing `A = A + B`.  Because this kind of operation -- increment the value of a variable, and assign it back to the variable -- is so common, python has a whole bunch of similar shortcut operators: `+=`, `-=`, `*=`, `/=`, `**=`, `%=`.

# 
