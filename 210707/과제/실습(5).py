#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys


# In[3]:


help('sys')


# In[4]:


import os


# In[6]:


help(os)


# In[7]:


dir(os)


# In[5]:


os.getcwd()


# In[8]:


os.listdir()


# In[9]:


import numpy as np


# In[10]:


np.absolute(-3)


# In[11]:


np.sqrt(16)


# In[12]:


from scipy import stats


# In[14]:


stats.hmean([1, 2, 3])


# In[15]:


stats.variation([1, 2, 3])


# In[16]:


from datetime import datetime


# In[17]:


now = datetime.now()


# In[18]:


now.year


# In[19]:


now.month


# In[20]:


import sys


# In[21]:


sys.path


# In[22]:


import myprint


# In[23]:


hello = 'Hello World Python'


# In[24]:


myprint.print1(hello)


# In[25]:


myprint.print2(hello)


# In[30]:


from mymodule import myprint2


# In[31]:


myprint2.print3(hello)


# In[32]:


myprint2.print4(hello)


# In[33]:


import myprint

hello = 'Hello World Python'



myprint.print1(hello)

myprint.print2(hello)



from mymodule import myprint2

myprint2.print3(hello)

myprint2.print4(hello)

