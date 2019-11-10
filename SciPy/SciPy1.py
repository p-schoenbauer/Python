#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


file = open(r"d:\_data\indices\FTSE100")
for i in range(5):
    print(file.readline())
file.close()


# In[ ]:


file = open(r"d:\_data\indices\FTSE100")
values_txt = []
dates_txt = []
volume_txt = []
while True:
    line = file.readline()
    if not line:
        break
    a = line.split("\t")
    dates_txt.append(a[0])
    values_txt.append(a[4])
    volume_txt.append(a[-1])
file.close()


# In[ ]:


values_txt[0:4]


# In[160]:


volume_txt[0:4]


# In[161]:


N = len(values_txt)

# Reversing. 

# values2 = [0]*N
# dates2 = [0]*N
# volume2 = [0]*N
# for i in range(len(values_txt)):
#     values2[i] = values_txt[len(values_txt)-1-i]
#     dates2[i] = dates_txt[len(values_txt)-1-i]
#     volume2[i] = volume_txt[len(values_txt)-1-i]
# dates_txt = dates2
# values_txt = values2
# volume_txt = volume2

dates_txt = dates_txt[::-1]
volume_txt = volume_txt[::-1]
values_txt = values_txt[::-1]


# In[162]:


volume_txt[-1]
dates_txt[-1]


# In[163]:


values_list = [v.replace(",","") for v in values_txt]
values_list = [float(v) for v in values_list]
values = np.array(values_list)


# In[164]:


# Preprocess dates...


# In[165]:


volume_list = [v.replace(",","").replace("\n","") for v in volume_txt]
volume_list = [float(v) for v in volume_list]
volumes = np.array(volume_list)
volumes[-1]


# In[166]:


# NumPy is fast compared to Python lists(#dynamicTypecasting)
get_ipython().run_line_magic('timeit', '[x**2 for x in values_list]')
get_ipython().run_line_magic('timeit', 'values**2')


# In[167]:


# Get help
get_ipython().run_line_magic('psearch', 'np.con*')


# In[168]:


values.shape


# In[169]:


values.ndim


# In[170]:


len(values)


# In[171]:


print(np.arange(10))
print(np.arange(2,17,4))
print(np.linspace(1,5,40, endpoint=False))


# In[172]:


print(np.ones((2,2)))
print(np.zeros((2,2)))
print(np.eye(2))
print(np.diag([1,2,3]))
print(np.empty(3))


# In[154]:


np.random.seed(1232)
print(np.random.rand(4))   # Uniform
print(np.random.randn(4))  # Gaussian


# In[155]:





# In[174]:


N = len(values)
x = np.arange(N)
plt.plot(x,values)


# In[175]:


plt.plot(x,values,".")


# In[176]:


import math
x = np.linspace(0,6*math.pi,200)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,"x")
plt.plot(x,z,"p")


# In[181]:


a = np.ones((5,9))
a[0,2] = -88
a[0,3] = 5
a[1,4] = 19
a


# In[182]:


a[:,::2]


# In[190]:


a = np.arange(6)
b = np.arange(5)[:,np.newaxis]
print(a,"\n",b,"\n",a+b)
print(a[:,np.newaxis])
print(a[np.newaxis,:])


# In[193]:


A = np.ones((4,4),int)
A[2,3] = 2
A[3,1] = 6
A


# In[205]:


B = np.diag([1.,2,3,4,5,6])
B = B[:,1:6]
B


# In[212]:


C = np.tile([[4,3],[2,1]],(2,3))
C


# In[213]:


D = C.copy()
C[1,1] = 177
print(C,"\n",D)


# In[227]:


def find_primes(N):
    is_prime = np.ones(N,dtype=bool)
    is_prime[0:2] = False
    for j in range(2, int(np.sqrt(N))):
        is_prime[j*j::j] = False;
    return is_prime.nonzero();


# In[293]:


K = 10000
primes = np.array(find_primes(K))
primes = np.squeeze(primes)
x = np.arange(K)
y = np.zeros(K)
for p in primes:
   y[p-1:] = y[p-1:] + 1
axes = plt.gca()
axes.set_ylim([0,3000])
plt.plot(x,y)
plt.plot(x,x/np.log(x+2))
plt.plot(x,10000*(y/((x+1)/np.log(x+2))-1))


# In[264]:


primes


# In[243]:


y[1:] = y[1:] + 1
y


# In[294]:


a = np.random.randint(0,100,20)
a


# In[295]:


a%3


# In[297]:


b = a[a%3 == 0]
b


# In[300]:


a[[1,1,2,2,2]]


# In[301]:


np.cumsum(a)


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




