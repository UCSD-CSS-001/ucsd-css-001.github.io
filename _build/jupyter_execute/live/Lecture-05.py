#!/usr/bin/env python
# coding: utf-8

# # Introducing Dictionaries (sometimes called "hash maps")

# Today, we'll be talking about a very important *data structure* that is more or less universal in coding languages: the dictionary.

# ### What is a dictionary?

# It keeps track of *key-value pairs* (like a word and its definition).
# 
# Can we just use existing data structures like lists for this? Not really. 

# ### What are dictionaries useful for?

# You need a dictionary (at least one) for almost any complex coding problem. 
# 
# They show up repeatedly in the rest of our labs and problem sets. 
# 
# Example: password validation

# ### So how do dictionaries work?

# Formally, a dictionary in python is:
# - mutable (you can change it *in place*)
# - a collection (like a list, it stores things and has attributes like `len`)
# - *unordered* (IMPORTANT: this has a big effect on how you interact with dictionaries. More on this below.)
# - defined by a pairing between unique *keys* and their associated *values*

# # Today's Agenda

# 1. How to **construct** dictionaries in python
# 
# 2. How to **add new items** to a dictionary
# 
# 3. How to **access** items in a dictionary
# 
# 4. How to **delete** items from a dictionary
# 
# 5. How to **iterate** over items in a dictionary (remember, they're un-ordered)
# 
# 6. How to **sort** a dictionary (sometimes, we need them in order!)

# 
# ----------------------------------------------------------------------------------------------------------------------
# 

# # Constructing dictionaries

# In python, you can declare a new, empty dictionary, or say what's in it when you declare it.

# In[1]:


# Declare a new, empty dictionary
birthdays = dict()
print(birthdays)

birthdays = {}
birthday_list = []
print(birthdays)


# In[2]:


# Declare a new dictionary with some stuff in it
birthdays = {
    'Erik': '03/21/1991',
    'Isabella': '07/14/1992'
}
print(birthdays)
print(len(birthdays)) # why is this 2?


# # Adding to dictionaries

# You can add *new key-value pairs* to dictionaries all at once with `update` or one by one with bracket [...] notation. 
# 
# NOTE: use the same syntax to change existing values in a dictionary.

# In[3]:


# Adding multiple key-value pairs 
print(birthdays)

new_birthdays = {
    'Deniz': '09/23/2000',
    'Elliott': '08/06/2001',
    'Kayla' : '10/12/2002'
}
birthdays.update(new_birthdays)

print(birthdays)


# In[4]:


print(birthdays)
# Adding a single key-value pair (this is more common than the above)
# dictionary[key] = value
birthdays['Talia'] = '10/16/1998'
birthdays['Maricel'] = '11/26/2000'
birthdays['Alexis'] = '6/27/2000'
birthdays['Rachel'] = '06/15/1999'


# Changing a single key-value pair
# dictionary[key] = new_value
birthdays['Erik'] = '3/21/1912'

print(birthdays)
print(len(birthdays))


# # Accessing items in a dictionary

# Access items in a dictionary using the same bracket [...] syntax as you use to add or update items.
# 
# NOTE: this means you can only get items in a dictionary using the lookup *key*, not the value.

# In[5]:


# Access dictionary values with `dictionary[key]`
Isabella_birthday = birthdays['Isabella']
print(Isabella_birthday)

bday_card = f"Dear Isabella, sorry I missed your birthday on {Isabella_birthday}."
print(bday_card)


# When you try to access an item that isn't in a dictionary, python returns a `KeyError`.

# In[6]:


birthdays['Ed']


# To avoid a `KeyError`, use the `in` operator to check if a key is in the dictionary.

# In[7]:


print('Erik' in birthdays) # What does this return?
print('Ed' in birthdays) # What does this return?

people = ['Erik', 'Ed']
for person in people:
    if person in birthdays: # This `in`, a little different from the one above! 
        print(birthdays[person])


# ### Aside: what's happening when we add or edit key-value pairs in a dictionary? 

# In most coding languages, the *values* in a dictionary or hash map are stored in memory just like a list. 
# 
# The magic is that instead of adding values to the list based on the index you assign to them, a **hash function** converts the key to a unique number and stores the value in the list at the index for that number. This keeps track of key-value pairs because the hash function applied to a particular key will always point to the same place where the value is stored. 

# ### Q: What can we use as keys in a dictionary?  

# A. Only things that can be *uniquely* "hashed". 
# 
# This usually means strings or numbers (even tuples!) but not things like lists (or other dictionaries).
# 
# This also means **you can't have multiple copies of the same key** in a dictionary.
# 
# Final point: dictionaries are very flexible!

# In[8]:


birthdays[6.5] = 'January 1st'
print(birthdays)

birthdays[('I am', 'a tuple')] = 'January 1st'
print(birthdays)

# Can we add another entry with the same key? No!
birthdays['Erik'] = 'January 2nd'
print(birthdays)


# In[9]:


birthdays[['I am', 'a list']] = 'January 1st'


# ### Q: What can we use as values in a dictionary? 

# A. Almost anything, including other dictionaries!

# In[10]:


# How about a list? sure!
birthdays['Erik_siblings'] = ['02/26/1994', '03/31/1999']
print(birthdays)

# Dictionaries inside dictionaries? sure! 
birthdays_by_month = {
    # key = month, value = another dictionary with key = name, value = day of the month
    'March': {
        'Erik': 21
    },
    'July': {
        'Isabella': 14,
        'Riley': 12
    }
}
print(birthdays_by_month)

# Accessing and editing values is the same as before, just with multiple levels of keys
print(birthdays_by_month['July']) # {'Isabella': 14, 'Riley': 12}
print(birthdays_by_month['July']['Riley']) # 12

birthdays_by_month['July']['America'] = 4
print(birthdays_by_month)


# # Deleting items from a dictionary

# Use the `del` operator to delete items from a dictionary. 
# 
# The syntax to say which item you want to delete uses the same bracket [...] notation.

# In[11]:


print(birthdays) # Before deletion

# del(birthdays['Erik'], birthdays['Isabella']) # We're saying delete the key and value pair with 6.5 as the key

print(birthdays)

del birthdays['Kayla']


# What happens when you try to delete an item that wasn't in the dictionary in the first place? 
# 
# ...take a guess!

# In[12]:


# del birthdays['Ed']

if 'Ed' in birthdays:
    del birthdays['Ed']


# 
# ----------------------------------------------------------------------------------------------------------------------
# 

# # Iterating over items in a dictionary

# With lists, we say something like `for elem in my_list` or `for i in range(len(my_list))`. 
# 
# With dictionaries, it's a little more complicated. We iterate over the items by a) iterating through the *keys*, b) iterating through the *values* (not super common), or c) iterating through *keys and values* (most common).
# 
# To illustrate this, we're going to make use of a super common example of dictionaries: keeping track of counts of things.

# In[13]:


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

birthday_months = {} # Declaring my new dictionary

# Filling in counts of 0 for each month to initialize my dictionary
for month in months:
    birthday_months[month] = 0

print(birthday_months)


# In[14]:


# Now, we'll fill in the actual counts of birthday months in the class
birthday_months['Jan'] = 2
birthday_months['Feb'] = 0
birthday_months['Mar'] = 0
birthday_months['Apr'] = 0
birthday_months['May'] = 0
birthday_months['Jun'] = 3
birthday_months['Jul'] = 2
birthday_months['Aug'] = 1
birthday_months['Sep'] = 2
birthday_months['Oct'] = 2
birthday_months['Nov'] = 1
birthday_months['Dec'] = 3


print(birthday_months)


# ## Which month has the most birthdays??

# ### Iterating through dictionary keys 

# Use `.keys()` to fetch the keys in a dictionary. You can iterate through the dictionary keys like a list.

# In[15]:


month_keys = birthday_months.keys() # get the keys from the dictionary
print(month_keys)

for month in birthday_months.keys(): # iterate through the keys using a for loop
    print(month)
    print(birthday_months[month])
    

birthday_max = 0
max_month = ''
for month in birthday_months.keys():
    if birthday_months[month] > birthday_max:
        max_month = month
        birthday_max = birthday_months[month]

