#!/usr/bin/env python
# coding: utf-8

# # P04: Reading and writing files
# - **Python files**: open, close, with open as fp
# 
# 
# ## Reading files
# 
# ### Finding a file
# 
# - Files are stored somewhere in your computer systems hard drive or storage area.
# 
# - That location is specified via a file **path**.
# 
# - A file path encodes the location of the file within the directory structure on the computer.
# 
# - *Absolute* file paths encode the location of the file relative to the root, or base directory of the file system.  So let's say we have a file named `filename.ext` located in `folder2`, which is located inside `jserences`, which is inside `Users`, which is in the base (root) directory of the file system.  On a unix machine (such as Mac OS, Linux, etc.) this location is encoded as follows `/Users/jserences/folder2/filename.ext` where the slashes (`/`) indicates directories or folders. Windows machines use the forward slash `\`, so that path would look something like `C:\Users\jserences\folder2\filename.ext`.
# 
# - *Relative* file paths encode the location of the file relative to the current location or path, where the program is running. So if a program has been launched in the folder `/Users/jserences/programs/`, then the relative path to `/Users/jserences/folder2/filename.ext` would involve going up one directory in the file tree using the `..` syntax, then down into `folder2` and getting `filename.ext`.  The full relative path would be `../folder2/filename.ext`.  The key part here is that `..` move you up one level in the directory tree **relative** to the the current working directory. Basically `..` is like pressing the `back` arrow on a 'Finder' window when you're moving around using the mouse and the windows provided by your operating system.
# 
# ### Opening a file
# 
# - Files are accessed via the `open(file, mode)` command, specifying the (relative or absolute) path to the  file, and the mode with which you want to open it ('r' for read, 'w' for write, 'a' for append, there are [more](https://docs.python.org/3/library/functions.html#open)).
# 
# - Opening a file creates a file object which can be read from (or written to, or appended to, depending on what mode you used to open it).  
#     - Assuming we are dealing with text files, `file.read()` reads the entire content of the file as one string. 
#     - `file.readlines()` reads the entire content of the file as a list of strings, with each element corresponding to one line in the text file.  
#     - `file.readline()` reads one line at a time, and is helpful if your file is large, and you do not want to load its entirety into memory.
# 
# - When you open a file, your operating system is notified that some program is doing something to that file, and it will prevent other changes from being made to that file. Consequently, it is important that you *close* the file after opening it.  In Python, the easiest way to make this that this is done without errors is via the `with` keyword, that creates a temporary context in which the file is open, and then closes the file as soon as all the operations that need to be carried out on the file are completed. Bad things can happen if you do not close the file, so make sure you're careful with this (the file might get corrupted, you might find that nothing was written to the file, etc). 

# ## File Paths

# The specific location of a file or folder on your computer.

# When using a Graphical User Interface (GUI), you click on directories to access subdirectories and finally find the file you're interested in.

# When using the command line, you specify a file's path explicitly with text.

# ### Absolute vs. Relative Paths
# 
# The two ways to specify the path to your file of interest allow for flexibility in programming.

# #### Absolute Paths

# Absolute paths specify the full path for a given file system (starting from the root directory).

# **root** specifies the 'highest' directory in the file structure (the start).
# 
# An absolute file path starts with a slash `/` specifying the root directory.
# 

# In[1]:


## absolute path
## this is specific to my computer
## look at the path output above for you computer
get_ipython().run_line_magic('ls', "'/Users/johnserences/Dropbox/My Papers/Editorial/'")


# #### Relative Paths

# **Relative paths** specify the path to a file from your **current working directory** (where your computer is working right now).
# 

# In[2]:


# remind us of our current working directory
get_ipython().run_line_magic('pwd', '')


# In[3]:


# relative path
# this is specific to my computer
get_ipython().run_line_magic('ls', '../../Lectures')


# - `..` specify you want to move one directory up in your hierarchy - here I am moving up two levels with the `../../` syntax
# - `Lectures` specifies the path to the directory I want to list files in
# - each directory is separated with a slash (`/`)

# This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

# ## Opening and interacting with files!
# * Using the `with` method of opening files will ensure that they are closed properly when you are done with them...
# * This will create a file object `f` (although you can name it whatever you'd like)
# * You can then use the file object `f` to write stuff to the file using `f.write()`

# ### Open a file for writing, and just write some text to it using the f-string method we learned last time...

# In[4]:


with open('test.txt', 'w') as f:
    for i in range(0, 11):
        # include the \n newline character.
        # its like pressing the `enter` key at the end of each line
        f.write(f'This is the {i}th line of the file\n')


# Note the escape sequence `'\n'` in the strings -- these are the *newline* escape character, and is how we encode line breaks inside strings.

# ### You can use the built in magic `%pycat` to view the contents of the file. 

# In[5]:


get_ipython().run_line_magic('pycat', 'test.txt')


# ### Open a file for reading...
# * `f.read()` will read in a fixed number of elements...where `f.read(x)` will read in `x` elements
# * if not parameters are passed to `f.read()` then it will read the entire file! be careful with this if you're dealing with super big files!
# * `f.readline()` will read in one line at a time (and it knows how to find the end of each line because its looking for the the `\n` newline escape character...that's why it is so important to include the `\n` in your files when you write them...makes it way easier to deal with when reading the data back in. 
# * `f.readlines()` will read in the entire file and will store each line as a string that is an entry in a list...

# #### `f.read()`

# In[6]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read the entire file...
    out = f.read()
    
# print it out
print(out)


# #### This time use `f.read() but specify a fixed number of elements to read (instead of the entire file). 

# In[7]:


# make a variable to determine how many elements to read.
num_elements_to_read = 10

# open our file for reading...
with open('test.txt', 'r') as f:
    # This time just read in a set number of elements
    out = f.read(num_elements_to_read)
    
# print it out - note that there are 
# num_elements_to_read characters (including spaces)
print(out)


# ### `f.readline` - read one line

# In[8]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read a line from the file
    out = f.readline()
    
# print it out
print(out)


# #### Side note, but sorta related to `f.readline()`...if you want to loop over lines, one at a time, use a for loop like this:

# In[9]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read in line by line...
    for line in f:
        print(line, end="")
        # end = "" tells the `print` statement not to end each 
        # line with a '\n' because there is already a '\n' character
        # at the end of each line because that is how we wrote it out...


# ### `f.readlines()` - read entire file into a list of strings, where each string is a line from the file. 

# In[10]:


# open our file for reading...
with open('test.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    out = f.readlines()
    
# print the list of strings
print(out)

# because `out` is now a list, 
# you can index/slice to find specific 
# elements
print('\nSlicing the list to grab a subset of the strings...\n')
print(out[2:4])


# ## Working with files once they have been read in...
# 
# ### Find a target string and then keep the next N lines of text
# * Here we will read in txt from a book (Frankenstein by Mary Wollstonecraft (Godwin) Shelley)
# * We'll then search for a specific string in the book...in this case we'll look for the first sentence of Chapter 5
# * We'll use `.readlines()` to read the book into a list, where each line of text from the book is an entry in the list (and remember, `.readlines()` is parsing the text based on where the `'\n'` (newline) characters are). 
# * Then we'll get rid of everything else in the book except for the few lines at the start of Chapter 5
# * I will show you two methods...one using a counter that we initialize, and one using the `enumerate` method that allows you to have a counter in a `for` loop that is initialized and incremented automatically. 
# * I'll also show you the `break` syntax for a `for` loop. `break` allows you to exit the loop if a certain condition is met. In this case, we will exit the loop when we find the text that we're looking for!
# * Last - there are many ways to do this task...so don't feel constrained by this approach when you're working on the problem set...

# In[11]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    book = f.readlines()

# now we can search the book for the text that we want, 
# which in this case is the first sentence of Chapter 5, which 
# starts with the string 'It was on a dreary night' 
search_target = 'It was on a dreary night'

# how many lines of text do we want to keep 
# after we find the search target?
keep_lines = 50

# initialize a counter (int object)
cnt = 0

# loop over each line in the book
for line in book:
    
    # test to see if the current line has search_target in it
    if search_target in line:
        # grab the line where chapter 5 starts
        start_index = cnt
        
        # exit the for loop by calling 'break'
        break
        
    # if the current line does not have our search_target
    # then we'll increment the counter to keep track of how
    # many lines we've read...
    else:
        cnt += 1
        
# now use slicing to just keep the first keep_lines lines 
# after the search_target
book = book[start_index:start_index + keep_lines]

print(book)

# Related to ps3, Q1: How would you do the slicing if you 
# wanted to keep **all** of the text in the book after search_target?
# And how would do the slicing if you wanted to keep all of the text
# after the search_target while excluding the line that contained the 
# search_target? 


# ### Find a target string and then keep the next N lines of text but this time use `enumerate`
# * See [here](https://realpython.com/python-enumerate/) for a nice explanation...

# In[12]:


# open our file for reading...
with open('frankenstein.txt', 'r') as f:
    # read the entire file...with each line 
    # returned as a string in a list
    # we'll call the list 'book'
    book = f.readlines()

# now we can search the book for the text that we want, 
# which in this case is the first sentence of Chapter 5, which 
# starts with the string 'It was on a dreary night' 
search_target = 'It was on a dreary night'

# how many lines of text do we want to keep 
# after we find the search target?
keep_lines = 50

# loop over each line in the book using enumerate
# enumerate will automatically create and increment a counter 
# that we'll call 'cnt' and it will give you each line
# in the book just like a normal for loop. 
for cnt, line in enumerate(book):
    
    # test to see if the current line has search_target in it
    if search_target in line:
        # grab the line where chapter 5 starts
        start_index = cnt
        
        # exit the loop by calling 'break'
        break
        

# now use slicing to just keep the first keep_lines lines 
# after the search_target
book = book[start_index:start_index + keep_lines]

print(book)

# Related to ps3, Q1: How would you do the slicing if you 
# wanted to keep **all** of the text in the book after search_target?
# And how would do the slicing if you wanted to keep all of the text
# after the search_target while excluding the line that contained the 
# search_target? 


# ### Counting words in text...
# * Here we can count the occurence of each word in the book (or in the part of the book that you have left after slicing the book list in the code cell above). 
# * Notice that there are some empty strings `''` in the list that we need to deal with (i.e. things that are not words, so we need to check for these so they don't get counted). We can do that in a few ways that I'll write out below. 
# * Our general algorithm here will be: 
#     * convert the list to a string to make it easier to clean
#     * remove the newline characters using the `.replace()` method (and if you are working with a string that has other stuff in it that you don't want you can define a string with all the unwanted characters and loop over each_letter in that string to `.replace()` each unwanted character using a `for` loop). 
#     * convert back to a list
#     * initialize an empty dictionary
#     * loop over all unique words in the book - use `set` to get the unique words
#         * in this loop check to make sure we're not considering the empty strings `''`
#     * whenever we find a real word, create a new `key:value` pair in a dictionary with the word as the `key` and an initial value of `0`
#     * Now that the dictionary is set up and we have one key for each unique word, we can loop over **all** the words in the book, including repeated words, and increment the `value` associated with each `key`

# In[13]:


# turn the book list into a string to make it easier to remove things we don't want (like newline 
# characters)
book_str = ''.join(book)

# convert to lower case
book_str = book_str.lower()

# clean out the newline characters
book_str = book_str.replace('\n', ' ')

# turn back into a list based on the location of spaces
book_lst_clean = book_str.split(' ')

# init a dictionary with a key for each unique 
# word, and 0 for the starting count
wc = {}
for w in set(book_lst_clean):
    # because there are some empty strings in our list
    # we can check here and we'll skip them 
    if w != '':
        wc[w] = 0

# now loop over **all** words in the book, even the repeated words
# and count them up!
for w in book_lst_clean:
    if w != '':
        wc[w] += 1

# have a look at the dictionary...
print(wc)


# ### A slightly more compact way to count all the words in text using just one `for` loop
# * This might be easier to understand (or it might be harder) so just writing it out in case it helps...
# * I am using the `continue` statement (see below)...
# * Note that there are several other ways you could achieve the same result, so long as you are checking to make sure that the current word is not an empty string `''` somehow

# In[14]:


# turn the book list into a string to make it easier to remove things we don't want (like newline 
# characters)
book_str = ''.join(book)

# convert to lower case
book_str = book_str.lower()

# clean out the newline characters
book_str = book_str.replace('\n', ' ')

# turn back into a list based on the location of spaces
book_lst_clean = book_str.split(' ')

# init an empty dictionary
wc = {}   # or you can use dict()

# now loop over **all** words in the book, even the repeated words
# and count them up!
for w in book_lst_clean:
    
    # if w is not a word (i.e. it is an empty string)
    # then continue, where continue means "go back to the 
    # top of the for loop and skip the rest of the code in
    # the loop"
    if not w:
        continue
    
    # if w is a word, and its not already in our dictionary
    # then make a new key and assign a value of 0
    if w not in wc:
        wc[w] = 0
    
    # increment a counter each time the word w appears...
    # note that you only get to this line of code if w
    # is indeed a word (the if not w: continue
    # line above will prevent you from getting here if w is
    # not a word)
    wc[w] += 1

# have a look at the dictionary...
print(wc)


# ### Find the most common word in text. 
# * To find the most common word, you can loop over our word count dictionary (`wc`, defined above)
# * Basic approach: 
#     * Initialize a counter (lets call it `max_count`) to `0`
#     * Loop over `key:value` pairs in `wc` using the `.items()` method
#     * If the current `value` exceeds `max_count`, then update `max_count` with that value and also store the current `key`

# In[15]:


# init max_count to 0
max_count = 0

# loop over the key:value pairs in wc
for k,v in wc.items():
    
    # if the current value exceeds the previous value of 
    # max_count, then reassign max_count to the current value
    # and save the associated key (which is the actual word)
    if v > max_count:
        max_count = v
        most_common_word = k
        
print(f'The most common word is "{most_common_word}", it occured {max_count} times')
    

