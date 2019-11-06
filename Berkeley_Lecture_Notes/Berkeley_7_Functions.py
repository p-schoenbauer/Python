#!/usr/bin/env python
# coding: utf-8

# In[5]:


count_add = 0
def add(x,y):
    global count_add   # tell Python that count_add refers to the global namespace
    count_add = count_add + 1
    return [a+b for a,b in zip(x,y)]


# In[8]:


x=[1,2,3,4,5]
y=[1,2,3,4,6]
add(x,y)


# In[9]:


#Gobal variables
count_add


# In[13]:


# Define functions within functions
def multThree(x,y,z):
    def multTwo(a,b):
        return [p*q for p,q in zip (a,b)]
    return multTwo(multTwo(x,y),z)


# In[14]:


multThree([1,2,3],[4,5,6],[7,8,9])


# In[21]:


# Return a function
def addX(x):
    "Returns a function that adds x to a list"
    def add(y):
        return [p+q for p,q in zip(x,y)]
    return add


# In[18]:


myAdd = addX(x)
myAdd(y)


# In[22]:


print(addX.__doc__)


# In[25]:


# Default value for parameters

def funcWithDefaultValue(x=3):
    return x*x
funcWithDefaultValue()


# In[33]:


# Variable number of parameters

def add(*x):
    sum = 0
    for y in x:
        sum = sum + y
    return sum
add(1,2,3,4,5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