print(max_month)


# ### Iterating through dictionary values

# Use `.values()` to fetch the values in a dictionary. You can iterate through the values this way 
# (NOTE: this is not very common).

# In[16]:


month_vals = birthday_months.values()
print(month_vals)

for val in birthday_months.values():
    print(val)

print(type(birthday_months.values()))
max_birthdays = max(birthday_months.values())
print(max_birthdays)

for month in birthday_months.keys():
    print(month)
    if birthday_months[month] == max_birthdays:
        max_month = month
print(max_month)


# ### Iterating through dictionaries using key-value combinations (most common) 

# Use `.items()` to fetch the *key-value pairs* in a dictionary. This lets you iterate over the keys and their corresponding values all at once!

# In[17]:


key_vals = birthday_months.items()
print(key_vals) # NOTE: these are tuples

# Iterate through them by declaring the key and the value in the for-loop
for key, val in birthday_months.items():
    print(key)
    print(val)

    
max_month = ''
max_birthdays = 0
for month, count in birthday_months.items():
    if count > max_birthdays:
        max_month = month
        max_birthdays = count

print(max_month)
print(max_birthdays)


# 
# ----------------------------------------------------------------------------------------------------------------------
# 

# # Sorting items in a dictionary

# One common challenge with a dictionary is to identify the smallest or largest values in the dictionary. 
# 
# For example, say we want to know which **3** birthday months have the most birthdays. *How can we do this?*
# 
# We'll use our old friend `sorted` and a new friend, `itemgetter`.

# ### Sorting by keys 

# In[18]:


print(sorted(birthday_months.keys()))
print(sorted(birthday_months.items()))


birthdays_sorted = {}
for month, count in sorted(birthday_months.items()):
    birthdays_sorted[month] = count
    
print(birthday_months)
print(birthdays_sorted)


# This sorts our keys alphabetically (if keys were numeric, it would be in numeric order, etc.). But that's not what we want!

# ### Sorting by values

# To sort by values, we need to introduce a new tool in our toolbox: the `itemgetter`. 
# 
# We use this to tell python to sort by the *values* in our dictionary, rather than the keys.

# In[19]:


from operator import itemgetter # this imports the itemgetter function

"""
This says: 
a. sort the items in the dictionary, 
b. but use the element at index 1 (the second element of our key-value pair) as the basis for sorting
"""
print(sorted(birthday_months.items(), key=itemgetter(1))) # this is sorting by value




print(sorted(birthday_months.items(), key=itemgetter(0))) # this is the same as sorting by key above










# We can sort in the other direction as well with reverse=True (this sorts from high to low)
print(sorted(birthday_months.items(), key=itemgetter(1), reverse=True))
type(sorted(birthday_months.items(), key=itemgetter(1), reverse=True)) # Note this is a list!

sorted_dict = sorted(birthday_months.items(), key=itemgetter(1), reverse=True) # this is a list
print(type(sorted_dict))
print(sorted_dict[0]) # the first item in the list
print(type(sorted_dict[0]))
print(sorted_dict[0][1]) # the value at index 1 (second item) from the first item in the list


# In[20]:


birthday_times = {
    'Talia': ('10/16/1998', '3:42 AM'),
    'Erik': ('3/21/1991', '2:00 AM')
}

print(birthday_times)

sorted(birthday_times.values())

print(sorted(birthday_times.items(), key=itemgetter(1)))



# In[21]:


print(sorted(birthday_months.items()))

print(sorted(birthday_months.items(), key=itemgetter(0))) # Use the key (element 0) to sort each item

print(sorted(birthday_months.items(), key=itemgetter(1))) # Use the value (element 1) to sort each item


# **Using the tools above, what are our top three birthday months?**

# In[22]:


top_3_months = []

# Sort the items in the dictionary, by their value, from highest to lowest
sorted_months = sorted(birthday_months.items(), key=itemgetter(1), reverse=True)
# print(sorted_months)
for key, value in sorted_months[0:3]:
    top_3_months.append(key) # Add the month

print(top_3_months)

# for item in sorted_months[0:3]:
#     top_3_months.append(item) # Add the month

# print(top_3_months)

