#!/usr/bin/env python
# coding: utf-8

# # P02: Control flow and logic
# 
# Computer programs become very powerful once we can command their flow of execution.  This is done via two primary control structures:
# 
# - Conditionals (`if...elif...else`) statements that allow the program execution to *branch*, and
# - Loops (`for` and `while`) that allow the program execution to *repeat*.

# ## Conditional Control: if..else
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
#     - if `polite` is True then it runs the code block (indicated by indentation) comprised of two print statements;
#     - if `polite` is not true (i.e., False) then it does not run those two print statements.
# - execution then moves on to the next line outside of the `if` block (the 3rd print statement)
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
    


# 
# Note that execution of the `if..elif..else` statement takes the first available branch, and then does not execute the other branches.  Here, `verbose` evaluated to True, so the first branch was taken and no other branches were (even though `polite` also evaluated to true).  Thus an `if..elif..else` block sets up a mutually exclusive branching structure.
# 
# We can have as many `elif` after an `if` as we see fit, but it only makes sense to have one `else`.  (Note that an `else:` is logically equivalent to `elif True:`)
# 

# ### if..elif vs if..if..
# 
# The mutually exclusive branching structure of `if..elif` is contrasted with a series of independent `if` statements, that each presents an optional branch, independent of the others.
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
    print('neither A nor B nor C are true')


# Note that what the code above *prints* deviates from reality!  The code runs just fine, but it will print "neither A nor B nor C are true" even when A or B are true!  This is the trickiest sort of bug to fix, because the computer does not know that anything is wrong, so it cheerfully does the incorrect thing.
# 
# How would we fix the code above to do work correctly?
# 
# ## Logical operators
# 
# While working with a single boolean value can solve some problems, often we want to specify a more complicated logical expression by combining boolean values from many comparisons.  For instance, to make the code above work, we need to figure out if A, B, and C are all False.
# 
# These kinds of boolean operations can be done with
# 
# `A and B`: returns True if both A and B are true.
# `A or B`: returns True if either A or B are true.
# `not A`: returns True if A is False.

# In[9]:


if A:
    print('A is true')
if B:
    print('B is true')
if C:
    print('C is true')
if not A and not B and not C:
    # alternatively:  not (A or B or C)
    print('neither A nor B nor C are true')


# ## Comparison operators
# 
# So far we have written if..else statements to evaluate based on pre-defined boolean variables, but a much more common scenario is to compare values, and define new boolean variables that way.  To this end, Python has a number of comparison operators:
# 
# `A == B`: returns True if A and B are equal   
# `A != B`: returns True if A and B are not equal   
# `A < B` (or  `A > B`): return True is A is less than B (or greater than B)   
# `A <= B` (or `A >= B`): return True is A is less than or equal to B (or greater than or equal to B)    

# In[10]:


5 == 5.0


# In[11]:


5 != 5.0


# In[12]:


5 > 5


# In[13]:


5 >= 5


# ### Comparison operators on strings
# 
# Comparison operators are also overloaded for strings.  Equality is case sensitive, and greater/less than correspond to unicode character index order.

# In[14]:


'abracadabra' == 'abracadabra'


# In[15]:


'Abracadabra' == 'abracadabra'


# In[16]:


'a' > 'b'


# In[17]:


'a' < 'b'


# **Case and unicode character index**   However, note that behavior for lower/uppercase letters and symbols may be unintuitive.

# In[18]:


'A' < 'a'


# In[19]:


'Z' < 'a'


# In[20]:


'[' < 'a' 


# In[21]:


'Z' < '['


# Comparison of characters is underpinned by comparing the [UTF-8 integer code of each character](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec).  Which can be obtained for a given character via the `ord()` function.

# In[22]:


ord('a')


# ## Logical operators
# 
# Let's combine comparisons and logical operators.  Let's say we want to see if someone's age (in years) is an odd number and greater than 20, we are looking for a conjunction of two comparisons.
# 
# These kinds of boolean operations can be done with 
# 
# `A and B`: returns True if both A and B are true.    
# `A or B`: returns True if either A or B are true.    
# `not A`: returns True if A is False.   

# In[23]:


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
# 

# # Conditionals
# 
# - `if`
# - `elif`
# - `else`

# ## Conditionals: `if`

# <div class="alert alert-success">
# Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
# </div>

# In[24]:


condition = True

if condition:
    print('This code executes if the condition evaluates as True.')


# In[25]:


# equivalent to above
if condition == True:
    print('This code executes if the condition evaluates as True.')


# #### Clicker Question #1
# 
# Replace `---` below with something that will print 'True'
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start

# In[26]:


math = 3 > 2

if math:
    print('True')


# ## Conditional: `else`

# <div class="alert alert-success">
# After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
# </div>

# In[27]:


condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else:
    print('This code executes if the condition evaluates as False')


# #### Clicker Question #2
# 
# Replace `---` below with something that will print 'False'.
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start

# In[28]:


my_value = 19 <= 10

if my_value:
    print('True')
else:
    print('False')


# ## Conditional: `elif`

# <div class="alert alert-success">
# After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
# </div>

# In[29]:


condition_1 = False
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else:
    print('This code executes if both condition_1 and condition_2 evaluate as False')


# ### `elif` without an `else`
# 
# An else statement is not required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.

# In[30]:


condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ### `elif` *after* an `else` does not make sense
# 
# The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

# In[31]:


## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else:
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ## Conditionals With Value Comparisons

# <div class="alert alert-success">
# Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
# </div>

# In[ ]:


language = "Perl"

if language == "Python" or language == "R":
    print("Yay!")
elif language == "Perl":
    print("Hmmmmmmm")
else:
    print("Get yourself a programming language!")


# In[ ]:


# Exploring conditionals
number = 4

print('Before Conditional')

if number < 5:
    print('    if statement execution')
elif number > 5:
    print('    elif statement execution')

print('After Conditional')


# #### Clicker Question #3
# 
# What will the following code snippet print out:

# In[ ]:


condition = False

if condition:
    print("John")
elif not condition:
    print("Paul")
elif not condition:
    print("George")
else:
    print("Ringo")


# - A) John
# - B) Paul, George, Ringo
# - C) Paul
# - D) Paul, George
# - E) Ringo

# #### Clicker Question #4
# 
# What will the following code snippet print out:

# In[ ]:


if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")


# - A) I did Math
# - B) I broke Math
# - C) I didn't do math
# - D) This code won't execute

# #### Clicker Question #5
# 
# What will the following code snippet print out:

# In[ ]:


conditional = False
python = "great"

if conditional:
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")


# - A) Yay Python!
# - B) Oh no.
# - C) I'm here.
# - D) This code won't execute

# ## Properties of conditionals
# 
# - All conditionals start with an `if`, can have an optional and variable number of `elif`'s and an optional `else` statement
# - Conditionals can take any expression that can be evaluated as `True` or `False`.
# - At most one component (`if` / `elif` / `else`) of a conditional will run
# - The order of conditional blocks is always `if` then `elif`(s) then `else`
# - Code is only ever executed if the condition is met
