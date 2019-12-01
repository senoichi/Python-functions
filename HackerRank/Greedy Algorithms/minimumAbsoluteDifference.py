#!/usr/bin/env python
# coding: utf-8

# In[3]:


arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75,]


# In[2]:


def minimumAbsoluteDifference(arr):
    min_abs = 10**9
    a = sorted(arr)
    for i in range(len(a))[:-1]:
        if abs(a[i+1] - a[i]) < min_abs:
            min_abs = a[i+1] - a[i]
    return min_abs
        


# In[4]:


minimumAbsoluteDifference(arr)


# In[ ]:




