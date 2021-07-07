#!/usr/bin/env python
# coding: utf-8

# In[2]:


for num in [1, 2, 3]:
    print(num)


# In[3]:


for st in ['Hello', 'World', 'Hugo']:
    print(st)


# In[5]:


score = {'국어':25, '영어':90, '수학':80}


# In[6]:


for item in score.keys():
    print(item)


# In[7]:


for item in score.values():
    print(item)


# In[8]:


for key, value in score.items():
    print(f'{key}과목 점수는 {value}점 입니다.')


# In[9]:


list(range(10))


# In[10]:


list(range(1, 11))


# In[11]:


list(range(10, 0, -1))


# In[12]:


for i in range(1, 11, 2):
    print(i)


# In[13]:


for i in range(0, 11, 2):
    print(i)


# In[14]:


for i in range(1, 10):
    ans = 2 * i
    print(f'2 X {i} = {ans}')
else:
    print('구구단 2단을 종료합니다.')


# In[15]:


a = 0


# In[9]:


while a < 10:
    print(a)
    a += 1 # a = a + 1
else:
    print(f'a가 {a}이므로 종료합니다.')


# In[ ]:





# In[24]:


x = 0


# In[25]:


while True:
    x += 3
    print(x)
    if x > 100 and x % 3 == 0:
        break


# In[16]:


a = 0

while a < 10:
    print(a)
    a += 1 # a = a + 1
else:
    print(f'a가 {a}이므로 종료합니다.')



x = 0

while True:
    x += 3
    print(x)
    if x > 100 and x % 3 == 0:
        break


# In[8]:


a = 0


# In[9]:


while a < 10:
    print(a)
    a += 1 # a = a + 1
else:
    print(f'a가 {a}이므로 종료합니다.')


# In[ ]:





# In[24]:


x = 0


# In[25]:


while True:
    x += 3
    print(x)
    if x > 100 and x % 3 == 0:
        break


# In[17]:


a = 0

while a < 10:
    print(a)
    a += 1 # a = a + 1
else:
    print(f'a가 {a}이므로 종료합니다.')



x = 0

while True:
    x += 3
    print(x)
    if x > 100 and x % 3 == 0:
        break


# In[18]:


list1 = list(range(1, 11))
print(list1)


# In[19]:


list2 = [i*2 for i in list1]
list2


# In[ ]:





# In[20]:


list1 = list(range(1, 11))
print(list1)


# In[21]:


list3 = [i**2 for i in list1 if i % 2 == 1]
list3


# In[45]:


list1 = list(range(1, 11))
list4 = list1
list1[1] = 100
print(list4)


# In[47]:


list1 = list(range(1, 11))
list4 = list1.copy()
list1[1] = 100
print(list4)


# In[37]:


from copy import copy


# In[50]:


list1 = list(range(1, 11))
list4 = copy(list1)
list1[1] = 100
print(list4)


# In[65]:


list1 = list(range(1, 11))
list4 = list1[:]
list1[1] = 100
print(list4)


# In[5]:


list2 = [i*2 for i in list1]
list2


# In[ ]:





# In[8]:


list1 = list(range(1, 11))
print(list1)


# In[7]:


list3 = [i**2 for i in list1 if i % 2 == 1]
list3


# In[ ]:




