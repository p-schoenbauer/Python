#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


A = np.ones((2,3))
B = np.ones((3,4))
A.dot(B)


# In[11]:


B = np.ones((2,3))
B[1,2] = 0
A==B
np.logical_and(A,B)


# In[13]:


C = np.exp(B)
C


# In[17]:


D = np.random.random((4,4))
D


# In[18]:


D.T


# In[23]:


print(D.sum())
print(D.sum(axis=0))
print(D.sum(axis=1))


# In[24]:


D[:,0].sum()


# In[25]:


D.max()


# In[26]:


D.max(axis=1)


# In[27]:


D.argmin()


# In[29]:


np.median(D)


# In[30]:


np.std(D)


# In[33]:


np.mean(D)


# In[41]:


np.cumsum(D, axis=1)


# In[37]:


D


# In[39]:


x = np.array([1,2,3,4,5])
np.cumsum(x)


# In[49]:


data = np.loadtxt(r"d:\_data\indices\FTSE100preproc")


# In[50]:


data


# In[56]:


print(data.mean(axis=0))
print(data.std(axis=0))


# In[64]:


earningsAbs = data[1:,0] - data[:-1,0]
earnings = earningsAbs/data[:-1,0]


# In[65]:


print(earnings.mean())
print(earnings.std())


# In[66]:


plt.plot(earnings)


# In[81]:


n_avg = [200,500]
earnings_abs_cumavg = []
for n in n_avg:
    earnings_abs_cumavg.append((np.cumsum(earningsAbs)[n:]-np.cumsum(earningsAbs)[:-n])/n)
for y in earnings_abs_cumavg:
    plt.plot(y)


# In[82]:


a = np.arange(100).reshape(10,2,5)
a


# In[87]:


np.resize(a,(10,10,10))


# In[92]:


a.ravel()


# In[93]:


get_ipython().run_line_magic('pinfo', 'a.ravel')


# In[97]:


A = np.arange(5)[:,np.newaxis] + np.arange(1,12,5)
A


# In[100]:


a = np.arange(25).reshape(5,5)
b = np.array([1.,5,10,15,20])
c = a/b[:,np.newaxis]
a,b,c


# In[102]:


a = np.random.random((10,3))
a


# In[110]:


b = np.abs( a - 0.5 )
c = np.argsort(b, axis = 0)
d = a[c[0,:],:]
c[0,:], d


# In[ ]:





# In[ ]:





# In[ ]:




