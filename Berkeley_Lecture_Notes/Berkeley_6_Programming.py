#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Assignments

x=y=z=0
print(x,y,z)
x,y,z = 1,2,3
print(x,y,z)
x,y,z = [10,20,30]
print(x,y,z)
x,y,z = "ABC"
print(x,y,z)


# In[17]:


import copy

x = [1,2,3,4,5]
y = x                   # Reference
print(y == x, y is x)
y = copy.copy(x)        # Copy
print(y == x, y is x)
y = x[:]                # Copy
print(y == x, y is x)
x[2] = 333
print(x,y)


# In[23]:


x = int(input())
if x>0:
    print("X is positive")
elif x<0:
    print("X is negative")
else:
    print("X is zero")


# In[24]:


file = open("data.txt")
for line in file:
    print(len(line))
file.close()


# In[29]:


x = [1,2,3,4,5]
y = [2,3,4,5,6]
z = []
for i in range(len(x)):
    z.append(x[i]*y[i])
print(z)
w = [p*q for p,q in zip(x,y)]
print(w)


# In[32]:


# List Comprehensions
# [expression for var1 in seq1 if condition1 for var2 in seq2 if condition2 ...]
a = [[1,2,3],[4,5,6]]
b = [p*p for q in a for p in q]
b


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




