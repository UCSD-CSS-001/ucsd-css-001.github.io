#!/usr/bin/env python
# coding: utf-8

# # CSS1 Lecture 2
# 
# **Lab 1:**
# - fetch feedback.
# 
# - start early.
# 
# - read carefully

# ## Control flow
# 
# - notes!

# ## If..elif..else

# In[1]:


age = 17


# our goal is to:
# print:
#  "you cannot vote and you cannot drink"
#  "you can vote but you cannot drink"
#  "you can vote and drink!"


# In[2]:


canvote = True

# print:
#  "you cannot vote"
#  "you can vote!"

if True:
    print("you cannot vote")
    print("You still cannot vote")
    print("you really really cant vote")

print("we print this either way")


# In[3]:


canvote = True

if canvote:
    print("you can vote!")
else:
    print("you cannot vote")
    
print("congratulations either way")


# In[4]:


# print:
#  "you cannot vote and you cannot drink"
#  "you can vote but you cannot drink"
#  "you can vote and drink!"

cannotvote = True
cannotdrink = True

if cannotvote:
    print("you cannot vote and you cannot drink")
elif cannotdrink:
    print("you can vote but you cannot drink")
else:
    print("you can vote and drink!")
    
print("congratulations either way")


# In[5]:


cannotvote = True
cannotdrink = True

if cannotvote:
    print("you cannot vote and you cannot drink")

if cannotdrink:
    print("you can vote but you cannot drink")
else:
    print("you can vote and drink!")
    


# In[6]:


pet_type = 'dfgfdskljhgfiuhgb'


if pet_type == 'dog':
    print('woof')
elif pet_type == 'cat':
    print('meow')
elif pet_type == 'goat':
    print('baa')
elif pet_type == 'pig':
    print('oink')
else:  # equivalent to elif True:
    print('squeek')


# In[7]:


pet_type = 'cat'
pet_size = 'tiny' 

if pet_type == 'dog':
    if pet_size == 'small':
        print('arf')
    else:
        print('woof')
elif pet_type == 'cat':
    if pet_size == 'small':
        print('meow')
    else:
        print('raar')
else:  # equivalent to elif True:
    print('squeek')


# ## Comparison operators

# In[8]:


print(5 < 6)
print(6 > 7)
print(7 < 5)


# In[9]:


x = 5 >= 4


# In[10]:


5 == int('5')


# In[11]:


5 != 4


# In[12]:


'z' in 'abracadabra'


# ## Logical operators

# In[13]:


country = 'Elbonia'

age = 18

age >= 18 or country == 'Elbonia'


# In[14]:


print(True or False)
print(False or True)
print(True or True)
print(False or False)


# In[15]:


print(True and False)
print(False and True)
print(True and True)
print(False and False)


# In[16]:


print(not True)
print(not False)


# In[17]:


# US scenario
age = 15

print(age)

if age >= 21:
    # 21, 22, ...:   you can vote and drink!"
    print("you can vote and drink!")
elif age < 18:
    # .. 15, 16, 17:   "you cannot vote and you cannot drink"
    print("you cannot vote and you cannot drink")
else: #equivalently: elif age >= 18 and age < 21:
    # 18, 19, 20:   "you can vote but you cannot drink"
    print("you can vote but you cannot drink")


# ## Lists

# In[18]:


x = 45


# In[19]:


y = 5.0


# In[ ]:





# ### making lists

# In[20]:


ages = [15, 18, 25, 78, 7, 45]
print(ages)


# In[21]:


type(ages)


# In[22]:


len(ages)


# ### index

# In[23]:


ages[2]


# In[24]:


print(ages)
ages[3] = 67
print(ages)


# ### append to list

# In[25]:


print(ages)
ages.append(2000)
print(ages)


# In[26]:


print(ages)
ages.remove(2000)
print(ages)


# In[27]:


ages = ages[0:6]


# In[28]:


ages


# ## For loops

# In[29]:


for number in [1, 2, 3, 4]:
    print(number)


# In[30]:


for x in ages:
    print(x)


# In[31]:


ages


# In[32]:


print('Processing all ages')

for age in ages:
    print('-----------------------')
    print('You are ', age, ' years old')
    if age >= 21:
        print("you can vote and drink!")
    elif age < 18:
        print("you cannot vote and you cannot drink")
    else: 
        print("you can vote but you cannot drink")
    
print('Done!')


# In[33]:


# modulus operator

# range()


# In[34]:


# print out all the numbers between 1 and 1000 that are divisible by 71?


# In[35]:


# print out all the numbers between 1 and 1000 (inclusive)

for number in range(1, 1001):
    print(number)


# ### range command to set up an iterable
# 
# ### Modulus

# In[36]:


# divisible by 71?

number = 71*212121 + 4

(number % 71) == 0


# In[37]:


# print out all the numbers between 1 and 1000 that are divisible by 71?

for number in range(1, 1001):
    if (number % 71) == 0:
        print(number)


# In[38]:


# make a list of all the numbers between 1 and 1000 
# that are divisible by 93?

# make a list with some name
number_list = []

for number in range(1, 1001):
    if (number % 93) == 0:
        # print(number)
        number_list.append(number)
        # add the number to a list.  

print(number_list)


# ## while loops

# In[39]:


for x in range(10):
    print(x)


# In[40]:


i = 0

while i < 100:
    print(i)
    i = i + 1


# In[41]:


i = 0

# infinite loop
#while i < 100:
#    print(i)
#    i = i - 1


# ## debugging
# 
# - print 
# 
# - rubber ducky
# 
# - minimum reproducible example

# In[42]:


x = 'this is a sentence'


# In[43]:


ages = [45, 235 , 18, 56, 457, 568, 34, 23, '56', 3, 34, 6, 78]


# In[44]:


for age in ages:
    if age >= 18 and age < 21:
        print("you can vote but you cannot drink")
    elif age < 18:
        print("you cannot vote and you cannot drink")
    else:
        print("you can vote and you can drink")


# In[45]:


age = '56'
age >= 18


# In[ ]:




