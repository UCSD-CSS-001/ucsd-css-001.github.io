#!/usr/bin/env python
# coding: utf-8

# # Plotting with matplotlib
# 
# ## visualization
# 
# data analysis should start with looking at data, and ends with presenting results.  Both of these are done most effectively with *graphs*.  
# 
# There are many skills associated with making graphs and visualizations:
# 
# 1) choosing the right kind of plot.
# 
# 2) transforming data into a representation that exposes the variables you want to plot
# 
# 3) instructing a computer to make the plot you want.
# 
# 4) making the plot **interpretable**, and appealing
# 
# ## Choosing plots
# 
# What are you looking for, or trying to show?
# 
# - the distribution of one variable.  -> histogram
# 
# - the distribution of two variables: how two variables relate to one another  -> scatter
# 
# - how one variable changes as a function of a categorical other variable -> barplot
# 
# - how one variable changes as a function of another numerical variable -> line plot
# 
# 
# 
# ## data
# 
# https://raw.githubusercontent.com/UCSD-CSS-001/ucsd-css-001.github.io/main/live/gapminder.csv
# 
# 
# Standard plots:
# 
# - histogram -> (density plot)  `hist`
# 
# - scatter -> (bubble)  `scatter`
# 
# - line chart -> (+ error bars)  `plot`
# 
# - bar chart -> (+ error bars) `bar`
# 
# - labeling axes.  `xlabel` and `ylabel`
# 
# - log scale `yscale('log')`
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


gapminder = pd.read_csv('gapminder.csv')
gapminder


# In[3]:


gapminder = gapminder.drop(columns = 'Unnamed: 0')
gapminder


# - Life expectancy distribution overall
# 
# What kind of plot?
# 
# **histogram**

# In[4]:


plt.hist(gapminder['lifeExp'])


# In[5]:


counts, bins, bars = plt.hist('lifeExp', bins = range(25, 90, 1), color='purple', data = gapminder)
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Count (number of country-years)')


# TODO:
# - [x] change bins
# - [ ] change colors
# - [ ] make it prettier

# In[6]:


get_ipython().run_line_magic('pinfo', 'plt.hist')


# In[7]:


bins


# In[8]:


counts


# - Life expectancy and gdp Per capita
# 
# what kind of plot to show the distribuion of life expectancy and gdp per capita

# 3^2 = 3*3 = 9
# 
# 10^4 = 10*10*10*10 = 10000
# 
# log(10000, base=10) = 4
# 
# base 10 log = 3
# 
# 

# In[9]:


plt.scatter(x='gdpPercap', y='lifeExp', data = gapminder)
plt.xlabel('GDP per capita')
plt.ylabel('Life Expectancy in years')
plt.xscale('log')


# In[10]:


plt.scatter(x='gdpPercap', y='lifeExp', data = gapminder)
plt.xlabel('GDP per capita')
plt.ylabel('Life Expectancy in years')


# TODO:
# - [ ] change point size
# - [ ] change transparency (alpha

# In[11]:


gapminder.sort_values('gdpPercap', ascending = False).head(10)


# In[12]:


plt.hist('gdpPercap', data=gapminder)
plt.xlabel('gdp per capita')


# - Life expectancy as a function of continent
# 
# what kind of plot is this?   Bar plot
# 
# x axis: continent {africa, asia, europe, n. america, s.america}
# y axis: life expectancy for that continent.  *average*, *mean* life expectancy.
# 
# how do we get our data into this plot format?
# 
# we need to get an average for each continent.

# In[13]:


# how to average per continent?

continent_means = gapminder.groupby('continent').aggregate(mean_life_expectancy = ('lifeExp', 'mean'))

# continent is an *index* not a *column*, which does not play well with matplotlib call
# convert index to column by reset_index
continent_means = continent_means.reset_index()


plt.bar(x = 'continent', height='mean_life_expectancy', data = continent_means)
plt.ylabel('Mean Life Expectancy')
plt.xlabel('Continent')


# - how has life expectancy changed over time (as a function of year) across the world?
# 
# what kind of plot should we use here? histogram, scatter, bar, line
# 
# line plot.
# 
# x axis: year
# y axis: mean life expectancy for that year
# 
# make a new data frame with
# year, and mean_life_expectancy
# 
# 
# what do we need to do to the data to make such a plot?

# In[14]:


# roughly what we are doing.
#for year in set(gapminder['year']):
#    print(year, gapminder[gapminder['year']==year]['lifeExp'].mean())
    
year_averages = gapminder.groupby('year').aggregate(mean_life_expectancy = ('lifeExp', 'mean'))

year_averages


# In[15]:


# convert year to column

year_averages = year_averages.reset_index()

year_averages


# In[16]:


plt.plot('year', 'mean_life_expectancy', data=year_averages)
plt.xlabel('Year')
plt.ylabel('Mean Life Expectancy over all Countries')


# TODO:
# - change color
# - change the point style
# - change the thickness of the line

# - distribution over country's life expectancy and gdp per capita in 2007 (with population scaled bubbles.)
# 
# how to get just 2007?

# In[17]:


year_2007 = gapminder[gapminder['year']==2007]
year_2007


# In[18]:


plt.scatter(x='gdpPercap', y='lifeExp', data=year_2007)
plt.xscale('log')
plt.xlabel('gdp per capita (log scale)')
plt.ylabel('Life expectancy (years)')


# In[19]:


year_2007.sort_values('pop', ascending=False)


# In[20]:


year_2007['dotsize'] = year_2007['pop']/1000000

plt.scatter(x='gdpPercap', y='lifeExp', s='dotsize', data=year_2007)
plt.xscale('log')
plt.xlabel('gdp per capita (log scale)')
plt.ylabel('Life expectancy (years)')


# In[21]:


get_ipython().run_line_magic('pinfo', 'plt.scatter')


# In[22]:


year_2007['dotsize'] = year_2007['pop']/1000000

colormap = {'Asia':'tab:blue', 
            'Africa':'tab:orange', 
            'Oceania':'tab:green', 
            'Americas':'tab:red', 
            'Europe':'tab:purple'}

plt.scatter(x='gdpPercap', y='lifeExp', s='dotsize', c=year_2007['continent'].map(colormap), data=year_2007)
plt.xscale('log')
plt.xlabel('gdp per capita (log scale)')
plt.ylabel('Life expectancy (years)')


# In[23]:


year_2007['continent'].map(colormap)


# In[ ]:




