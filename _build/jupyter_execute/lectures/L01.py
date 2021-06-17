#!/usr/bin/env python
# coding: utf-8

# # CSS 1: L01 - Crash course
# 
# ## Jupyter Notebooks
# 
# This is a jupyter notebook.  A notebook is file that combines explanatory text (written in markdown), computer code, and the output of the computer code.  
# 
# A notebook is comprised of "cells".  A given cell can contain different types of things.  We will concern ourselves with cells that contain either markdown (like this cell), or python code.  

# ### Markdown Cells
# 
# Markdown is a way of specifying text formatting in plain text.   
# For instance, this cell starts with the text `### Markdown` which tells the computer that it should display a level 3 heading with the text "Markdown".  The cell above starts with the text `# CSS 1:...` which specifies a level 1 heading, which you can see is rendered in larger text.
# 
# Some other common markdown formatting syntax:   
# 
# #### paragraphs and linebreaks
# 
# Markdown ignores single line breaks. For instance, the following markdown is rendered on one line:
# 
# ```markdown
# The text here
# is 
# formatted
# like so.
# ```
# 
# The text here
# is 
# formatted
# like so.
# 
# To create linebreaks you can either add two linebreaks between each line, like so:
# 
# 
# ```
# The text here
# 
# is 
# formatted
# like so.
# ```
# 
# The text here
# 
# is 
# formatted
# like so.
# 
# 
# Or you could add two spaces to the end of each line:
# 
# ```
# The text here  
# is   
# formatted   
# like so.  
# ```
# 
# The text here  
# is   
# formatted   
# like so.  
# 
# 
# 
# #### text formatting
# 
# `*text*` yields italics: *text*   
# `**text**` yields bold: **text**   
# ``` `text` ``` yields a code formatting: `text`
# 
# 
# #### links
# 
# `[text](URI)` yields a link.  For instance `[pydocs](https://docs.python.org/3/)` yields a link to python docs: [pydocs](https://docs.python.org/3/)
# 
# #### lists
# 
# ```
# - item 1  
# - item 2
# ```
# 
# yields a bulleted list:
# - item 1   
# - item 2
# 
# ```
# 1. item 1  
# 1. item 2
# ```
# 
# yields an automatically numbered list:
# 
# 1. item 1  
# 1. item 2
# 
# 

# ### Code cells
# 
# The virtue of jupyter notebooks is that you can mix explanatory text with computer code, and the results of running that code.  We will be using these notebooks with Python code.  Python code will run in special kinds of cells called code cells.
# 
# A given code cell has some content, which is sent to a Python interpreter.  Upon executing that code, the cell prints some output.  The output may be more or less complicated.  Without any particular instructions about what to output, the code cell will output whatever the last line "returns"

# In[1]:


34


# #### Magics 
# 
# We will spend most of our time worrying about how to write code that goes inside code cells, but it is worth noting that code cells can also contain special commands called "line magics" or "cell magics" which do something, but are not part of the python language itself.  These commands occur on lines starting with `%` or `%%`.  We will cover them as needed, but for now, here is an example:   
# 
# `%lsmagic` will list all the line and cell magics that are available.

# In[2]:


get_ipython().run_line_magic('lsmagic', '')


# ### Notebook navigation
# 
# Notebooks are "modal" in the sense that you can be in different modes.  If you are in "edit" mode, you are editing the content of a given cell.  If you are in "command" mode then you might create new cells, change their type, rearrange them, etc.
# 
# You can enter command mode by hitting "escape".  Then you can navigate with the arrow keys, or by clicking on particular cells.  
# 
# You can enter "edit" mode in a given cell by pressing the "enter/return" key.  
# 
# When in edit mode, you can press "Shift + enter" (hold down the shift key and press enter) to execute the cell, and exit edit mode.
# 
# In command mode, you can press "H" to see a list of keyboard shortcuts, or you can press "cmd + shift + f" to enter the command pallette, where you can search for all the commands available to you.
# 
# There is a lot of extended functionality to notebook navigation and execution, but that covers the basics.

# ### Kernel
# 
# A notebook is edited in a browser, but it "talks" to a "kernel" that is being run on some server.  The Kernel is a running session of (in our case) Python.  When we run a code cell in the notebook, the code from that cell is sent to the running Python kernel, which executes that code, and then sends the output back to the notebook.  The notebook then embeds that output below the code cell.
# 
# This arrangement is rather complicated.  It has a number of benefits and a number of costs.
# 
# The benefits: The output has to be run once, and is then embedded in the notebook, and can be viewed without rerunning the code.  The code can be embedded in a document such as this one, with text, explanations, output, etc.  The kernel can be run on various remote servers, while you access the notebook through your own browser, so you do not have to set up your own python environment on your own computer, and so you can easily plug into a kernel running on a server more powerful than your own computer.
# 
# There are costs however: Code cells can be executed out of order, and the state of the kernel is changed by each cell that is run.  This can cause quite a bit of confusion.   A notebook is a complicated file, and you can't just look at it in a text editor, as you could would just code on its own. 

# ## Python Syntax
# 
# The core of what we must learn to do is write Python code.  Python is a programming language.  Unlikely human languages, programming languages have a very strict syntax.  One virtue of this is that code written in a programming language is unambiguous -- there is only one way that Python can interpret that code.  The downside is that our intuitions from speaking human language fail us when faced with a very strict syntax, semantics, vocabulary, etc.

# ### Comments
# 

# In[3]:


# a line of code starting with the # character is a comment.  
# The python interpreter ignores it.  
# Consequently, this code cell does nothing.


# ### Literals
# 
# Some kinds of things that we can type into the Python interepreter are interpreted literally.  For instance, a number is interpreted as a number literal, and some characters inside quotes are interpreted as a string literal.

# In[4]:


34


# In[5]:


'abc'


# ### Names
# 
# Without quotes, `abc` is interpreted by Python to be a reference to an object in memory.  When no object in memory has such a name, we get a `NameError`.

# In[6]:


abc


# ### Errors
# 
# An exception is an error -- it means that the Python interpreter cannot do what you have told it to do.  There are many different kinds of exceptions you will encounter, and the specific type of exception tells you something about what is wrong with your code.
# 
# The most dire sort of error is a SyntaxError: it means that Python does not know how to parse the instructions at all.
# 
# Then there is a long list of logical errors which raise "Exceptions" that may be 'caught' (we will deal with that later).

# In[7]:


3 +


# In[8]:


abc


# In[9]:


'3' + 4


# Note that for strings, the quotes have to be closed, and must match.  `'abc'` is an acceptable string literal.  `"abc"` is also an acceptable string literal.  `'abc"`, `"abc'`, `'abc`, `"abc` are all syntax errors because Python cannot figure out where the string started by the first quote is supposed to end:

# In[10]:


'abc'


# In[11]:


"abc"


# In[12]:


'abc"


# In[13]:


"abc'


# In[14]:


'abc


# In[15]:


"abc


# ### functions
# 
# We will talk much more about functions when we start writing them ourselves, but for now, we just need to know that functions are stored procedures, which we can call by invoking their name, and passing some arguments to them:  `functionname(argument)`

# In[16]:


print('hello!')
print('with the print function, we can print many lines in one cell!')


# ### White space
# 
# Python treats white space (i.e., spaces, tabs, etc.) as meaningful.  Some puzzling syntax errors might arise from impropertly indenting code.  

# In[17]:


print('hello')
   print('with the print function...')


# Other syntax errors might arise from mixing spaces and tabs.  We will talk more about indenting in the context of code blocks.  For now, just be aware that blank spaces are meaningful to the Python interpreter.  
# 
# Even though they just look like space to you, they are a meaningful character to the python interpreter.  It might make sense if you visualize what the interpreter sees -- the white space is shown to us as a blank, but the computer encodes it with characters, like any other character.
# 
# `
# print('hello')
# ␣␣␣print('with the print function...')
# `

# ## Python types, operators
# 
# Computer programs do stuff to data.  The data has to somehow be represented in the computer.  Ultimately, all the data is represented in binary in computer memory, but we generally don't have to deal with the binary ourselves, we deal with more abstracted data representations.  However, Python needs to know what kind of data it is dealing with, to determine what to do with the relevant binary information.  Thus, data are encoded in some kind of data type, and the *data type* is of utmost importance to how Python will interpret our commands.  There are many different types of data and data structures in Python.  Today we will deal with the basics: integers, floating point numbers, strings, and boolean values.
# 
# ### type()
# 
# the `type()` function takes some argument, and returns the data type of the object referenced by that argument.  If we pass in a literal, it will tell us the literal's type.

# In[18]:


type('34')


# In[19]:


type(34.0)


# In[20]:


type(34)


# In[21]:


type(True)


# The basic data types we have encountered so far are 
# - `str`: strings, which are sequences of characters -- text. (more in a bit)    
# - `int`: integers, which are whole (integer) numbers.
# - `float`: floating point numbers, which are numbers that have decimals.   
# - `bool`: boolean / binary values, used for all logical operations: either `True`, or `False`.

# ### Operators
# 
# Operators are special symbols that take some arguments, do something to them, and return some value.  The basic binary (meaning they take two values) arithmetic operators are very familiar, when applied to numbers:

# In[22]:


3 + 4


# In[23]:


3 - 4


# In[24]:


3 * 4


# In[25]:


3 / 4


# In[26]:


3 ** 4


# Note, that last one might be a bit surprising.  the `**` operator corresponds to exponentiation, so `3 ** 4` calculates $3^4$ (i.e., $3 * 3 * 3 *3$)

# ### Operator precedence
# 
# As in basic arithmetic, operators have precedence: some of them are executed first, and parentheses can be used to group operations to set a precedence order.

# In[27]:


14 - 3 * 2


# In[28]:


(14 - 3) * 2


# ### Operators and types
# 
# As we saw, a given literal has a type, and what it means to apply a given operation to a particular entity depends on its type.
# 
# For instance, some operations don't make any sense for certain types:

# In[29]:


'css ' * 'class'


# The cell above yields a `TypeError` because Python does not have a defined operation corresponding to `*` for two strings.  That makes sense -- after all, what do you think such an operation could mean?
# 
# Some confusion may arise because, sometimes, the operation might look meaningful to us, but not to Python, because Python does not interpret code the same way we do.  For instance `'3' * '4'` makes sense to us, but not to Python.  The reason is that Python knows that `'3'` and `'4'` are strings, the fact that those strings *could* be interpreted as numbers is irrelevant for the Python interpreter.  At the level of data types, `'3'` and `'4'` are no different from a string like `'css'`.  All it knows is that you have asked it to apply `*` to two strings, and it does not think that is a valid operation.

# In[30]:


'3' * '4'


# ### Type casting
# 
# When we see `'3' * '4'` we are implicitly converting ("casting") the strings into integers.  We need to do so explicitly for python to understand.  Which we can do by explicitly telling Python to convert those strings to integers.

# In[ ]:


int('3') * int('4')


# Of course, some strings cannot be converted to integers, what would it even mean?

# In[ ]:


int('css')


# Some types of converstion might make sense to us, but Python does not understand them:

# In[31]:


int('three')


# In short, if we are trying to convert a string to an `int` (or a `float`), then the string ought to be interpretable as an integer or a float if we were to just provide it to Python directly without quotes.  Otherwise, Python will not know how to convert it, and will throw a `ValueError` exception

# ### Overloaded operators
# 
# Many operators can work for different types, but they do different things depending on what the types are.  For instance consider `+`:
# - `int + int -> int`: for two integers, `+` takes their sum, and returns it as an integer.  
# - `float + float -> float`: for two floating point numbers, `+` takes their sum and returns another floating point number.  
# - `float + int -> float`: for a floating point number and an integer, `+` takes their sum and returns a floating point number.   
# 
# These are mostly obvious: `+` applied to two numbers returns their sum.  Slightly less obvious is what number data type it returns: for two integers it returns another integer, but if a float is involved, it will return a float.

# In[32]:


3 + 3


# In[33]:


3.0 + 3.0


# In[34]:


3 + 3.0


# Less intuitively, `+` can also be applied to two strings:
# 
# - `str + str -> str`: when applied to two strings, `+` returns the concatenation of the two strings.

# In[35]:


'3' + '3'


# Some combinations of types, however, do not work with `+`:  `str + int` will return a TypeError.

# In[36]:


'3' + 3


# Here is another surprising operator type combination that works:
# 
# - `str * int -> str`: a string `*` an integer `n` returns that string, repeated `n` times.  (this also works for other sequences, which we will see later)
# 
# This has a certain logic to it: if we think of multiplication as repeated addition, and addition of strings is concatenation, then multiplication of strings would be repeated concatenation.

# In[37]:


'a' * 5


# In[38]:


2 * 'hip ' + 'hooray'


# In[39]:


'a' * 5.0


# The combination of type casting, and operator overloading yields some potentially puzzling behavior.  
# 
# consider what the lines below will return:  
# - `str(3) + str(4)`   
# - `str(3) + 4`  
# - `int('3') * 4`  
# - `int('3') * str(4)`    
# etc. 

# ## Python: variables, execution
# 
# ### Variables
# 
# We will need to store things in memory.  To do so, we will use variables.  A variable is a name that we can assign to an object, and refer to that object later.
# 

# In[ ]:


greeting = 'Hello!  This is a long string describing how we greet you!'

print(greeting)


# By assigning values to variables, we can use them many times.

# In[40]:


radius = 4
pi = 3.14159

print('area: ', pi * radius ** 2)
print('circumference: ', 2 * pi * radius)


# ### Sequential execution
# 
# Within a given code block, instructions are executed in a particular sequence, and future instructions (such as changing the value of a variable) do not change the calculations (and assignments) from prior instructions:

# In[41]:


a = 3
b = 4
x = a * b
a = 5
print(x)
print(a*b)


# ## Reading code
# 
# When **reading** code, it is important that you consider not just what the lines are telling the computer to do, but what the *state* of the program in memory is at the moment that the computer follows those instructions.
# 
# For instance, to think through what the code above is doing, let's step through it.  Starting with the memory state before the first line is even evaluated.
# 
# *memory state:* `{}` (blank, other than built in stuff)
# 
# `a = 3`: assign value 3 to variable named `a`
# 
# *memory state:* `{'a': 3}`
# 
# `b = 4`: assign value 4 to variable named `b`
# 
# *memory state:* `{'a':3, 'b':4}`   
# 
# `x = a * b`: `a` evaluated to `3` (`x = 3 * b`), `b` evaluated to `4` (`x = 3 * 4`), `*` applied to `3` and `4` to yield `12` (`x = 12`), `12` is assigned to `x`.
# 
# *memory state:* `{'a':3, 'b':4, 'x':12}`   
# 
# `a = 5`: assign value 5 to variable named `a`   
# 
# *memory state:* `{'a':5, 'b':4, 'x':12}`   
# 
# `print(x)`: `x` evaluated to `12` (`print(12)`), `print()` prints `12`
# 
# *memory state:* `{'a':5, 'b':4, 'x':12}`   
# 
# `print(a*b)`: `a` evaluated to `5` (`print(5*b)`), `b` evaluated to `4` (`print(5*4)`), `*` applied to `5` and `4` to yield `20` (`print(20)`), `print()` prints `20`
# 
# *memory state:* `{'a':5, 'b':4, 'x':12}`   
# 
# 
# When dealing with more complicated programs and algorithms, it is sometimes very helpful to do this with paper and pencil, to make sure you can think through what each line is doing to the memory state. 

# ### Notebooks, cells, and memory state.
# 
# Important Note: This kind of logic for stepping through code works great when considering stand alone scripts.  Notebooks, however, are pretty tricky, because each cell runs code in the same environment, so the memory state at the start of the cell is determined by which cells had been run previously.  Cells *could* be run out of order.  This presents a great deal of opportunity for confusion.  Make sure that you can run your whole notebook from start to finish, in the order it is written!

# In[42]:


print(x) # note that x is still in memory, even though it was not defined in this cell!


# In jupyter notebooks, you can use the 'line magic' commands `%who` to see a list of currently declared variables in memory, and `%whos` to also see their values.

# In[43]:


get_ipython().run_line_magic('who', '')


# In[44]:


get_ipython().run_line_magic('whos', '')


# ### Print debugging
# 
# The most generic (and arguably most powerful) way to figure out why a program is not doing what you want it to do (i.e., to "debug" a program) is to insert `print()` statements into the code, to ask the program to print out the current values of various variables in memory.  Often this will reveal that variables do not have the values you expected, and you can figure out at what point in the program your expectations diverge from what the code is actually doing.