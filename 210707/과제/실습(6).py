#!/usr/bin/env python
# coding: utf-8

# In[3]:


fr = open('./12-1. hello.txt', 'r')


# In[4]:


for line in fr:
    print(line)


# In[6]:


fr.close()


# In[10]:


with open('./12-1. hello.txt', 'r') as fr:
    for line in fr:
        print(line)


# In[9]:


import myprint


# In[14]:


hello = 'Hello World Python'


# In[15]:


myprint.print1(hello)


# In[16]:


myprint.print2(hello)


# In[18]:


from mymodule import myprint2


# In[19]:


myprint2.print3(hello)


# In[20]:


myprint2.print4(hello)


# In[21]:


import myprint


# In[22]:


hello = 'Hello World Python'


# In[5]:


myprint.print1(hello)


# In[6]:


myprint.print2(hello)


# In[7]:


from mymodule import myprint2


# In[8]:


myprint2.print3(hello)


# In[9]:


myprint2.print4(hello)


# In[26]:


import myprint

hello = 'Hello World Python'
myprint.print1(hello)
myprint.print2(hello)


# In[25]:


from mymodule import myprint2

myprint2.print3(hello)

myprint2.print4(hello)


# In[27]:


fw = open('./hello_write.txt', 'w')


# In[28]:


fw.write('Hello World Python!!!\n')


# In[13]:


fw.write('Welcome to Python World!!!')


# In[14]:


fw.close()


# In[20]:


with open('./hello_write.txt', 'w') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!\n')


# In[21]:


with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# In[ ]:


fw = open('./hello_write.txt', 'w')


fw.write('Hello World Python!!!\n')

fw.write('Welcome to Python World!!!')

fw.close()



with open('./hello_write.txt', 'w') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!\n')



with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# In[11]:


fw = open('./hello_write.txt', 'w')


# In[12]:


fw.write('Hello World Python!!!\n')


# In[13]:


fw.write('Welcome to Python World!!!')


# In[14]:


fw.close()


# In[20]:


with open('./hello_write.txt', 'w') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!\n')


# In[21]:


with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# In[29]:


fw = open('./hello_write.txt', 'w')


fw.write('Hello World Python!!!\n')

fw.write('Welcome to Python World!!!')

fw.close()



with open('./hello_write.txt', 'w') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!\n')


with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# In[30]:


import os


# In[31]:


os.listdir('.')


# In[32]:


file_list = os.listdir('.')


# In[33]:


file_ipynb = [ f for f in file_list if f.endswith('.ipynb')]


# In[34]:


file_ipynb


# In[35]:


os.getcwd()


# In[36]:


os.mkdir('test')


# In[37]:


os.path.join('.', 'test')


# In[38]:


os.path.abspath('hello_write.txt')


# In[39]:


os.path.isfile('hello_write.txt')


# In[14]:


os.path.isdir('hello_write.txt')


# In[15]:


os.path.isfile('test')


# In[17]:


os.path.isdir('test')


# In[18]:


os.path.split(os.path.abspath('hello_write.txt'))


# In[20]:


os.path.splitext('hello_write.txt')


# In[ ]:




