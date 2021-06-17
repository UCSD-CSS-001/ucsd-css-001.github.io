#!/usr/bin/env python
# coding: utf-8

# # CSS 1. L02: Control, logic
# 
# Computer programs can be very powerful once we can command their flow of execution.  This is done via assorted control structures.

# ## Control: if..else
# 
# The basic control structure allows branching: do something only if a condition is met.

# In[1]:


polite = False

if polite:
    print("hello!")
    print("it is a pleasure to meet you!")

print("My name is Ed")


# What this code is doing is:
# - set the variable `polite` to the boolean value True
# - if statement checks if the expression (`polite`) evaluates to True  
# - if `polite` is True then it runs the code block (indicated by indentation) comparised of two print statements; if `polite` is not true (i.e., False) then it does not run those two print statements.     
# - execution then moves on to the next line outside of the `if` block
# 
# ### Code blocks
# 
# Note that here we are creating a code block via indentation.  We would get different results with different indentation.  Below, the indentation indicates that the second print statement is *outside* of the if block, and it will be run regardless of whether greet is true or false.

# In[2]:


polite = False

if polite:
    print("hello!")
print("it is a pleasure to meet you!")

print("My name is Ed")


# ### else
# 
# If we wanted to print one thing if `polite` is true, and a different thing if `polite` is false, when we would want to set up an `else` block:

# In[3]:


polite = False

if polite:
    print("hello!")
else:
    print("hey.")

print("My name is Ed")


# ### elif
# 
# Sometimes we want to have more than two branches, so we would want a control structure that can accomodate that:

# In[4]:


verbose = True
polite = True

if verbose:
    print('Good day to you!')
elif polite:
    print('Hello!')
else:
    print('hey.')
    
print('My name is Ed')
    


# Note that execution of the `if..elif..else` statement takes the first available branch, and then does not execute the other branches.  Here, `verbose` evaluated to True, so the first branch was taken (and no other branches were, even though `polite` also evaluated to true).  Thus an `if..elif..else` block sets up a mutually exclusive branching structure.
# 
# This is contrasted with a series of independent `if` statements, that each presents an optional branch, independent of the others.

# ### if..elif vs if..if..
# 
# Consider the two blocks of code below.  What will each print?

# In[5]:


A = True
B = True
C = False


# In[6]:


if A:
    print('A is true')
elif B:
    print('B is true')
elif C:
    print('C is true')


# In[7]:


if A:
    print('A is true')
if B:
    print('B is true')
if C:
    print('C is true')


# Note also that an else statement is attached to exactly one if..elif.. statement.  So what will the code below do?

# In[8]:


if A:
    print('A is true')
if B:
    print('B is true')
if C:
    print('C is true')
else:
    print('nothing is true')


# ## Comparison operators
# 
# So far we have written if..else statements to evaluate based on pre-defined boolean variables, but a much more common scenario is to compare values, and define new boolean variables that way.  To this end, Python has a number of comparison operators:
# 
# `A == B`: returns True if A and B are equal   
# `A != B`: returns True if A and B are not equal   
# `A < B` (or  `A > B`): return True is A is less than B (or greater than B)   
# `A <= B` (or `A >= B`): return True is A is less than or equal to B (or greater than or equal to B)    

# In[9]:


5 == 5.0


# In[10]:


5 != 5.0


# In[11]:


5 > 5


# In[12]:


5 >= 5


# ### Comparison operators on strings
# 
# Comparison operators are also overloaded for strings.  Equality is case sensitive, and greater/less than correspond to ascii alphabetical order. 

# In[13]:


'abracadabra' == 'abracadabra'


# In[14]:


'Abracadabra' == 'abracadabra'


# In[15]:


'a' > 'b'


# In[16]:


'a' < 'b'


# **Case and ascii**   However, note that behavior for lower/uppercase letters and symbols may be unintuitive. 

# In[17]:


'A' < 'a'


# In[18]:


'Z' < 'a'


# In[19]:


'[' < 'a' 


# In[20]:


'Z' < '['


# Comparison of characters is underpinned by comparing the [UTF-8 integer code of each character](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec).  Which can be obtained for a given character via the `ord()` function.

# In[21]:


ord('a')


# ## Logical operators
# 
# While obtaining a single boolean value can solve some problems, often we want to specify a more complicated logical expression by combining boolean values from many comparisons.  
# 
# For instance, if we want to see if someone's age (in years) is an odd number and greater than 20, we are looking for a conjunction of two comparisons.
# 
# These kinds of boolean operations can be done with 
# 
# `A and B`: returns True if both A and B are true.    
# `A or B`: returns True if either A or B are true.    
# `not A`: returns True if A is False.   

# In[22]:


age = 37

if (age % 2) == 1 and age > 20:
    print('age is odd and greater than 20')


# **Note 1**: Here we are using the `%` "modulus" operator.  `A % B` returns the remainder after dividing A by B (and taking only a whole quotient).    
# e.g., `17 % 3` returns 2.  The closest multiple of 3 closest to, but smaller than, 17 is $3 \cdot 5 = 15$, and 17-15 = 2).    
# e.g., `15 % 3` will return 0.    
# We have to be careful with negative numbers: (`-17 % 3` = 1 because $3 \cdot -6 = -18$ is the closest multiple of 3 less than -17.   
# Even weirder things happen with negative divisors: `17 % -3 = -1` because the smallest quotient that is closest to 17 is -6 ($-3 \cdot -6 = 18$).  Generally, I try to avoid negative divisors in the modulus operator, as that always creates confusion and I have never seen it be worthwhile.
# 
# **Note 2** What will happen if `age=37.6`?  What *should* happen in that case?

# ## While loops
# 
# The next control structure we ought to master is the `while` loop.  A while loop is a block of code with a condition, and that block of code is executed over and over and over again  so long as the condition is satisfied.  While loops create an opportunity for an infinite loop.  If you are using a while loop and your code is running for a long time.

# In[23]:


x = 0

while x < 10:
    print(x)
    x += 1


# **Note** here we are using the `+=` assignment operator, which is a convenient shorthand.  `A += B` is equivalent to writing `A = A + B`.  Because this kind of operation -- increment the value of a variable, and assign it back to the variable -- is so common, python has a whole bunch of similar shortcut operators: `+=`, `-=`, `*=`, `/=`, `**=`, `%=`.

# ### Fizz Buzz
# 
# A very simple programming challenge is to implement the kids game ["Fizz Buzz"](https://en.wikipedia.org/wiki/Fizz_buzz).  Count from 1 to 100.  For each number, if it is divizible by 3 print "Fizz", if it is divisible by 5 print "Buzz", (thus print "Fizz Buzz" for numbers divisible by 15).  For all other numbers, just print that number.

# In[24]:


x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1


# ## Sequences and indexing
# 
# We have seen string types before, but strings are a special kind of "sequence" data type.  Specifically, a string is a sequence of characters.  Sequences are a list of many objects of the same type.

# In[25]:


sentence = 'This is a sentence about string sequences!'


# The string stored in `sentence` is represented as a sequence of characters.  We can get the *length* of that sequence using the `len()` function:

# In[26]:


len(sentence)


# ### Indexing
# 
# We can pull out elements of that sequence by indexing and slicing.  
# Python has 0-indexed lists, which means that the first element has the index of 0, and the last element has an index of `len(x)-1`

# In[27]:


sentence[0]


# We can pull out any letter by referring to its index.  For instance, the 6th letter of the string ('i' in 'is') has the index 5:

# In[28]:


sentence[5]


# The last element of the sequence has an index of `len(x)-1`:

# In[29]:


sentence[len(sentence)-1]


# But we can also refer to it with the helpful shortcut of `-1`.  In general, we can refer to elements by indexing from the beginning (starting with 0), or indexing from the end, starting with -1.  

# In[30]:


sentence[-1]


# ### Slicing
# 
# We often want to pull out multiple elements of a sequence, for instance, maybe we want all the characters between the 6th ('i') and 12th (first 'e' in 'sentence').  We can do this with the slicing notation `5:12`.

# In[31]:


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

# In[32]:


sentence[5:12:2]


# We can also increment in reverse.  But note that the second bound is still excluded, so we get slightly different behavior:
# 
# `5:12:1` yields `[5, 6, 7, 8, 9, 10, 11]`  while   
# `12:5:-1` yields `[12, 11, 10, 9, 8, 7, 6]`.

# In[33]:


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

# In[34]:


sentence[0:len(sentence):1]


# In[35]:


sentence[:len(sentence):]


# In[36]:


sentence[0:]


# In[37]:


sentence[:]


# 
# In general it is customary to omit default arguments, so you will often see slicing like the following: 
# `a[:5]`: get the first 5 elements of `a` (indices 0, 1, 2, 3, 4)   
# `a[5:]`: get all the elements starting from 5 through the end.   
# `a[:-3]`: get all the elements from the start until the 4th to last element.   
# `a[-3:]`: get the last 3 elements

# In[38]:


sentence[:-3]


# This also means that an easy way to reverse a sequence is to just index it with a step size of -1"

# In[39]:


sentence[::-1]


# ## for loops
# 
# Given that we have a sequence, we might want to iterate through it, and do something to each element.  To accomplish this, we will use the `for` loop control structure:
# 
# `for x in iterable:
#     do stuff
#     fo more stuff
# `

# In[40]:


for letter in sentence:
    print(letter)


# What this notation is doing is generating a "loop", which iterates over all the elements in `sentence`.  On each iteration it assigns the next item from the sentence sequence to `letter`, and then executes the for loop code block (indicating by indentation).  Basically, this prints each letter in the sentence, one at a time.   But we could do a number of other things

# #### Caesar cipher
# 
# Here we will do some (really primitive) encryption with a "[Caeser cipher](https://en.wikipedia.org/wiki/Caesar_cipher)", or "shift cipher" -- basically a glorified encoder/decoder ring.  We will encrypt our sentence using a particular shift key.  

# In[41]:


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

# In[42]:


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

# In[43]:


decrypted = ''

for letter in encrypted:
    decrypted += chr(((ord(letter) - utf_min - shift) % utf_range) + utf_min)
    
print(decrypted)


# ## Lists
# 
# We have dealt with strings, but a list is a more general type of sequence.  We can create a list with square brackets:

# In[44]:


x = [6, 12, 34, 22, 10]


# In[45]:


print(x)


# `x` is now a list of integers, and we can index and slice it the same way we did to a string (list of characters).

# In[46]:


x[2]


# In[47]:


x[-3:]


# ## Fibonacci variants
# 
# The fibonacci sequence starts with 0, 1, and then every subsequent number is the sum of the preceding two.  So $x_i = x_{i-1} + x_{i-2}$.  Let's write something that prints out the first 20 fibonacci sequence numbers.

# ### While loop
# 
# First, let's do this via a while loop, and no lists

# In[48]:


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

# In[49]:


fib = [0, 1]

for idx in range(2, 20):
    fib += [ fib[idx-2] + fib[idx-1] ]
    
print(fib)


# Here we have introduced a few new maneuvers:
# 
# `range(start, stop, step)` creates an iterable sequence of numbers, and works just like the slice notation we had previously used.   So the very common command `for i in range(start,stop):` iterates for all values of idx from `start` to `stop-1`.
# 
# `list1 += list2` appends list2 to list1, so that if list1=[1, 2, 3], and list2=[4, 5, 6], after the line shown list1 will be [1, 2, 3, 4, 5, 6].  In our case, we calculate the current list item by summing the two prior list items, and then we append that item to the list.
