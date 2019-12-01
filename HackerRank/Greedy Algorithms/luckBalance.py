#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq as hp


# In[43]:


k = 3
#con = [[5,1],[1,1],[4,0]]
con = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]


# In[48]:


def luckBalance(k, contests):
    savBalnce = 0
    buffer = []
    for c in contests:
        #loose all unimportant games
        if c[1] == 0:
            savBalnce += c[0]
        elif k == 0:
            savBalnce -= c[0]
        else:
            if len(buffer) < k:
                hp.heappush(buffer,c[0])
            else:
                if c[0] > buffer[0]:
                    savBalnce -= hp.heappop(buffer)
                    hp.heappush(buffer,c[0])
                else:
                    savBalnce -= c[0]
    savBalnce += sum(buffer)
    return savBalnce, buffer


# In[81]:


arry = ['a','c','v','m', 'h']
r = 0
arry[::-1][:r] + arry[:len(arry)-r] 


# In[49]:


luckBalance(k, con)


# In[ ]:




