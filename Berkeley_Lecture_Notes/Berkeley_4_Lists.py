#!/usr/bin/env python
# coding: utf-8

# In[31]:


list=[1,2,3,"hello",[1.02,3+2J], abs]


# In[32]:


print(list[5](-3))
print(list[2:4])


# In[36]:


# List Alterations

list = ["How", "do", "you", "do", "?"]
list[0:3] = ["HELLO","WORLD"]   # Replace 
print(list)
list[1:1] = "xD"   #Insert
print(list)
list[1:3] = []   # Delete
print(list)
del list[2]   # Delte
print(list)


# In[34]:


# Concatenation

list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)


# In[35]:


# Repetition

list3 = ["WHAT ???"]*5
print(list3)


# In[37]:


# Check if element is in the list

2 in list1


# In[49]:


# Append, Extend, Insert, Remove

list1 = [1,2,3]
list1.extend(list2)
print(list1)
list1.append("HELLO")
print(list1)
list1.insert(3,"WORLD")
print(list1)
list1.remove("WORLD")
print(list1)
del list1[4]
print(list1)


# In[47]:


# Index and Count

list = [1,2,33,4,3,2,2,3,2]
print(list.count(2))
print(list.index(2))


# In[51]:


# Tuple 
# Like list but not mutable

x = (1,2,3)
y = (4,5,6)
z = ()   # Empty tuple
a = (1,) # Tuple with one element (comma is necessary to distinguish from arithmetic expression)
print (x+y+z+a)


# In[57]:


# Convert Tuple to List and reverse

x = (1,20,-1,2.2,7)
y = __builtin__.list(x)   # name list has been overwritten above. Use __bulitin__ to access the bulitin namespace. 
y.sort()
x = tuple(y)
print(x)


# In[72]:


# Dictionaries
# Can use any immutable object as index

dict = {"X":1, "Y":2, "Z":3+2J}
print(dict["Y"])
dict["U"] = 5        # Add a value to the dictionary
print(dict)
print("X" in dict)   # Check if an element is in keys
print(dict.get("X"))
print(dict.get("X","HELLO"))
print(dict.get("XX","HELLO"))
print(dict.keys())  
print(dict.values())
del dict["Y"]        # Delete an element
print(dict.items())  # Return items as tupels (key,value)
print(type(dict.items()))
print(__builtin__.list(dict.items()))   # Convert items to list
newdict = {"X":22, (1,0):"WORLD!"}
dict.update(newdict) # Update dict using newdict
print(dict)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




