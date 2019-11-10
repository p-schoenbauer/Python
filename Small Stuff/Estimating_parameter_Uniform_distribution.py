#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
import matplotlib.pyplot as plt
import numpy as np


# In[177]:


theta = 1
N = 5
K = 50
X = np.random.rand(K,N) * theta


# In[178]:


q = np.arange(1,102,1)
theta_star = np.ones(len(q)+1)
theta_star_var = np.ones(len(q)+1)
theta_star_details = np.ones((len(q)+1,K))

for i in range(len(q)):
    p = q[i]
    Xp = X**p
    Xp_mean = Xp.mean(axis = 1)
    theta_star_p = ((p+1)*Xp_mean)**(1/p)
    theta_star_details[i,] = theta_star_p
    theta_star[i] = (theta_star_p.mean())
    theta_star_var[i] = (theta_star_p.var())
theta_star[len(q)] = (X.max(axis=1).mean())
theta_star_var[len(q)] = (X.max(axis=1).var())
theta_star_details[len(q),] = theta_star[len(q)]
# theta_star,theta_star_var


# In[179]:


t = np.ones(len(q)+1)
t[:len(q)] = q
t[len(t)-1] = q.max()+1
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(t,theta_star, "o", color = "blue")
plt.subplot(1,2,2)
plt.plot(t,theta_star_var, "." , color = "green")


# In[175]:


X.max(axis=1)


# In[51]:


X.max(axis=1).mean()


# In[52]:


X.max(axis=1).var()


# In[94]:


len(theta_star)


# In[180]:


plt.figure(figsize=(15,5))
to_plot = np.arange(1,20,1)
u = np.tile(to_plot,(K,1))
plt.scatter(theta_star_details[to_plot,:], u.T, marker=".")
plt.scatter(theta_star[to_plot], to_plot, marker="o", color="red")


# In[181]:


plt.figure(figsize=(15,5))
plt.scatter(theta_star_details[1,:], [1]*K)


# In[ ]:





# In[166]:


theta_star


# In[ ]:




