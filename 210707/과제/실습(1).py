#!/usr/bin/env python
# coding: utf-8

# In[17]:


set1 = {'A', 'B', 'C', 'A', 'D', 'E', 'F', 'B'}
set1


# In[26]:


#set1[0] # 하나하나 읽을 수 없다?
#변형불가, 심지어 읽는것도 불가능?
x, *y = set1
print(x)


# In[8]:


set1[:5]


# In[29]:


set1.add('a')
set1


# In[30]:


set1.add('A')
set1


# In[31]:


set1.remove('a')
set1


# In[32]:


set1.pop()
set1


# In[33]:


중간고사 = {
    "수학": 100,
    "영어": 90,
}
중간고사


# In[34]:


중간고사['국어'] = 85
중간고사


# In[35]:


중간고사['영어']


# In[36]:


list(중간고사.keys())


# In[37]:


list(중간고사.values())


# In[38]:


중간고사.items()


# In[39]:


set1 = {'A', 'B', 'C', 'D', 'E', 'F'}
set2 = {'B', 'D', 'G', 'H'}


# In[40]:


set1 & set2 #교집합


# In[41]:


set1.intersection(set2) #교집합


# In[42]:


set1 | set2 #합집합


# In[43]:


set1.union(set2)


# In[44]:


set1 - set2 #차집합


# In[45]:


set1.difference(set2)


# In[46]:


set1 ^ set2 #없늑넛만 하는거...교차집합?


# In[47]:


set1.symmetric_difference(set2)


# In[48]:


중간고사 = {"수학": 100,"영어": 90,}
중간고사


# In[49]:


중간고사['국어'] = 85
중간고사


# In[50]:


중간고사['영어']


# In[51]:


중간고사['영어'] = 95
중간고사


# In[52]:


list(중간고사.keys())


# In[53]:


list(중간고사.values())


# In[54]:


중간고사.items()


# In[55]:


중간고사.pop('국어')


# In[56]:


중간고사

