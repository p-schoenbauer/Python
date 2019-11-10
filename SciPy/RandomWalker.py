#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


N = 50   # Number of experiments
K = 1000  # Number of steps

steps = 2*np.random.randint(0,2,(N,K))-1
x = np.cumsum(steps, axis = 1)


# In[34]:


fig= plt.figure(figsize=(17,8))
for a in x:
    plt.plot(a)


# In[35]:


x_avg = np.abs(x).mean(axis=0)
x_avg_sq = (x**2).mean(axis=0) ** 0.5
plt.plot(x_avg)
plt.plot(x_avg_sq)
s = np.arange(K)
plt.plot(s,s**0.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




