#!/usr/bin/env python
# coding: utf-8

# # P01:  Python syntax, variables, types
# 
# ## Python Syntax
# 
# Python is a programming language.  Unlike human languages, programming languages have a very strict syntax.  One virtue of this is that code written in a programming language is unambiguous -- there is only one way that Python can interpret that code.  The downside is that our intuitions from speaking human language fail us when faced with a very strict syntax, semantics, vocabulary, etc.

# ### Comments
# 

# In[1]:


# a line of code starting with the # character is a comment.
# The python interpreter ignores it.
# Consequently, this code cell does nothing.


# ### Expressions
# 
# Anything in a block of code that is not a comment, Python reads from top to bottom, and treats as an **expression**.  Python tries to parse it (into sub-expressions), and then tries to **evaluate** those expressions.
# 
# As an example

# In[2]:


x = 34
print(x)


# Python reads the `x = 34` line first.  It parses this into a binary operator expression: `exp op exp` with the assignment operator:  `exp_1 = exp_2`. The right hand expression is the name `x`, and the left hand expression is the literal `34`.  Python evaluates the literal `34` which returns the integer 34; that value is then assigned to the variable named `x`.
# 
# The next line is parsed as a call expression.  The `print()` function is called on a sub-expression.  That sub-expression contains the name `x`.  Python evaluates `x` to obtain the integer 34.  And that is passed to the print() function.  The print function calls a particular method in the integer object to obtain its string representation, and then prints that representation.
# 
# This is all a bit fast and loose, but the parts that are worth remembering:
# - Python has to parse the code you type

# ### Literals
# 
# Some kinds of things that we can type into the Python interepreter are interpreted literally.  For instance, a number is interpreted as a number literal, and some characters inside quotes are interpreted as a string literal, the word True (and False) are interpreted as Boolean literals.

# In[3]:


34


# In[4]:


'abc'


# In[5]:


True


# ### Names
# 
# Without quotes, `abc` is interpreted by Python to be a reference to an object in memory.  When no object in memory has such a name, we get a `NameError`.

# In[6]:


abc


# ### Errors and Exceptions
# 
# As you write code, you will encounter problems of various sorts: syntax error and exceptions.
# 
# Problems of these sorts mean that the Python interpreter cannot do what you have
# told it to do.  There are many different kinds of exceptions you will encounter, and the specific type of exception tells you something about what is wrong with your code.
# 
# A **SyntaxError** (or **IndentationError**): means that Python does not know how to parse the instructions you wrote, and cannot even begin executing them.
# 
# Other kinds of errors arise while the program is executing (during *runtime*).  Such runtime **Exceptions** mean that Python cannot do what you have asked of it.
# 
# For a bit more on fixing errors see [debugging](../course/debugging.md)

# In[ ]:


3 +


# In[ ]:


abc


# In[ ]:


'3' + 4


# Note that for strings, the quotes have to be closed, and must match.  `'abc'` is an acceptable string literal.  `"abc"` is also an acceptable string literal.  `'abc"`, `"abc'`, `'abc`, `"abc` are all syntax errors because Python cannot figure out where the string started by the first quote is supposed to end:

# In[ ]:


'abc'


# In[ ]:


"abc"


# In[ ]:


'abc"


# In[ ]:


"abc'


# In[ ]:


'abc


# In[ ]:


"abc


# ### functions
# 
# We will talk much more about functions when we start writing them ourselves, but for now, we just need to know that functions are stored procedures, which we can call by invoking their name, and passing some arguments to them:  `functionname(argument)`.
# 
# For instance, the `print()` function prints whatever you give it.

# In[ ]:


print('hello!')
print('with the print function, we can print many lines in one cell!')


# ### White space
# 
# Python treats white space (i.e., spaces, tabs, etc.) as meaningful.  Some puzzling syntax errors might arise from impropertly indenting code.

# In[ ]:


print('hello')
   print('with the print function...')


# Other syntax errors might arise from mixing spaces and tabs.  We will talk more about indenting in the context of code blocks.  For now, just be aware that even though blank spaces just look like space to you, they are a meaningful character to the python interpreter.  It might make sense if you visualize what the interpreter sees -- the white space is shown to us as a blank, but the computer encodes it with characters, like any other character.
# 
# `
# print('hello')
# ␣␣␣print('with the print function...')
# `

# ## Python types, operators
# 
# Computer programs do stuff to data.  The data has to somehow be represented in the computer.  Ultimately, all the data is represented in binary in computer memory, but we generally don't have to deal with the binary ourselves, we deal with more abstracted data representations.  However, Python needs to know what kind of data it is dealing with, to determine what to do with the relevant binary information.  Thus, data are encoded in some kind of data type, and the *data type* is of utmost importance to how Python will interpret our commands.  There are many different types of data and data structures in Python.  Today we will deal with the basics: integers, floating point numbers, strings, and boolean values.
# 
# The important thing to remember is that how things *appear* is different from how things are **represented** in the computer.  So when investigating what Python might do to a certain variable, we must know not only the value of the variable, but also its **type**.
# 
# ### type()
# 
# the `type()` function takes some argument, and returns the data type of the object referenced by that argument.  If we pass in a literal, it will tell us the literal's type.

# In[ ]:


type('34')


# In[ ]:


type(34.0)


# In[ ]:


type(34)


# In[ ]:


type(True)


# The basic data types we have encountered so far are
# - `str`: strings, which are sequences of characters -- text. (more in a bit)
# - `int`: integers, which are whole (integer) numbers.
# - `float`: floating point numbers, which are numbers that have decimals.
# - `bool`: boolean / binary values, used for all logical operations: either `True`, or `False`.
# 
# #### isinstance()
# 
# We can check if a given variable is a certain type with the isinstance() function

# In[ ]:


x = 34
isinstance(x, int) # True
isinstance(x, float) # False
isinstance(x, str) # False


# ### Operators
# 
# Operators are special symbols that take some arguments, do something to them, and return some value.  The basic binary (meaning they take two values) arithmetic operators are very familiar, when applied to numbers:

# In[ ]:


3 + 4


# In[ ]:


3 - 4


# In[ ]:


3 * 4


# In[ ]:


3 / 4


# In[ ]:


3 ** 4


# Note, that last one might be a bit surprising.  the `**` operator corresponds to exponentiation, so `3 ** 4` calculates $3^4$ (i.e., $3 * 3 * 3 *3$)

# ### Operator precedence
# 
# As in basic arithmetic, operators have precedence: some of them are executed first, and parentheses can be used to group operations to set a precedence order.

# In[ ]:


14 - 3 * 2


# In[ ]:


(14 - 3) * 2


# ### Operators and types
# 
# As we saw, a given literal has a type, and what it means to apply a given operation to a particular entity depends on its type.
# 
# For instance, some operations don't make any sense for certain types:

# In[ ]:


'css ' * 'class'


# The cell above yields a `TypeError` because Python does not have a defined operation corresponding to `*` for two strings.  That makes sense -- after all, what do you think such an operation could mean?
# 
# Some confusion may arise because, sometimes, the operation might look meaningful to us, but not to Python, because Python does not interpret code the same way we do.  For instance `'3' * '4'` makes sense to us, but not to Python.  The reason is that Python knows that `'3'` and `'4'` are strings, the fact that those strings *could* be interpreted as numbers is irrelevant for the Python interpreter.  At the level of data types, `'3'` and `'4'` are no different from a string like `'css'`.  All it knows is that you have asked it to apply `*` to two strings, and it does not think that is a valid operation.

# In[ ]:


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

# In[ ]:


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

# In[ ]:


3 + 3


# In[ ]:


3.0 + 3.0


# In[ ]:


3 + 3.0


# Less intuitively, `+` can also be applied to two strings:
# 
# - `str + str -> str`: when applied to two strings, `+` returns the concatenation of the two strings.

# In[ ]:


'3' + '3'


# Some combinations of types, however, do not work with `+`:  `str + int` will return a TypeError.

# In[ ]:


'3' + 3


# Here is another surprising operator type combination that works:
# 
# - `str * int -> str`: a string `*` an integer `n` returns that string, repeated `n` times.  (this also works for other sequences, which we will see later)
# 
# This has a certain logic to it: if we think of multiplication as repeated addition, and addition of strings is concatenation, then multiplication of strings would be repeated concatenation.

# In[ ]:


'a' * 5


# In[ ]:


2 * 'hip ' + 'hooray'


# In[ ]:


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
# We will need to store things in memory.  To do so, we will use variables.  A variable is a name that we can assign to an object, and refer to that object later.  We use the assignment operator `=` to do this.
# 
# > **Note that this is *assignment* not mathematical *equality*.**
# >
# > **Mathematical equality** is a declarative statement of fact.  $x = 4y+3$ declares a particular fact: that a certain relationship holds.  We can do algebra to derive other facts from this one (e.g., $x-3 = 4y$ and $y=x/4 - 3/4$).  So a statement like $x = x + 1$ is invalid because from it we can derive a contradiction, such as $0 = 1$.
# >
# > **Assignment** is a procedural instruction, where we tell the computer to evaluate the stuff on the right hand side, and assign the output to the left hand side.  So a statement like `x = x+1` is totally fine.  We calculate `x+1` on the right hand side, then assign that value to `x`.  The net effect is that we have incremented the value of `x` by 1.
# 

# In[ ]:


greeting = 'Hello!  This is a long string describing how we greet you!'

print(greeting)


# By assigning values to variables, we can use them many times.

# In[ ]:


radius = 4
pi = 3.14159

print('area: ', pi * radius ** 2)
print('circumference: ', 2 * pi * radius)


# ### Sequential execution
# 
# Within a given code block, instructions are executed in a particular sequence, and future instructions (such as changing the value of a variable) do not change the calculations (and assignments) from prior instructions:

# In[ ]:


a = 3
b = 4
x = a * b
a = 5
print('x: ', x)
print('a*b: ', a*b)


# ## Reading code
# 
# When **reading** code, it is important that you consider not just what the lines are telling the computer to do, but what the *state* of the program in memory is at the moment that the computer follows those instructions.
# 
# For instance, to think through what the code above is doing, let's step through it.  Starting with the memory state before the first line is even evaluated.
# 
# > *memory state:* `{}` (blank, other than built in stuff)
# 
# `a = 3`: assign value 3 to variable named `a`
# 
# > *memory state:* `{'a': 3}`
# 
# `b = 4`: assign value 4 to variable named `b`
# 
# > *memory state:* `{'a':3, 'b':4}`
# 
# `x = a * b`: `a` evaluated to `3` (`x = 3 * b`), `b` evaluated to `4` (`x = 3 * 4`), `*` applied to `3` and `4` to yield `12` (`x = 12`), `12` is assigned to `x`.
# 
# > *memory state:* `{'a':3, 'b':4, 'x':12}`
# 
# `a = 5`: assign value 5 to variable named `a`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# `print(x)`: `x` evaluated to `12` (`print(12)`), `print()` prints `12`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# `print(a*b)`: `a` evaluated to `5` (`print(5*b)`), `b` evaluated to `4` (`print(5*4)`), `*` applied to `5` and `4` to yield `20` (`print(20)`), `print()` prints `20`
# 
# > *memory state:* `{'a':5, 'b':4, 'x':12}`
# 
# When dealing with more complicated programs and algorithms, it is sometimes very helpful to do this with paper and pencil, to make sure you can think through what each line is doing to the memory state. Alternatively you can (1) insert print statements to check specific variable values (print [debugging](https://en.wikipedia.org/wiki/Debugging)), (2) in jupyter notebooks, insert IPython `%whos` linemagic to check all variables in memory, or (3) run the code in [python tutor](http://pythontutor.com/).
# 
# Below I demonstrate the second method:

# In[ ]:


# this line clears all prior variables from memory
get_ipython().run_line_magic('reset', '-f')
# shows contents of variables in memory
get_ipython().run_line_magic('whos', '')
print('') # prints an empty line for easier reading.

a = 3
get_ipython().run_line_magic('whos', '')
print('')

b = 4
get_ipython().run_line_magic('whos', '')
print('')

x = a * b
get_ipython().run_line_magic('whos', '')
print('')

a = 5
get_ipython().run_line_magic('whos', '')
print('')

print('x: ', x)
print('a*b: ', a*b)


# ### Notebooks, cells, and memory state.
# 
# Important Note: This kind of logic for stepping through code works great when considering stand alone scripts.  Notebooks, however, are pretty tricky, because each cell runs code in the same environment, so the memory state at the start of the cell is determined by which cells had been run previously.  (this is why I used `%reset -f` above, to clear all variables from prior cells).

# In[ ]:


# note that x is still in memory, even though it was not defined in this cell!
print(x)


# Cells *could* be run out of order.  This presents a great deal of opportunity for confusion.   Make sure that you can run your whole notebook from start to finish, in the order it is written!
# 
# In jupyter notebooks, you can use the 'line magic' commands `%who` to see a list of currently declared variables in memory, and `%whos` to also see their values.

# In[ ]:


get_ipython().run_line_magic('who', '')


# In[ ]:


get_ipython().run_line_magic('whos', '')


# ### Print debugging
# 
# The most generic (and arguably most powerful) way to figure out why a program is not doing what you want it to do (i.e., to "debug" a program) is to insert `print()` statements into the code, to ask the program to print out the current values (and types!) of various variables in memory.  Often this will reveal that variables do not have the values you expected, and you can figure out at what point in the program your expectations diverge from what the code is actually doing.

# In[ ]:


a = input('enter number a: ')
b = input('enter number b: ')
print(type(a), a)
print(type(b), b)
print(a+b)


# # Variables
# 
# - definition
# - Namespace
# - Variable types

# ## Programming With Python

# Programming: a way to ask computer to store values (variables), and do things with them (operations).`

# In[ ]:


# This is a comment. You can write a comment by using a `#`
my_variable = 12

my_other_variable = 13 # Comments can be 'inline', like this one


# ### Defining Variables

# <div class="alert alert-success">
# In programming, variables are things that store values. Variables are defined with <code>name = value</code>.
# </div>

# In[ ]:


my_var = 1  # `my_var` is a variable

# This defines another variable
other_var = 'variables are cool'


# In[ ]:


# once you create a variable it's stored in your namespace
other_var


# ## Code Variables != Math Variables
# 
# In mathematics: `=` refers to equality (as a statement of truth).
# 
# In coding: `=` refers to assignment.

# Math: What is x?
# 
# $y = 10x + 2$

# Code: What is x?
# 
# `x = x + 1`

# #### Clicker Question #1
# 
# After executing the following code, what will be the value of `my_var`?

# In[ ]:


my_var = 2

my_var = my_var + 1


# In[ ]:


my_var


# - A) 2
# - B) 3
# - C) "my_var + 1"
# - D) This code will fail

# #### Clicker Question #2
# 
# After executing the following code, what will be the value of `diff_var`?

# In[ ]:


diff_var = my_variabel - my_var

print(diff_var)


# In[ ]:


my_variable - my_var


# - A) 4
# - B) 9
# - C) "my_variable - my_var"
# - D) This code will fail

# ### Assignment Notes
# 
# - In programming `=` means assignment
# - There can be more than one assignment in a single line
# - Anything to the right of the `=` is evaluated before assignment
#     - This process proceeds from right to left

# ## Declaring Variables Cheat Sheet
# 
# - Names are always on the left of the `=`, values are always on the right
# - Names are case sensitive
# - Variables must start with letters (or underscores)
#     - After that, they can include numbers
#     - They cannot include special characters (like &, *, #, etc)
# - Python doesn't care what you name your variables
#     - Humans do care. Pick names that describe the data / value that they store

# ## Reserved Words
# 
# There are 33 words that are not allowed to be used for variable assignment in Python 3.6.

# <table type="text/css">
#   <tr>
#       <td><code>False</code></td>
#       <td><code>None</code></td>
#       <td><code>True</code></td>
#       <td><code>and</code></td>
#       <td><code>as</code></td>
#       <td><code>assert</code></td>
#       <td><code>break</code></td>
#   </tr>
#   <tr>
#       <td><code>class</code></td>
#       <td><code>continue</code></td>
#       <td><code>def</code></td>
#       <td><code>del</code></td>
#       <td><code>elif</code></td>
#       <td><code>else</code></td>
#       <td><code>except</code></td>
#   </tr>
#   <tr>
#       <td><code>finally</code></td>
#       <td><code>for</code></td>
#       <td><code>from</code></td>
#       <td><code>global</code></td>
#       <td><code>if</code></td>
#       <td><code>import</code></td>
#       <td><code>in</code></td>
#   </tr>
#   <tr>
#       <td><code>is</code></td>
#       <td><code>lambda</code></td>
#       <td><code>nonlocal</code></td>
#       <td><code>not</code></td>
#       <td><code>or</code></td>
#       <td><code>pass</code></td>
#       <td><code>raise</code></td>
#   </tr>
#   <tr>
#       <td><code>return</code></td>
#       <td><code>try</code></td>
#       <td><code>while</code></td>
#       <td><code>with</code></td>
#       <td><code>yield</code></td>
#   </tr>
# </table>

# In[ ]:


# you will get an error if you try to assign a variable to one of these words
try = 6


# ## Kernels

# <div class="alert alert-success">
# The <b>kernel</b> is the thing that executes your code. It is what connects the notebook (as you see it) with the part of your computer that runs code.
# </div>

# Your kernel also stores your **namespace** - all the variables and code that you have declared (executed).
# 
# It can be useful to clear and re-launch the kernel. You can do this from the 'kernel' drop down menu, at the top, optionally also clearing all ouputs. Note that this will erase any variables that are stored in memory.

# ## Namespace

# <div class="alert alert-success">
# The <b>namespace</b> is the 'place' where all your currently defined code is declared - all the things you have stored in active memory.
# </div>

# In[ ]:


get_ipython().run_line_magic('pinfo', 'whos')


# In[ ]:


# You can list everything declared in the namespace with '%whos'
get_ipython().run_line_magic('whos', '')


# ## Variable Types

# <div class="alert alert-success">
# Every variable has a <b>type</b>, which refers to the kind of variable that it is, and how the computer stores that data.
# </div>

# In[ ]:


# Declare a variable
variable_name = 1

# You can always ask Python 'what type is this variable' using:
type(variable_name)


# ### Int

# <div class="alert alert-success">
# <b>Integers</b> store whole numbers.
# </div>

# In[ ]:


my_integer = 1
another_integer = 321


# In[ ]:


# integers can be signed
yet_another_integer = -4
type(yet_another_integer)


# ### Float

# <div class="alert alert-success">
# <b>Floats</b> store signed, decimal-point numbers.
# </div>

# In[ ]:


my_float = 1.0
another_float = -231.45


# In[ ]:


type(another_float)


# ### String

# <div class="alert alert-success">
# <b>Strings</b> store characters, as text.
# </div>

# In[ ]:


my_string = 'words, words, words'
another_string = 'more words'

# Note that strings can be defined with either '' or ""
and_another = "and some more"


# In[ ]:


print(and_another)
type(and_another)


# #### Quotation Marks
# 
# About those quotation marks...

# In[ ]:


my_string = 'This is a single-quoted string.'
my_string


# In[ ]:


my_string = "This is a double-quoted string."
my_string


# Note that Python will put single quotes around it, even if you specify double quotes.
# 
# A general principle is to pick something and be consistent. In this course, I'll do my best to only use single quotes.

# #### Aside: What if you want to print a quotation mark?
# - use double quotes outside with apostraphe inside quotes
# - use an escape `\` (backslash) before character

# In[ ]:


# double quotes on outside; single quote inside
my_string = "i wan't to see a quote."
my_string


# In[ ]:


# backslash to "escape" quotation mark
string_quote = "And she said, \"Please teach me Python!\""
string_quote


# ## Boolean

# <div class="alert alert-success">
# <b>Booleans</b> store <code>True</code> or <code>False</code>.
# </div>

# In[ ]:


my_bool = True
another_bool = False


# In[ ]:


type(another_bool)


# ## None

# <div class="alert alert-success">
# <code>None</code> is a special type that stores <code>None</code>, used to denote a null or empty value.
# </div>

# In[ ]:


the_concept_of_nothing = None


# In[ ]:


type(the_concept_of_nothing)


# #### Clicker Question #3
# 
# After executing the following code, what will the type of `var_a` be?

# In[ ]:


var_a = -17.5


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #4
# 
# After executing the following code, what will the type of `var_b` be?

# In[ ]:


var_b = '-17.5'


# In[ ]:


type(var_b)


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #5
# 
# After executing the following code, what will the type of the variable `m` be?

# In[ ]:


n = 1
a = 'm'
m = n
type(m)


# In[ ]:


m


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# ## Aliases

# <div class="alert alert-success">
# Variables are names assigned to a value. Values can have more than one name.
# </div>

# In[ ]:


# Make a variable, and an alias
a = 1
b = a
print(b)


# Here, the value 1 is assigned to the variable `a`.
# 
# We then make an **alias** of `a` and store that in the variable `b`.
# 
# Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

# ### Reminders

# - Multiple variables can relate to the same value(s)

# ### Mutable vs Immutable
# 
# The variable types we've talked about today are all **immutable**. This means they cannot be altered after they're created.

# In[ ]:


immutable_string = 'COGS18 is the best!'
immutable_string[4]


# In[ ]:


# cannot change part of the string after creation
immutable_string[4] = '0'


# Python does have **mutable** types. We'll talk about these later in the course, and these are where aliasing shines!

# ## Indentation
# 
# Just a *brief* word on indentation.
# 
# Python *does* care about whitespace.
# 
# You will get an error if Python runs into unanticipated whitespace.

# In[ ]:


a = 1
    b = a

    print(b)


# There *are* times when indentation will be required and expected. We'll discuss these in future lectures.

# 
# <center><img src="img/doing_it_right.png" width="900px"></center>
# 
