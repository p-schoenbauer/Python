#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[5]:


x = np.linspace(-np.pi,np.pi,100,endpoint=True)
y,z = np.cos(x), np.sin(x)


# In[76]:


plt.figure(figsize=(12,4), dpi=80)
plt.subplot(1,2,1)
plt.plot(x,y, color="blue", linewidth=2.0, linestyle="-", label="cosine")
plt.plot(x,z, color="green", linewidth=2.0, linestyle="-", label="sine")
plt.xlim(x.min(),x.max())
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r"$-\pi$",r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])
plt.yticks([-1,1])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.legend(loc="upper left")

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t], [np.cos(t)], 50, color='blue')
plt.annotate(r'$cos(\frac{2\pi}{3} )=-\frac{1} {2} $',
xy=(t, np.cos(t)), xycoords='data',
xytext=(-90, -40), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.subplot(1,2,2)
plt.plot(x,x**2, x, x**4/9, x, x**6/90)


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





# In[ ]:





# In[ ]:




