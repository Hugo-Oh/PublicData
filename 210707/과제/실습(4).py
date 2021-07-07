#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#실습1은 대체!


# In[1]:


def add1():
    print("더하기 함수입니다.ㅎ.ㅎ.ㅎ.ㅎ.ㅎ.ㅎ")


# In[2]:


add1()


# In[3]:


def add2(x, y):
    print(x + y)


# In[5]:


add2(1, 2)


# In[6]:


def add3():
    x, y = 2, 4
    return x + y


# In[7]:


re_val = add3()
print(re_val)


# In[ ]:





# In[9]:


def add4(x, y):
    return x + y


# In[11]:


re_val = add3()
print(re_val)


# In[12]:


def square(x, y):
    x = x ** 2
    y = y ** 2
    return x, y


# In[13]:


a, b = square(2, 3)
print(a)
print(b)


# In[ ]:


#살숩은 대체?


# In[15]:


def square2(x=2, y=3):
    x = x ** 2
    y = y ** 2
    return x, y


# In[16]:


square2()


# In[17]:


square2(2)


# In[18]:


square2(2, 3)


# In[ ]:





# In[20]:


def square2(x=2, y=3):
    x = x ** 2
    y = y ** 2
    return x, y


# In[21]:


square2(4, 5)


# In[23]:


square2(y=5, x=4)


# In[ ]:





# In[24]:


def changeble(x, *y):
    print(x, y)


# In[25]:


changeble(1)


# In[26]:


changeble(1, 2)


# In[27]:


changeble(1, 2, 3)


# In[28]:


changeble(1, 2, 3, 4, 5)


# In[ ]:


#살숩은 대체

def square2(x=2, y=3):
    x = x ** 2
    y = y ** 2
    return x, y

square2()

square2(2)

square2(2, 3)



def square2(x=2, y=3):
    x = x ** 2
    y = y ** 2
    return x, y

square2(4, 5)

square2(y=5, x=4)



def changeble(x, *y):
    print(x, y)

changeble(1)

changeble(1, 2)

changeble(1, 2, 3)

changeble(1, 2, 3, 4, 5)

