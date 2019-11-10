#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Input: datafile containing the historical FTSE100 data (source: https://finance.yahoo.com/)
# Format: Date \t open \t high \t low \t close \t adj.close \t volume

import numpy as np


# In[3]:


file = open(r"d:\_data\indices\FTSE100")
for i in range(5):
    print(file.readline())
file.close()


# In[58]:


file = open(r"d:\_data\indices\FTSE100")
values_list = []
dates_list = []
volume_list = []
while True:
    line = file.readline()
    if not line:
        break
    a = line.split("\t")
    dates_list.append(a[0])
    values_list.append(a[4])
    volume_list.append(a[-1])
file.close()

values_list = values_list[::-1]
dates_list = dates_list[::-1]
volume_list = volume_list[::-1]

print(values_list[0:5])
len(values_list)


# In[59]:


def preproc(x):
    x = [a.replace(",","").replace("\n","") for a in x]
    x = [float(a) for a in x]
    return x


# In[60]:


values_list = preproc(values_list)
volume_list = preproc(volume_list)


values = np.array(values_list)
volume = np.array(volume_list)


# In[61]:


file = open(r"d:\_data\indices\FTSE100preproc","w")
for a,b in zip(values,volume):
    file.write(repr(a) + "\t" + repr(b) + "\n" )
file.close()


# In[51]:


len(values_list)


# In[62]:


get_ipython().run_line_magic('pinfo', 'np.insert')


# In[ ]:




