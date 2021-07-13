#!/usr/bin/env python
# coding: utf-8

# # Dictionaries
# 

# In[1]:


lst = [1, 2, 3, 4, 'abra']


# In[2]:


lst[-1]


# In[ ]:





# ## Making a dictionary

# In[3]:


dictionary = {'x':4, 'ed':'instructor', 3:'fish'}


# In[4]:


print(dictionary)


# In[5]:


len(dictionary)


# In[6]:


dictionary['x']


# In[7]:


dictionary[3]


# In[8]:


lookup = dict()
print(lookup)
lookup['vul'] = 'last name'
print(lookup)


# ### What can be a key?

# In[9]:


lookup = dict()
print(lookup)


# In[10]:


lookup['instructor'] = 'ed vul'
print(lookup)


# In[11]:


lookup[5000] = 'five thousand'
print(lookup)


# In[12]:


key = [2, 3]
lookup[key] = 'a list'
print(lookup)


# In[13]:


key[0] = 4
print(key)


# In[14]:


list_variable = [1, 2, 3]
print(id(list_variable))
other_variable = list_variable
print(id(other_variable))
other_variable[0] = 5
print(f'{other_variable=}')
print(f'{list_variable=}')
print(id(list_variable))
print(id(other_variable))


# In[15]:


s = 'edward'
print(id(s))
other_s = s
print(id(other_s))
other_s = other_s.replace('e', 'f')
print(other_s)
print(s)
print(id(s))
print(id(other_s))


# ### mutability?  lists vs tuples.

# In[16]:


tuple_item = (3, 4, 5)
len(tuple_item)
tuple_item[0]

tuple_item[0] = 4


# In[17]:


key  = (2, 3)
lookup[key] = 'tuple key'
print(lookup)


# In[18]:


tuple([1, 2, 3])


# ## Checking if key exists

# In[19]:


course = dict()
course['instructor'] = 'ed vul'
course['ta'] = 'jiaying xu'
course['website'] = 'http://ucsd-css-001.github.io'

print(course)


# In[20]:


'TA' in course


# ## iterating over dictionary keys, values, items
# 

# In[21]:


for key in course.keys():
    print("key: ", key)
    print("value:", course[key])


# In[22]:


for value in course.values():
    print("value:" , value)


# In[23]:


for item in course.items():
    print(item)
    print("key: ", item[0])
    print("value: ", item[1])


# ### assignment unpacking

# In[24]:


pair = ('instructor', 'ed vul')
print(pair)


# In[25]:


key = pair[0]
value = pair[1]
print(key)
print(value)


# In[26]:


for item in course.items():
    key = item[0]
    value = item[1]
    print("key: ", key)
    print("value: ", value)


# In[27]:


pair = ('instructor', 'ed vul')
key, value = pair
print(key)
print(value)


# In[28]:


for key, value in course.items():
    print("key: ", key)
    print("value: ", value)


# ## updating a dictionary

# In[29]:


course = dict()
course['instructor'] = 'ed vul'
course['ta'] = 'jiaying xu'
course['website'] = 'http://ucsd-css-001.github.io'

print(course)


# In[30]:


more_course = {'datahub':'https://datahub.ucsd.edu/user/evul/notebooks/Live%20Lectures/Lecture%205.ipynb',
              'instructor':'edward vul',
              'email':'evul@ucsd.edu'}
print(more_course)


# In[31]:


course.update(more_course)
print(course)


# ## deleting items from a dictionary

# In[32]:


course['email'] = 'test'
del course['email']
course


# ## Using a dictionary to count
# 

# In[33]:


from random import randint

integers = [randint(10, 20) for _ in range(100)]


# In[34]:


# how do we count integers?

int_counts = dict()
n_of_20 = 0

for n in integers:
    print('this loop:')
    print('n:', n)
    if n == 20:
        print('incrementing counter')
        n_of_20 += 1

print(n_of_20)


# In[35]:


# how do we count integers?

int_counts = dict()


for n in integers:
    #print('this loop:')
    #print('n:', n)
    if n not in int_counts:
        #print("making a new key entry")
        int_counts[n] = 0
    int_counts[n] = int_counts[n] + 1

print(int_counts)


# In[ ]:





# In[36]:


print(int_counts)


# In[37]:


int_counts = dict()

for n in integers:
    if n not in int_counts:
        int_counts[n] = 0
    int_counts[n] = int_counts[n] + 1

print(int_counts)


# ## sorting a dictionary

# In[38]:


int_counts


# In[39]:


for key in sorted(int_counts.keys()):
    print(key, int_counts[key])


# In[40]:


sorted(int_counts.values())


# In[41]:


from operator import itemgetter

fn = itemgetter(1)

for item in int_counts.items():
    print(item)
    print(fn(item))


# In[42]:


sorted(int_counts.items(), key = itemgetter(1), reverse=True)


# In[43]:


for k,v in sorted(int_counts.items(), key = itemgetter(1), reverse=True):
    print(k, v)


# In[44]:


sentence = "This course develops computational thinking practices and skills critical for defining, describing and analyzing social science problems using a computational approach. Students will learn to program in Python in the context of computational social science problems."


# In[45]:


print(sentence)


# In[46]:


# goal is to count letters.

# make a new dictionary to keep track of the count of each letter.
# keys will be letters.  values will be counts.
letter_count = dict()

# loop over all characters in the sentence
for character in sentence:
    # print(character)
    character = character.lower()
    # check if the character is a letter
    if character.isalpha():
        #print("its a letter!")
        if character not in letter_count:
            #print("make a new key")
            letter_count[character] = 0
        letter_count[character] = letter_count[character] + 1


# In[ ]:





# In[ ]:





# In[47]:


letter_count


# In[48]:


len(letter_count)


# In[49]:


for key in sorted(letter_count.keys()):
    print(key, letter_count[key])


# In[50]:


# what is the most frequent letter?

most_frequent = ''
max_count = 0
for key,value in letter_count.items():
    if value > max_count:
        # current value is higher than previously seen maximum
        max_count = value
        most_frequent = key


# In[51]:


print(most_frequent, max_count)


# In[52]:


# which letters never occurred?
# which letters do not appear as a key in letter_count

missing = []
letters = 'abcdefghijklmnopqrstuvwxyz'
# run a for loop to see if the values are or are not in the letters variable
for letter in letters:
    #print(letter)
    if letter not in letter_count:
        missing.append(letter)

print(missing)


# In[53]:


del letter_count['a']


# In[54]:


for key in sorted(letter_count.keys()):
    print(key, letter_count[key])


# In[55]:


# print the list of letters from most to least common.

top_5 = []

for key,value in sorted(letter_count.items(), key=itemgetter(1), reverse=True):
    print(key, value)


# In[56]:


# get list of top 5 most frequent letters

top_5 = []

i = 0
for key,value in sorted(letter_count.items(), key=itemgetter(1), reverse=True):
    if i < 5:
        top_5.append(key)
        i += 1

print(top_5)


# In[57]:


# get list of top 5 most frequent letters

top_5 = []

sorted_items = sorted(letter_count.items(), key=itemgetter(1), reverse=True)
for key,value in sorted_items[0:5]:
    top_5.append(key)

print(top_5)


# ## Problem set questions

# In[ ]:




