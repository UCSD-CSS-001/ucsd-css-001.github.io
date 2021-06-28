#!/usr/bin/env python
# coding: utf-8

# # In class code for 01112021
# * in, not in operator
# * slicing lists

# ## The in operator (and not in)
# * also mixed types in a list
# * boolean (True/False)

# In[1]:


a_lst = [18, 'john', 'Kexin', 24]
print(a_lst)

print(18 in a_lst)
print('john' not in a_lst)


# ## Slicing (indexing into lists)
# * use range to make a list of numbers!
# * start, stop, non-inclusive

# In[2]:


x = list(range(0,15)) 

# pull the first three numbers - non inclusive!
print(x[0:3])


# In[3]:


# same thing
print(x[:3])


# In[4]:


# 3rd to end
print(x[2:10])


# ### start, stop, step...non-inclusive
# * can make the start and stop explicit, or can just use : if you want it all...

# In[5]:


# stepping through list of numbers - every other
print(x[0:15:2])


# In[6]:


# same thing (start at begin of list, go to the end, step size of 2)
print(x[::2])
# print(x[4::2]) # specify just the start, go till end
# print(x[:11:2]) # specify just the stop, start at first element. 


# ### Entire list, step size of -1, starting at the end
# * this reverses the list!
# 

# In[7]:


print(x[::-1])


# In[8]:


# step based on counting from the end
print(x[::-2])


# ## For loops
# * repeat an operation or set of operations a specified number of times 
# * iterate over items in a sequence (e.g. a string, a list, etc)
# * syntax can be read: for each item in a sequence, do:
# * indentation

# In[9]:


# iterate over characters in a string
for each_letter in 'funny things happen':
  print(each_letter)
  #print(each_letter.upper())

#print(each_letter)


# ### Loop over elements in a list

# In[10]:


names = ['pauline', 'zhentao', 'mariela']

for name in names:
  print(name)


# ### Apply a method to each item in a list

# In[11]:


names = ['courtney', 'ayoung', 'madison']

for name in names:
  # print each name in title format
  print(name.title())


# ### Generate an "iterable" set of numbers using the 'range' function

# In[12]:


for i in range(0,5):
  print(i)

  print((i*10)+5)


# ### Can use for other purposes as well
# * fill up a list with numbers, after doing some operation on the numbers
# * Introduce the 'append' method for list objects

# In[13]:


lst_squares = []
nums = range(0,6)

print(nums)

for number in nums:
  lst_squares.append(number**2)
  
print(lst_squares)


# ### Use nested for loops to operate over all elements in multiple lists
# * in this example we'll make two lists of numbers and then will multiply every element of the first array with every element of the second array. 

# In[14]:


x = list(range(0,5))
y = list(range(10,15))

for num1 in x:
  for num2 in y:
    print(str(num1), str(num2), 'Product:', str(num1 * num2))


# ### Another example of an embedded loop...
# * introduction to += operator

# In[15]:


# use embedded loops to go over multiple lists (or sequences of numbers, whatever)
x = list(range(0,3))
y = list(range(0,3))

print(x)
print(y)

out = 0
for i in x:
  for j in y:
    # assign after summing current value with RHS
    out += (i*j)
    
print(out)


# ### Use a list of numbers to index into another list 
# * can change the order of the list by changing the range
# * this is often useful when you only want to loop over a subset of an array

# In[16]:


# make a range of numbers
x = range(0,3)
x = range(2,-1,-1) # remember that range starts at the first value, but does not include the stop value (so stops at 0 in this case!)

# make a list of names
names = ['cho-chang', 'valeria', 'sabina']

for num in x:
  # using our range of numbers to index into another list
  print(names[num])

