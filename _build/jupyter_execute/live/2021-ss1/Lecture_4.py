#!/usr/bin/env python
# coding: utf-8

# # Lecture 4: strings
# 
# ## making strings, quotes, escaping

# In[1]:


one = 'this is a string'
two = "this is another string"

print(one, two)


# In[2]:


quoted_string = "ed's class is listening"
print(quoted_string)


# In[3]:


quoted_string = 'ed\'s quote is "escape characters"'
print(quoted_string)


# In[4]:


another_string = 'the escape character is \\'
print(another_string)


# In[5]:


quoted_string = "ed's quote is " + '"escape characters"'
print(quoted_string)


# In[6]:


quoted_string = """ed's quote is "escape characters" 
and new lines
and more"""

print(quoted_string)


# ## putting variables in strings

# In[7]:


age = 18
name = "Alice"

print(name + " is " + str(age))


# In[8]:


print(f'{name} is {age}')


# In[9]:


print(f'{name=}')


# ## sorted(), encoding and order

# In[10]:


sentence = "I opened jupyter notebook and typed a sentence"

sorted(sentence)


# In[11]:


ord('a')


# In[12]:


words = ['one', 'four', 'apple', 'zebra', 'banana']
sorted(words)


# ## lower, upper, title, etc.

# In[13]:


weird_string = "ABDH AhahBAhj dbahdbahasu haAKJ iuABSF"
print(weird_string.title())


# In[14]:


# I want to sort these in intuitive alphabetical order.
# convert them all to the same case.  lower upper title

words = ['One', 'four', 'apple', 'Zebra', 'Banana', 'Rhino']

for index in range(0,len(words)):
    words[index] = words[index].title()

words.sort()
print(words)    


# ## replace 
# 
# (and string.punctuation)

# In[15]:


sentence = 'Who\'s going to say, or eat, "cheese" -- the dairy product?'
print(sentence)


# In[16]:


from string import punctuation

for mark in punctuation:
    # print('replacing: ' + mark)
    sentence = sentence.replace(mark, '')

print(sentence)


# In[17]:


newstring = ''
for item in sentence:
    if item.isalpha() or item == ' ':
        newstring = newstring + item
print(newstring)


# ## in, index, find

# In[18]:


sentence = "I like to eat apples and bananas and pears and strawberries and cake"

print(sentence)


# In[19]:


'pineapple' in sentence


# In[20]:


sentence.index('pineapple')


# In[21]:


sentence.find('pineapple')


# ## splitting and joining strings

# In[22]:


sentence = "I like to eat apples and bananas and pears and strawberries and cake"


# In[23]:


words = sentence.split(' ')


# In[24]:


print(words)


# In[25]:


' '.join(words)


# In[26]:


' '


# # Hard example
# 
# Let's count the unique words in the poem below.   
# 
# Later we will learn to use *dictionaries* to make this easier, but for now, we will sort and count.
# 
# Specifically we will:
# 1. extract all the lowercase words
# 2. split them into a list
# 3. sort the list
# 4. iterate through the list to count the number of times each unique word appeared
# 5. store the results in a new list.

# In[27]:


frost = """
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.
"""
print(frost)


# In[28]:


from string import punctuation
# convert to lowercase?
frost = frost.lower()
# get rid of newline
frost = frost.replace('\n', ' ')
# remove punctuation
for mark in punctuation:
    frost = frost.replace(mark,'')

frost = frost.replace('—', '')

# split on ' '
words = frost.split(' ')

# count these words
unique_words = dict()

for word in words:
    if word != '':
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] = unique_words[word] + 1
    
#print(unique_words)
    
word_counts = []
for key in unique_words:
    word_counts.append([unique_words[key], key])

word_counts.sort()
print(word_counts)


# # how to count unique items?
# 

# In[29]:


names = ['Alice', 'Bob', 'Carol', 'Bob', 'James', 'Joan', 'Alice', 'Bob', 'Joan']

# we want a list of lists: [[2, 'Alice'], [3, 'Bob'], [1, 'Carol'], [1, 'James'], [2, 'Joan']]


# ## approach 1:
# 
# sort list, loop through list and count repetitions.

# In[30]:


names.sort()

unique = []

prev = ''
count = 0

for name in names + ['#END']: 
    print(name, prev, count)
    if name == prev:
        count = count + 1
    else:
        if count > 0:
            unique.append([count, prev])
        count = 1
        prev = name

print(unique)


# ## approach 2
# 
# use a dictionary. (which we will cover in more detail later), use name as key for dictionary, and increment

# In[31]:


name_counts = dict()

name_counts['Alice'] = 2
name_counts['Bob'] = 3

print(name_counts)

print('Carol' in name_counts)


# In[32]:


name_counts = dict()

for name in names:
    #print(name)
    if name not in name_counts:
        name_counts[name] = 1
    else:
        name_counts[name] = name_counts[name] + 1
    #print(name_counts)
    
print(name_counts)
        


# In[33]:


print(name_counts)


# Then convert dictionary to the list we wanted.

# In[34]:


unique = []

for key in name_counts:
    # print(key, name_counts[key])
    unique.append([name_counts[key], key])
    
print(unique)


# ## approach 3:
# 
# use Counter object from collections, which is a dictionary that does the counting for us

# In[35]:


from collections import Counter

name_counter = Counter(names)

print(name_counter)


# Then convert to the list format we wanted, as we did for dictionaries

# In[36]:


unique = []

for key in name_counter:
    # print(key, name_counts[key])
    unique.append([name_counter[key], key])
    
print(unique)

