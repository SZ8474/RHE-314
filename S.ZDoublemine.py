#!/usr/bin/env python
# coding: utf-8

# In[38]:


def doublemin(sequence):
    result = []
    for element in sequence:
        if element == min(sequence):
            element = element + element
        result = result + [element]
    print result
    


# In[39]:


doublemin([10,3,3])


# In[40]:


X = [3,4,5]


# In[41]:


x = double(X)


# In[42]:


double(X)


# In[37]:


double([10,6,3])


# In[ ]:




