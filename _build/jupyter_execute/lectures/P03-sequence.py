#!/usr/bin/env python
# coding: utf-8

# #  P03: Sequence types
# 
# ## Conceptual overview
# 
# ### Container data types in Python
# 
# **Atomic types** such as integers, floats, booleans, and a few other types in Python, are data types that have no substructure -- they are the smallest possible unit.  A boolean like True is a basic unit in Python: it has no parts.  Ditto for integers, floats, etc. (even though, mathematically, we could define "parts" to an integer, in the Python representation they have no parts).
# 
# **Containers** are data types in Python that that **contain** multiple other objects.  Every container has the ability to be probed with the expression `x in container` (which will return True if `x` is an item in the container, and False otherwise).
# 
# **Collections** Are *containers* that have a few further properties: they have a *size*, indicating how many elements it contains (obtained via `len(x)`); and they can be *iterated* over (e.g., you can loop through all the items in a collection via a for loop `for item in collection:`...).
# 
# **Sequences** are *collections* with a **deterministic order**, which means they can be **indexed** via an integer indicating the order of an element, with the notation `x[3]` and **sliced** via integer expressions to obtain subsequences.  Sequences can also be concatenated with the `+` operator.
# For instance, a list is a sequence, so you can ask for the initial item of a list via `x[3]`.  (In contrast, a `set` is a collection but not a sequence, so you cannot ask for a particular item via an index.)
# 
# **Mutable sequences** are *sequences* that can be changed after they are created (in contrast, immutable sequences cannot be changed, they can only be overwritten with a newly created immutable sequence). Mutable sequences have useful methods like `seq.append(item)` (add an item to the end of the sequence), `seq_1.extend(seq_2)` (add the items in seq_2 to the end of seq_1), `seq.pop(index)` (return the value of the item at index, and remove that item from the sequence), `seq.remove(item)` (remove the first item in the sequence that is equal to item), `seq.reverse()` to reverse the order of the sequence.  These are "in place" methods, in that they change the list in place, without returning a copy of the list.  In contrast, *immutable* sequence methods (such as those for *string*, have to return a new string with the change, because the original string cannot be changed).
# 
# **Strings** are immutable *sequences* of characters.  Each element of a string is a character.  Since they are a sequence, they can be indexed and sliced. Because they are immutable, you cannot change an element of a string, you can only create a new, different string.  Strings also have a number of very helpful methods for dealing with the text they represent, which we will cover below (since strings are immutable, methods that modify the string return a copy of a string with the modification, rather than changing the existing string in place).
# 
# **Lists** are *mutable sequences*, which can contain items of any type. They not only support indexing and slicing, but they can also be changed, reversed, appended to, extended, sorted, inserted into, and more.
# 
# **Tuples** are *immutable sequences* of mixed elements.  They have a number of uses which we may cover eventually.
# 
# **Sets** are *collections* of *unique* items.  They support useful [set operations](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) like set union, set difference, subset evaluations, etc.
# 
# **Dictionaries** are *collections* that are mappings.  They do not have a particular *order*, but items in a dictionary have a unique *key* which need not be an integer.
# 
# ### Indexing and slicing sequences.
# 
# Specific elements of a sequence can be obtained by **indexing** -- referring to the specific order of that element in the sequence.  Python uses zero-based indexing, which means that the item at the start of the index has an index of 0, the next item has an index of 1, and so on. There are some [good reasons](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html) to index starting with 0, although not all programming languages adopt this convention.
# 
# A subsequence can be obtained from a sequence by **slicing** -- referring to the set of indexes that you want to pull out.  A slice is defined with the notation `[start:stop:step]`, which we will cover in great detail below.
# 
# 
# ## Sequences
# 
# ### Strings: defining / creating
# 
# Strings are immutable sequences of characters.
# 
# A string can be created in python by putting some text in quotes.
# - You can use either single quotes (`'string'`), or double quotes (`"string"`), it does not matter so long as the start and end of the string match. The choice of single vs double quotes is arbitrary. Pick one and use it consistently.
# - Tripple quotes, where you repeat three quotes of the same type to start the string (e.g., : `'''string'''` or `"""string"""`) are a special string definition that allows the string to span multiple lines.

# In[1]:


a = 'this is a string'
b = "this is another string"
c = '''
this is a
3rd string
'''
d = """
this is a
fourth string
"""
print(a,b,c,d, sep='\n')


# One reason to favor single or double quotes is if you have to have quotes in your own string,
# in which case use one type of quote to indicate the string, and another type of quote inside.
# Alternatively, you can *escape* quotes inside a string, to tell Python that the quote in the
# string should be treated as a character, rather than the end of the string.

# In[2]:


# these are ok because different quotes are used inside the string.
print('1: Alice said "Hello!"')
print("2: Alice said 'Hello!'")
# these are ok because the inside quote is escaped.
print("3: Alice said \"Hello!\"")
print('4: Alice said \'Hello!\'')
# this is a syntax error because Python thinks the string ends before the H
print("5: Alice said "Hello!"")


# ### Lists: defining
# 
# Lists are a general purpose, mutable sequence types for storing a bunch of objects in a deterministic order.
# 
# A list can be created with square brackets: `[item1, item2]`.  A list can contain all sorts of objects, and those objects need not be of the same type.  A list can even contain more lists.

# In[3]:


list_of_stuff = ['hello', 'goodbye', 'ciao', 'salut', 'adios', 3.14159, 1200, ['a', 'b', 3, ], ]
print(list_of_stuff)


# ### Common sequence operations
# 
# First we will go over some common methods that all sequences (strings, lists, and more) share.
# 
# To do so, we will use the following two sequences.  Note that the list contains a mixture of types -- integers, floats, strings, and even another list.

# In[4]:


alphabet = 'abcdefghijklmnopqrstuvqxyz'
some_numbers = [0, 1, 2**(1/2), 3**(1/2), 2, 'e', 3, 'pi', 4, 5, [2, 3, 5, 7], ]
print('alphabet: ', alphabet)
print('some_numbers:', some_numbers)


# #### len()
# 
# Every collection (and thus, also every sequence) has a size property, indicating how many elements it has.  This can be polled with the `len()` function.  Note that the list inside the `some_numbers` list counts as one item.

# In[5]:


print(len(alphabet))
print(len(some_numbers))


# #### in
# 
# The contents of every container, (and thus every collection, and thus every sequence) can be probed with the `in` operation.  `x in container` returns `True` if x is one of the items in the container.

# In[6]:


print('b' in alphabet) # True
print('@' in alphabet) # False
print('pi' in some_numbers) # True
print(7 in some_numbers) # False -- it only probes immediate members, not elements of elements.
print([2, 3, 5, 7] in some_numbers) # True
print(1.41421356237 in some_numbers) # False Exact equality of floats is complicated


# For strings, the `in` operation is special because it can also evaluate if a given string contains a particular *substring*, rather than a specific character.  This does not work for other sequence types.

# In[7]:


print('hijk' in alphabet) # True
print('cba' in alphabet) # False
print('Abc' in alphabet) # False -- case sensitive
print(' abc' in alphabet) # False
print([0, 1] in some_numbers) # False: this asks if one of the elements is the list [0,1]


# 
# #### indexing
# 
# Because sequences have a deterministic ordering, we can retrieve particular items from them with square bracket numerical indexing.  This applies to both lists and strings.

# In[8]:


print(alphabet[0])
print(some_numbers[3])
print(alphabet[-1]) # same as len(alphabet)-1, or 25
print(some_numbers[-4]) # same as len(some_numbers)-4, or 7


# Note:
# - this is zero-indexed, so the initial item of the sequence has an index of 0,
# - the last item of the sequence has an index of `len(seq)-1`
# - negative indexing `-1` is a shortcut for indexing from the end of the sequence by omitting the `len(seq)` part, so `x[-1]` has the same meaning as `x[len(x)-1]`
# 
# 
# #### slicing
# 
# Indexing pulls out one item from a sequence, but slicing can pull out multiple elements.
# 
# The full slicing notation is `x[start:stop:step]`, where we can pull out elements beginning with `start`, through `step-1`, incrementing by `step`.

# In[9]:


print(alphabet)
print(alphabet[5]) # [5]
print(alphabet[0:5:1]) # [0, 1, 2, 3, 4] note, this omits the letter at index stop [5]='f'
print(alphabet[0:5:2]) # [0, 2, 4] we are counting by 2, so getting indices
print(alphabet[5:0:-1]) # [5, 4, 3, 2] we are counting by -1! note [0] omitted
print(alphabet[-3:-1:1]) # we can use negative indices here too. [-3, -2] = [23, 24]


# ##### Slicing defaults.
# 
# There are very commonly used values for `start`, `stop` and `step`, so these are set to be the defaults if that value is omitted.
# 
# - default `start=0`: `x[:b:1]` means `x[0:b:1]` because if the start value is omitted, the default of 0 -- initial element of sequence -- is used
# - default `stop = len(x)`:  `x[a::1]` means `x[a:len(x):1]` which yields all the items from index `a` through the end of the list
# - default `step = 1`: so `x[a:b:]` and `x[a:b]` both mean `x[a:b:1]`
# 
# These defaults make a few concise expressions possible:
# - `x[a:]` gets all the items from `a` through the end of the sequence (since it defaults to `x[a:len(x):1]`
# - `x[:b]` gets all the items from the start of the sequence through `b-1`
# - `x[::k]` gets every kth item from index 0 through the end.
# 
# ```{note}
# **Default slicing parameters with negative indexing**
# 
# One subtlety is that the default start and stop values change depending on the *step sign*:
# when incrementing positively defaults are as described above. When incrementing negatively,
# default start is `len(x)-1` (or just -1 -- the last item), and default stop is the item before 0, so that the last included item has index 0.
# 
# However, note that you cannot yourself indicate "the item before 0" because that would be -1, which has a different meaning (shorthand for `len(x)-1`).
# Consequently, if you want to end at the initial sequence item with negative indexing, you have to either omit it, or provide the argument `None`
# 
# Altogether, `x[::-1]` is the same as `x[-1:None:-1]`
# ```

# In[10]:


print(alphabet[:5]) # [0, 1, 2, 3, 4]
print(alphabet[-5:]) # [21, 22, 23, 24, 25]
print(alphabet[::2]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
print(alphabet[::-1]) # [25, 24, 23, ... 0]
print(alphabet[-1:None:-1]) # same as above.


# We can do the same things with a list:

# In[11]:


print(some_numbers[5:]) # [5, 6, 7, 8, 9, 10]
print(some_numbers[:-3]) # [0, 1, 2, 3, 4, 5, 6, 7] (note index 8 (11-3) excluded!)
print(some_numbers[::3]) # [0, 3, 6, 9]


# #### + concatenation
# 
# Often you will want to concatenate two sequences.  This can be done with the `+` operator.  This works for strings and all other sequences.

# In[12]:


a = "hello"
b = " world"
print(a + b)

c = [1, 2, 'a']
d = [35, 46]
print(c + d)


# Note that this does not work for different types.  You cannot `+` a string and an integer (later we will see that to do this we must first convert the integer to a string).  Nor can you `+ a string and a list, even though they are both sequence types.
# 

# In[13]:


print('boo' + 3) # TypeError


# In[14]:


print([1, 2, 3] + 'boo') # TypeError


# ##### * replication
# 
# Relatedly, if string/sequence "addition" means concatenating the two strings, what might string "multiplication" be? Repeated concatenation!
# 
# The operator `*` applied to a sequence (such as a string) and an integer `n` repeats the string/sequence `n` times.

# In[15]:


print('Go '*3 + 'Ole '*3)
print([1, 2]*5)


# (You cannot `*` two strings, or two sequences of any other type, or a sequence and a float)
# 
# ## Strings
# 
# In addition to inheriting properties from the generic "sequence" type, strings have many of their own unique methods that are particularly helpful for dealing with text.
# 
# ### inserting variables into strings via concatenation
# 
# We can use string concatenation to put variable values into strings.  For instance:

# In[16]:


name = "Bob"
age = 67
print("Hello " + name + "!")
print("Your age is " + str(age) + ".")


# Note two things about the code above:
# - because age is an integer, not a string, we have to convert it into a string
# first before we can use `+` concatenation to it. After all `+` applied to integers means something
# completely different than `+` applied to strings, so we have to make sure we are doing the right thing. (If we try to `+` a string and an integer, we get a TypeError.)
# - It is a bit ugly, there are all these quotes and `+` signs scattered about. There is a better way

# In[17]:


67 + 'years'


# ### inserting variables into strings via f-strings
# 
# f-strings, or formatted strings, are a special kind of string that allows for a nice way to
# include variables inside a string.  An f-string is defined with the special string notation: (`f''`)
# For instance, the example above can be written more elegantly with f-strings:

# In[18]:


name = "Bob"
age = 67
print(f'Hello {name}!')
print(f"Your age is {age}.")


# Note that the f strings look much tidier, and also do the conversion of different data types into strings for you.
# 
# There are lots of details about how to refine formatting inside the f-string
# (e.g., how many decimals to print in a float? pad a string with space? etc.)
# But for now we can just use them as a tidy way of sticking variables into strings.
# 
# ### String methods
# 
# Everything in python is an object, and strings are no exception. What it means for strings to be objects, is that each string has *methods* defined by the string class.  For an exhaustive list, and explanations, look at the [python string documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).
# 
# #### String modification methods
# 
# These methods are many, but a few helpful ones alter the string in various common ways:
# - `'string'.lower()` converts it to lower case
# - `'string'.upper()` converts to upper case
# - `'string'.replace(old,new)` replaces every instance of the string stored in the parameter `old` with a copy of the `new` string.
# 
# Note that I use the f-string shortcut f'{var=}' which prints "var='contents of var'", so we can easily see what each line below is doing.

# In[19]:


sentence = 'When angry it helps to WRITE IN ALL CAPS!'
print(f'{sentence=}')
print(f'{sentence.lower()=}')
print(f'{sentence.upper()=}')
print(f'{sentence.title()=}')
print(f'{sentence.replace("angry", "excited")=}')


# Note that strings are **immutable**, so any method that changes a string does not change the existing string, but instead makes a new, altered string.

# In[20]:


sentence = 'When angry it helps to WRITE IN ALL CAPS!'
print(sentence.lower())
print(sentence) # original not changed!
sentence = sentence.lower() # to change it, we have to overwrite it
print(sentence)


# #### String evaluation methods
# 
# There is also a large family of string evaluation methods of the form `'string'.isXXX()` where
# XXX is something you might care about.  For instance
# - `.isdigit()` returns True if a string is composed  entirely of digits {0...9}.
# - `.isalpha()` returns  True if a string is composed entirely of alphabetic letters {a-zA-Z}.
# 
# ## Lists
# 
# Lists are **mutable** sequences, so they have a number of methods for modifying the list "in place".  Which means that the method changes the existing list, rather than creates a new list with the change made (the only way to change immutable sequences, like strings).
# 
# ### growing a list in place
# 
# You could make a new list by concatenating two existing lists via `+`.  However, usually it is more efficient to add onto an existing list, rather than create a new, larger list.  This can be done via append and extend which change the list in place, and do not return anything:
# 
# - `list_1.append(item)` adds the item to the end of list_1.
# - `list_1.extend(list_2)` adds the items in list_2 to the end of list_1

# In[21]:


my_list = [1, 2, 'e', 3, ]
print(my_list)
my_list.append('pi')
print(my_list)
my_list.extend([4, 5, 6])
print(my_list)


# ### shrinking a list in place
# 
# You can make a new, subset of a list via slicing.  But sometimes that is cumbersome, and the creation of a new list is inefficient.  Alternatively, we can modify the list in place via `pop` and `remove`.
# 
# - `list_1.pop(idx)` returns the element at index `idx` and also removes that element from the list.
# - `list_1.remove(item)` removes the first occurrence of `item` from the list, i.e., it removes the first element that has the same value as `item`.

# In[22]:


my_list = ['red', 'blue', 'green', 'tomato', 'tomato', 'tomato', 'purple']
item = my_list.pop(2) # assigns 'green' (index 2!) to item, and removes it from the list
print(item)
print(my_list)
my_list.remove('tomato') # removes the first 'tomato'
print(my_list)
