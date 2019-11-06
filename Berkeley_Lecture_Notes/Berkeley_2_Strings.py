#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("hello world")


# In[4]:


dir()


# In[5]:


dir(_i)


# In[9]:


import string


# In[10]:


"Hello World".split()


# In[13]:


#Try-catch statement

try:
    print(7/0)
except ZeroDivisionError:
    print("Division by zero")


# In[14]:


# String with multiple lines

longtext = """This is a very long text.
Using multiple lines.
Hello World!"""

print(longtext)


# In[18]:


# Some special characters

specialcharacters = "\' \n \\ \""
print(specialcharacters)


# In[20]:


# Write R or r in front of a string to disable special characters


nospecialcharacters = r"\' \" \\ "
print(nospecialcharacters)


# In[79]:


# repr(), str(): Convert a number to a string 

print("Convert number to string with repr: " + repr(5.5))
print("Convert number to string with repr: " + str(5.5))


# In[25]:


# duplicate with the * opertor

print("A whole bunch of Tables: " + "Table "*10)
print("And som chairs: " + 20*"Chair ")


# In[28]:


# Access a particular index

print("The first character from longtext is \"" + longtext[0] + "\" and the last is \"" + longtext[-1] + "\"")


# In[31]:


#Access substrings

print(longtext[2:13])
print(longtext[:5])
print(len(longtext))


# In[61]:


# Split

print(longtext.split())
print(longtext.split("\n"))
list = [p for q in longtext.split("\n") for p in q.split(" ")]
print(list)
longtext.split(maxsplit=3)


# In[55]:


# Join

text = "!".join(list)
print(text)


# In[62]:


# Count/Index/Length

print(text.count("!"))
print(text.index("!"))   # First index
print(text.rindex("!"))  # Last index
print(len(text))


# In[78]:


text2 = text.center(92)
print(text2 + "...")
print(text2.lstrip() + "...")
print(text2.rstrip() + "...")
print(text2.strip() + "...")
print(text.ljust(92))
print(text.rjust(92))
print(text.capitalize())   # Capitalize only first letter
print(text.upper())
print(text.lower())
print(text.title())   # Capitalize the first letter in each word


# In[ ]:


#####   USEFUL FUNCTIONS NOT COVERED IN BERKELEY LECTURE NOTES   ##### 


# In[86]:


# Replace

text = "Hello World!!! Mundo, Mundo, Mundo"
text = text.replace("Mundo","").replace(",","").strip()
print("---" + text + "---")


# In[87]:


print(string.digits)
print(string.ascii_uppercase)
print(string.ascii_lowercase)


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




