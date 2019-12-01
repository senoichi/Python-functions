#!/usr/bin/env python
# coding: utf-8

# In[24]:


from collections import Counter 


# In[33]:


m = 'two times three is not four'.split()
n = 'two times two is four'.split()


# In[31]:


def checkMagazine(m, n):
    m_hash, n_hash = Counter(m), Counter(n)
    for word in n:
        if n_hash[word] > m_hash[word]:
            print('No')
            return
    print('Yes')
    return


# In[32]:


checkMagazine(m, n)

