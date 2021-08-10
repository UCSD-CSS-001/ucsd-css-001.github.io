#!/usr/bin/env python
# coding: utf-8

# # CSS 1 Lecture 3
# 
# ## Programming
# 
# - Think about what you want to do before you write code.
# 
# - Do not *guess* about the *logic* 
# 
# you can guess about the syntax, or function name, but do not guess on logic: there are too many ways to guess wrong, and you are likely to confuse yourself.
# 
# - write out the procedure in words/comments/pseudocode that you want to do, and then translate to code.
# 
# - print only what you want to see / check.  Too many print statements will confuse you, and if you leave them in there as you change code, what your code is *doing*, and what you are *printing* might diverge, and that will only cause more confusion.
# 
# ## Notes
# 
# - open a jupyter notebook as we go through class.
# 
# 

# # Lists
# 
# ## Collections (vs atomic)

# In[1]:


x = ['a', 3, 'abracadabra', 6.56, [56, 45], None, True, (4, 5, 6), {'a':56}]


# In[2]:


print(x)


# ### len and in

# In[3]:


len(x)


# In[4]:


'abracadabra' in x


# ## Sequence operations:

# In[5]:


x


# ### Index
# 
# - zero indexed

# In[6]:


x[6]


# In[7]:


alphabet = list('abcdefghijklmonpqrstuvwxyz')
print(alphabet)


# In[8]:


# index of letter e?
alphabet[4]


# In[9]:


# letter z?

alphabet[25]


# In[10]:


alphabet[len(alphabet) - 2]


# - negative indexing

# In[11]:


alphabet[len(alphabet) - 2]


# In[12]:


alphabet[-2] # shorthand for len(alphabet)-2


# In[13]:


alphabet


# In[14]:


# how do we get v from the front, and front the back of the list?
print(alphabet[21])
print(alphabet[-5])


# - index

# In[15]:


print('v' in alphabet)
print(alphabet.index('v'))


# In[16]:


alphabet.index('abracadadra')


# In[17]:


# must be an integer\
alphabet[3.0]


# ### Slicing
# 
# - make a new list from a subset
# 

# In[18]:


print(alphabet)


# In[19]:


[alphabet[3], alphabet[4], alphabet[5], alphabet[6]]


# In[20]:


newlist = []
for index in range(3, 7):
    newlist.append(alphabet[index])
print(newlist)


# In[21]:


alphabet[3:7]


# In[22]:


# what will this yield?
alphabet[2:7]


# In[23]:


alphabet[20:-3]


# - step size

# In[24]:


alphabet[0:6:2]


# In[25]:


for index in range(0, 6, 2):
    print(index, alphabet[index])


# - reverse slicing bounds

# In[26]:


alphabet[6:0:-1]


# In[27]:


for index in range(6, 0, -1):
    print(index, alphabet[index])


# In[28]:


alphabet[6::-1]


# In[29]:


alphabet[:3]   # shortcut for [0:stop:1]


# In[30]:


alphabet[20:]  # shortcut for [start:len(list):1]


# In[31]:


print(alphabet[::-1])


# - [start:stop:step]   stop is not included.  
# 
# - default start 0 when step is positive, -1 when step is negative  
# 
# - default stop is len(list) when step is positive, and the thing before 0 when step is negative  
# 
# - default step is 1

# In[32]:


# pull out every second letter between index 3 and index 18 and reverse them.

tmp = alphabet[3:19]
print(tmp)
tmp = tmp[::2]
print(tmp)
print(tmp[::-1])


# In[33]:


alphabet[17:2:-2]  #confusing!


# #### more on range()
# 
# - same argument as slicing.

# ## List methods

# In[34]:


# 
sentence = 'This is how we can split a sentence into its component words'.split(' ')
print(sentence)


# In[35]:


sentence[1:7]


# In[36]:


# find index of 'is'
# find the index of 'a'
# use those to slice

# sentence = 'this animal is a puppy'.split(' ')

print(sentence.index('is'))
print(sentence.index('a'))

sentence[sentence.index('is') : sentence.index('a') + 1]


# In[37]:


sentence = 'this animal is definitely not a puppy'.split(' ')
sentence[sentence.index('is') : sentence.index('a') + 1]


# ### append vs extend

# In[38]:


newlist = []

for i in range(0, 20):
    newlist.append(i**2)
    
print(newlist)


# In[39]:


print(sentence)
sentence.append('dog')
print(sentence)


# In[40]:


sentence = 'these are the animals that I have:'.split(' ')

print(sentence)
sentence.append('dog,')
sentence.append('cat,')
sentence.append('fish')
print(sentence)

print(sentence[-1])
print(sentence[-2])
print(sentence[-3])


# In[41]:


sentence = 'these are the animals that I have:'.split(' ')

print(sentence)
sentence.append(['dog', 'cat', 'fish'])
print(sentence)

sentence[-1]


# In[42]:


sentence = 'these are the animals that I have:'.split(' ')

print(sentence)
sentence.extend(['dog', 'cat', 'fish'])
print(sentence)

print(sentence[-1])
print(sentence[-2])
print(sentence[-3])


# ### pop and remove

# In[43]:


sentence


# In[44]:


print(sentence)
sentence.remove('the')
print(sentence)


# In[45]:


sentence =  'these are the animals that I have in the garage'.split(' ')
print(sentence)
sentence.remove('the')
print(sentence)


# In[46]:


sentence.remove('cobra')


# In[47]:


sentence =  'these are the animals that I have in the garage'.split(' ')
print(sentence)
item_5 = sentence.pop(5)
print(sentence)
print(item_5)


# In[48]:


sentence =  'these are the animals that I have in the garage'.split(' ')
print(sentence)
item_5 = sentence[5]
print(sentence)
print(item_5)


# - remove: remove by value
# 
# - pop: remove by index

# In[49]:


sentence =  'these are the animals that I have in the garage'.split(' ')
print(sentence)
item_5 = sentence.pop(5)
print(sentence)
print(item_5)


# In[50]:


sentence =  'these are the animals that I have in the garage'.split(' ')
print(sentence)
sentence.remove(['the', 'animals'])
print(sentence)


# In[51]:


things_to_remove = ['are', 'the', 'in']
sentence =  'these are the animals that I have in the garage'.split(' ')

print(sentence)
for potato in things_to_remove:
    sentence.remove(potato)

print(sentence)


# ### sort vs sorted
# 

# In[52]:


words = 'four score and seven years ago our father set forth upon this contintent, with the exlacmation abracadabra'.split(' ')

print(words)


# In[53]:


print(words)
words.sort()
print(words)
words.sort(reverse=True)
print(words)


# In[54]:


words = 'four score and seven years ago our father set forth upon this contintent, with the exlacmation abracadabra'.split(' ')

print(words)


# In[55]:


print(words)
sorted_list = sorted(words)
print(sorted_list)
print(words)


# In[56]:


words = 'A big Zebra and a .cat -foo _56 Bigger 57 zebra went home'.split(' ')
print(words)
print(sorted(words))


# In[57]:


ord('%')


# In[58]:


chr(97)


# In[59]:


heights = [68, 70, 59, 65, 77]
sorted(heights)


# ## List vs Tuple

# In[60]:


heights_list = [68, 70, 59, 65, 77] # this is a list
heights_tuple = (68, 70, 59, 65, 77) # this is a tuple


# In[61]:


print(heights_list)
print(heights_tuple)


# In[62]:


print(type(heights_list))
print(type(heights_tuple))


# In[63]:


for height in heights_tuple:
    print(height)


# In[64]:


print(heights_list[3])
print(heights_tuple[3])


# In[65]:


heights_list[3] = 78


# In[66]:


print(heights_list)


# In[67]:


heights_tuple[3] = 78


# In[68]:


heights_list.append(5)
heights_list.pop(3)
heights_list.remove(5)
heights[0] = 800


# In[69]:


heights_tuple


# Mutable objects (list lists) can be changed in place.
# 
# Immutable objects (like tuples) can only be reassigned.

# In[70]:


heights_tuple = tuple(sorted(heights_tuple))


# In[71]:


heights_tuple


# ## example

# In[72]:


from random import randint

heights = [randint(36, 96) for _ in range(100)]

print(heights)


# In[73]:


# how do I get out the 10 tallest heights?

# sort first.
heights.sort()

# way without reversing: 
print(heights[-10:])

# via reversing
# how do we reverse?
heights.sort(reverse = True)
#print(heights)
print(heights[0:10])


# In[74]:


# we have a list of heights we *hate* 
hated_heights = [69, 65, 78, 66, 160]

# note: that we might not have a given item

for potato in hated_heights:
    print(potato)
    if potato in heights:
        print('potato is in heights')
        heights.remove(potato)

# this leaves multiples.  oops


# In[75]:



heights = [randint(60, 80) for _ in range(100)]


# In[76]:


# we have a list of heights we *hate* 
hated_heights = [69, 65, 78, 66, 160]

# note: that we might not have a given item

for potato in hated_heights:
    print(potato)
    while potato in heights:
        print('potato is *still* in heights')
        heights.remove(potato)


# In[77]:


print(sorted(heights))


# ## + for lists

# In[78]:


'abra' + 'cadabra'


# In[79]:


['a', 'b', 'c'] + [1, 2, 3]


# In[80]:


x = ['a', 'b', 'c']
x.extend([1, 2, 3])
print(x)


# 

# ## Advanced list things
# 
# ### zip and enumerate
# 
# ### list comprehension

# In[ ]:




