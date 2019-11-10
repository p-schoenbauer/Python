#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[61]:


N = 2000
x_min = -1
x_max = 1 
x = np.linspace(x_min,x_max,N)
y = np.cos(x) + 0.9 * (np.random.rand(N)-0.5)
a = [4,8,12]
p = [np.poly1d(np.polyfit(x,y,i)) for i in a]


# In[64]:


t = np.linspace(x_min,x_max, 200)
fig= plt.figure(figsize=(17,8))
plt.plot(x,y,".")
#plt.plot(t, np.cos(t), "-")
for q in p:
    plt.plot(t,q(t),"-", )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




