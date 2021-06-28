#!/usr/bin/env python
# coding: utf-8

# # P04: dictionaries, sets, and files
# - **Concepts**: ordered vs not, hash
# - **Python dict, set**: hashable, set, dict, .update(), del
# - **Python files**: open, close, with open as fp
# 
# 
# 
# ### Reading files
# 
# #### Finding a file
# 
# - Files are stored somewhere in your computer systems hard drive or storage area.
# 
# - That location is specified via a file **path**.
# 
# - A file path encodes the location of the file within the directory structure on the computer.
# 
# - *Absolute* file paths encode the location of the file relative to the root, or base directory of the file system.  So let's say we have a file named `filename.ext` located in `folder2`, which is located inside `evul`, which is inside `Users`, which is in the base (root) directory of the file system.  On a unix machine (such as Mac OS, Linux, etc.) this location is encoded as follows `/Users/evul/folder2/filename.ext` where the slashes (`/`) indicates directories or folders.  Windows machines use the forward slash, so that path would look like `C:\Users\evul\folder2\filename.ext`.
# 
# - *Relative* file paths encode the location of the file relative to the current location or path, where the program is running.  So if a program has been launched in the folder `/Users/evul/programs/`, then the relative path to `/Users/evul/folder2/filename.ext` would involve going up one directory in the file tree `..`, then down into `folder2` and getting `filename.ext`.  The full relative path would be `../folder2/filename.ext`.  The key part here is that `..` refers to the parent directory.
# 
# #### Opening a file
# 
# - Files are accessed via the `open(file, mode)` command, specifying the (relative or absolute) path to the  file, and the mode with which you want to open it ('r' for read, 'w' for write, 'a' for append, there are [more](https://docs.python.org/3/library/functions.html#open)).
# 
# - Opening a file creates a file object which can be read from (or written to).  Assuming we are dealing with text files, `file.read()` reads the entire content of the file as one string.  `file.readlines()` reads the entire content of the file as a list of strings, with each element corresponding to one line in the text file.  `file.readline()` reads one line at a time, and is helpful if your file is large, and you do not want to load its entirety into memory.
# 
# - When you open a file, your operating system is notified that some program is doing something to that file, and it will prevent other changes from being made to that file. Consequently, it is important that you *close* the file after opening it.  In Python, the easiest way to make this that this is done without errors is via the `with` keyword, that creates a temporary context in which the file is open, and then closes the file as soon as all the operations that need to be carried out on the file are completed.
# 
# To avoid overloading you with options and alternatives, we will presume that all text files are read as follows:

# In[1]:


with open('../datasets/example.txt', 'r') as fp:
    file_contents = fp.readlines()

print(file_contents)


# this creates the variable `file_contents` which contains a list, with each element of that list being a line of the file (here, the file is `example.txt` located in a sibling directory called `datasets`.  Note the escape sequence `'\n'` in the strings -- these are the *newline* escape character, and is how we encode line breaks inside strings.
# 
# 
# 
# 
# 
# ## An important aside: File Paths

# <div class="alert alert-success">
# The specific location of a file or folder on your computer. </div>

# When using a Graphical User Interface (GUI), you click on directories to access subdirectories and finally find the file you're interested in.

# When using the command line, you specify a file's path explicitly with text.

# ### Absolute vs. Relative Paths
# 
# The two ways to specify the path to your file of interest allow for flexibility in programming.

# #### Absolute Paths

# <div class="alert alert-success">
# <b>Absolute paths</b> specify the <b>full</b> path for a given file system (starting from the root directory).
# </div>

# **root** specifies the 'highest' directory in the file structure (the start).
# 
# An absolute file path starts with a slash `/` specifying the root directory.
# 

# In[2]:


## absolute path
## this is specific to my computer
## look at the path output above for you computer
get_ipython().system('ls /Users/shannonellis/Desktop/Teaching/COGS18/Materials')


# #### Relative Paths

# <div class="alert alert-success">
# <b>Relative paths</b> specify the path to a file from your <b>current working directory</b> (where your computer is working right now).
# </div>

# In[3]:


# remind us of our current working directory
get_ipython().system('pwd')


# In[4]:


# relative path
# this is specific to my computer
get_ipython().system('ls ../../COGS108/Lectures-Sp21')


# - `..` specify you want to move one directory up in your hierarchy
# - `COGS108/Lectures-Sp21` specifies the path to the directory I want to list files in
# - each directory is separated with a slash (`/`)

# This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

# #### Clicker Question #1
# 
# Given the following file structure:
# 
# - `/`
#     - `scripts/`
#         - cool_thing.py
#         - super_cool_thing.py
#     - `images/`
#         - image1.png
#         - image2.png
#     - `notebooks/`
#         - 00_intro.ipynb
#         - 01_variables.ipynb
# 
# 
# If your current working directory is `notebooks`, what is the **absolute path** to `cool_thing.py`?
# 
# - A) `/scripts/cool_thing.py`
# - B) `scripts/cool_thing.py`
# - C) `cool_thing.py`
# - D) `../scripts/cool_thing.py`
# - E) ¯\\\_(ツ)\_/¯

# #### Clicker Question #2
# 
# Given the same file structure:
# 
# - `/`
#     - `scripts/`
#         - cool_thing.py
#         - super_cool_thing.py
#     - `images/`
#         - image1.png
#         - image2.png
#     - `notebooks/`
#         - 00_intro.ipynb
#         - 01_variables.ipynb
# 
# 
# If your current working directory is `notebooks`, what is the **relative path** to `cool_thing.py`?
# 
# - A) `/notebooks/../scripts/cool_thing.py`
# - B) `scripts/cool_thing.py`
# - C) `/scripts/cool_thing.py`
# - D) `../scripts/cool_thing.py`
# - E) ¯\\\_(ツ)\_/¯

# 
