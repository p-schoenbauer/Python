#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import matplotlib.pyplot as plt
import numpy as np


# In[38]:


N = 10000000;
X = np.random.randn(N)


# In[39]:


Y = []
for p in range(4):
    Y.append(len(X[np.all([X>-p,X<p],axis=0)]) / N)
Y


# In[ ]:





# In[12]:


np.all([X>-1,X<1],axis=0)


# In[101]:


N = 16
K = 10000
X = np.random.randn(K,N)
m = X.mean(axis=1)
w = len(m[np.all([m>-1/2, m<1/2] , axis=0)])
w/K


# In[105]:


N = 1600
K = 10000
X = np.random.randn(K,N)
m = X.mean(axis=1)
w = len(m[np.all([m>-1/20, m<1/20] , axis=0)])
w/K


# In[149]:


N = 10000
K = 1000
X = np.random.randn(K,N)
var = (X**2).sum(axis=1)/N
psi = np.log(var**0.5)
alpha = 0.05
a = -1/((2*N)**0.5) * norm.ppf(1/2 * alpha)
psi_true = psi[ np.all( [psi>-a, psi<a], axis=0  ) ]
len(psi_true)


# In[133]:


from scipy.stats import norm
t = norm.ppf(np.arange(1,K+1)/(K+1))/(1.4*N**0.5)
psi.sort()
plt.figure(figsize=(8,8))
plt.plot(t,psi)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




