#!/usr/bin/env python
# coding: utf-8

# # Lecture 4: Strings
# 
# Why deal with strings?
# 

# ## Making strings
# 
# different quote types
# 
# > '   
# 
# > "    
# 
# > """  

# In[1]:


x = 'string'
y = "string"
z = """string"""
print(x,y,z)


# In[2]:


"that's great"


# In[3]:


'john said, "Hello"'


# In[4]:


""" "that's just 
great" john 
said """


# ### Escape sequences

# In[5]:


print('Dear students, \n\n this is a\ttab, \\  \' \" ')


# ## What is a string anyway? 
# 
# immutable sequence of characters

# ### sequence
# 
# so indexing and slicing work as for lists

# In[6]:


x = "this is my favorite sentence"


# In[7]:


x[0:10]


# In[8]:


for character in x:
    print(character)


# ### characters 
# 
# Encoding and unicode, ord and chr
# 
# implications for sorted()

# In[9]:


character = 'a'


# In[10]:


ord('a')


# In[11]:


chr(12)


# In[12]:


for i in range(10, 160):
    print(i, chr(i))


# In[13]:


x = "this is a sEntence"

for character in x:
    print(character, ord(character))


# In[14]:


sorted(x)


# In[15]:


list(x)


# ## Putting variables in strings
# 
# string concatenation

# In[16]:


name = "Ed"
age = 38

'Hello, my name is ' + name + ' and i am ' + str(age) + ' years old' 


# ### f-strings

# In[17]:


f'Hello, my name is {name} and i am {age} years old' 


# In[18]:


f'Hello, my name is {name} and next year I will be {age + 1}' 


# In[19]:


f'{name=}'


# In[20]:


print(f'{name=}')
print(f'{age=}')
print(f'{x=}')


# ## Inspecting string contents

# In[21]:


x = "This string contains some numbers: 12345, and some punctuation!"
print(x)


# In[22]:


dir(x)


# ### Whole string tests
# 
# 'isalnum', 'isalpha',  'isnumeric',

# In[ ]:





# In[23]:


'abcdef'.isalpha()


# In[24]:


'abcdef 1234'.isalpha()


# 'islower', 'isupper', 'istitle',

# In[25]:


'This Is A title'.istitle()


# 'isspace', 'isdecimal', 'isdigit', 'isascii',  'isprintable', 'isidentifier'

# In[26]:


'235'.isdecimal()


# ### Substring tests
# 
# #### in operator

# In[27]:


'of this class' in 'The instructor of this class is named Ed'


# #### startswith, endswith, 

# In[28]:


filename = 'this-is-a-book.txt'
print(filename.endswith('.txt'))
print(filename.startswith('this-'))
print(filename.startswith('-is-'))


# ### Locating substrings
# 
# index, find, rindex, rfind

# In[29]:


string = 'The instructor of this class is named Ed'


# In[30]:


'ss' in string


# In[31]:


string.index('ss')


# In[32]:


string[26:28]


# In[33]:


string.index('t')


# In[34]:


string.rindex('t')


# In[35]:


string.rfind('t')


# In[36]:


string.index('abracadabra')


# In[37]:


string.find('abracadabra')


# In[38]:


string[-1]


# ### Counting substrings
# 
# count

# In[39]:


'abracadabra'.count('tomato')


# ## Manipulating strings

# In[ ]:





# ### Altering case
# 
# - lower
# - upper
# - title
# - capitalize
# - swapcase
# - casefold

# In[ ]:





# In[40]:


'AbracadabrA'.lower()


# In[41]:


text = "This is a List Of LETTERS"
print(text)
new_text = text.lower()
print(f'{new_text=}')
print(f'{text=}')


# In[42]:


"This is a List Of LETTERS".lower()


# In[43]:


"This is a List Of LETTERS".upper()


# In[44]:


"This is a List Of LETTERS".title()


# In[45]:


"This is a List Of LETTERS".capitalize()


# In[46]:


"This is a List Of LETTERS".swapcase()


# In[47]:


"This is a List Of LETTERS".casefold()


# ### replacing substrings

# In[48]:


text = """The Unicode Standard has become a success and is implemented in HTML, XML, Java, JavaScript, E-mail, ASP, PHP, etc. The Unicode standard is also supported in many operating systems and all modern browsers."""
print(text)


# In[49]:


text.replace(',', ' ')


# In[50]:


from string import punctuation

for character in punctuation:
    text = text.replace(character, ' ')

print(text)


# ## String pieces: splitting and joining

# In[51]:


text = text.lower()

text = text + ' 34 ^&'
print(text)


# In[ ]:





# ### separate string into pieces
# 
# - split, splitlines

# In[52]:


wordish = text.split(' ')
print(wordish)
len(wordish)


# In[53]:


word_count = 0
for item in wordish:
    print(f'{item=}')
    if len(item) > 0:
        print('\t incrementing word_count')
        word_count = word_count + 1  # word_count += 1

print(word_count)


# In[54]:


text.split('e ')


# In[55]:


text.splitlines()


# - less useful: partition, rpartition, rsplit

# ### combine pieces into one string
# 
# - join

# In[56]:


favorite_foods = ['taco', 'ice-cream', 'potatoes', 'chameleon']

f'My favorite foods are: {favorite_foods}'


# In[57]:


', '.join(favorite_foods)


# In[58]:


'My favorite foods are: ' + ', '.join(favorite_foods)


# ## other string stuff we are ignoring

# ### spacing/padding
# 
# Mostly useful for generating nice strings for printing.  Not something we worry about.
# 
# - center, ljust, rjust
# - zfill
# - strip / lstrip / rstrip
# - expandtabs
# 
# ### c-style formatting
# 
# we will use f-strings instead.
# 
# - format, format_map
# 
# ### dealing with string encoding
# 
# out of scope.
# 
# - 'encode', 'maketrans','translate',
# 
# ### regular expressions
# 
# Super useful for finding (and replacing) strings that match certain *patterns*.
# 
# However, expressing those patterns in ways that capture the usefulness of regular expressions requires learning a whole new syntax, and we will ignore it.
# 
# If feeling ambitious, read about them here:
# 
# https://docs.python.org/3/howto/regex.html

# r index vs index

# In[59]:


x = 'this is a string with some letters in it'

x.index('is')


# In[60]:


x.rindex('is')


# In[61]:


x


# In[62]:


x.split(' ')


# In[63]:


x.count('t')


# ## Sets

# In[64]:


items = {'a', 'b', 'c', 'd'}


# In[65]:


items


# In[66]:


x = 'this is a sentence'


# In[67]:


set(x)


# In[68]:


items = {'a', 'b', 'c', 'd'}


# In[69]:


print(items)


# In[70]:


print(items)
items.add('5')
print(items)


# In[71]:


print(items)
items.add('5')
print(items)


# In[72]:


print(items)
items.add('55')
print(items)


# In[73]:


x = 'abracadabra'
len(x)


# In[74]:


len(set(x))


# In[75]:


x = 'abracadabra'
y = 'supercalifragilisticexpealidiocious'


# In[76]:


set(x) & set(y) # set intersection


# In[77]:


set(x) - set(y)


# In[78]:


set(y) - set(x)


# In[79]:


set(x) | set(y) # set union


# In[80]:


# what characters occured in neither x nor y

alphabet = 'abcdefghijklmnopqrstuvwxyz'

not_in_x_or_y = []

for letter in alphabet:
    if letter not in x and letter not in y:
        not_in_x_or_y.append(letter)

print(not_in_x_or_y)


# In[81]:


set(alphabet) - (set(x) | set(y))


# In[82]:


text = """ The Unicode Standard has become a success and is implemented in HTML, XML, Java, JavaScript, E-mail, ASP, PHP, etc. The Unicode standard is also supported in many operating systems and all modern browsers.

The Unicode Consortium cooperates with the leading standards development organizations, like ISO, W3C, and ECMA.
"""


# In[83]:


text = text.lower()

characters = list(set(text))

curmax_count = 0
curmax_char = ''

for char in characters:
    print(f'{char=} {text.count(char)=} {curmax_count=} {curmax_char=}')
    if text.count(char) > curmax_count:
        print('Changing max to ', text.count(char), char)
        curmax_count = text.count(char)
        curmax_char = char


# In[84]:


text = text.lower()

characters = list(set(text))

counts = []

for char in characters:
    counts.append(text.count(char))

print(counts)


# In[85]:


max(counts)


# In[86]:


idx = counts.index(max(counts))

characters[idx]


# In[87]:


from string import ascii_lowercase as alphabet


# In[88]:


alphabet


# In[ ]:




