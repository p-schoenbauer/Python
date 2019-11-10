#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


from scipy import io as spio
data_folder = "d:\\_data\\"


# In[16]:


a = np.ones((10,10))
data_file = data_folder + r"mydata.mat"
spio.savemat(data_file, {"a":a})
data = spio.loadmat(data_file)
data["a"]


# In[24]:


import scipy.special as ss
ss.gamma(7.5)


# In[29]:


from scipy import linalg


# In[34]:


A = np.random.rand(5,5)
A,linalg.det(A)


# In[37]:


B = linalg.inv(A)
B


# In[40]:


uA, spec, vhA = linalg.svd(A)
uA, spec, vhA


# In[41]:


get_ipython().run_line_magic('pinfo', 'linalg.svd')


# In[44]:


from scipy.interpolate import interp1d


# In[96]:


np.random.seed(1)

N = 5
x = np.linspace(0,1,N)
y = x**3 + 0.5*(np.random.rand(N) - 0.5)
x = x #+ 0.05*(np.random.rand(N)-0.5)
t = np.linspace(min(x),max(x),100)

index = np.argsort(x)
x = x[index]
y = y[index]

linear_interp = interp1d(x,y)
cubic_interp = interp1d(x,y, kind="cubic")
plt.figure(figsize=(12,7))
plt.scatter(x,y,s=25) 
plt.plot(x, linear_interp(x))
plt.plot(t, cubic_interp(t))


# In[51]:


get_ipython().run_line_magic('pinfo', 'plt.scatter')


# In[70]:


get_ipython().run_line_magic('pinfo', 'interp1d')


# In[97]:


from scipy import optimize


# In[141]:


x = np.linspace(-10,10,100)
y = 1.5*np.sin(1.6*x) + 0.1*np.random.randn(100)


# In[142]:


def func(x,a,b):
    return a * np.sin(b*x)


# In[143]:


para, para_cov = optimize.curve_fit(func, x, y)
para, para_cov


# In[144]:


plt.scatter(x,y)
t = np.linspace(-10,10,300)
plt.plot(t,func(t,para[0],para[1]))


# In[117]:


get_ipython().run_line_magic('pinfo', 'optimize.curve_fit')


# In[149]:


def f(x):
    return x**2 - np.sin(x)
    


# In[154]:


result = optimize.minimize(f,x0=0, method="L-BFGS-B")
result


# In[155]:


x = np.linspace(-2,2,50)
plt.scatter(x, f(x))


# In[165]:


def ff(x):
    return np.sin(x[0]+x[1])+x[0]**2 + x[1]**2
result = optimize.minimize(ff,x0=[0,0], method="L-BFGS-B")
result


# In[174]:


from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2)
y = np.linspace(-2, 2)
xg, yg = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, ff([xg, yg]), rstride=1, cstride=1,
cmap=plt.cm.jet, linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')


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




