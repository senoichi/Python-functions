#!/usr/bin/env python
# coding: utf-8

# In[27]:


from collections import Counter


# In[40]:


cont = 100 - 2
a = int((cont+1)*(cont**2 + 2*cont)/6)
print(a)


# In[97]:


#arr = [1, 3, 9, 9, 27, 81]
arr = [3, 9, 27, 9, 27, 5]
r = 3
#arr = [1, 1, 1, 1, 1]
#r = 1 


# In[94]:


def countTriplets(arr, r):
    arr_hash = Counter(arr)
    numTri = 0
    if r == 1:
        for num in arr_hash.keys():
            cont = arr_hash[num] - 2
            numTri = int((cont+1)*(cont**2 + 2*cont)/6)
            return numTri
    for num in arr_hash.keys():
        tri_i = arr_hash[num] * arr_hash[num*r] * arr_hash[num*r**2]  
        numTri += tri_i
    return numTri
        


# In[118]:


def counter_index(arr):
    arrDex = {}
    i = 0
    for v in arr:
        if v in arrDex:
            arrDex[v].append(i)
        else:
            arrDex[v] = [i]
        i += 1
    return arrDex

def countTriplets(arr, r):
    arrDex = counter_index(arr)
    numTri = 0
    for num in arrDex.keys():
        #print(num, num*r, num*r**2)
        if (num*r in arrDex.keys()) and ((num*r**2) in arrDex.keys()):
            triples = []
            for i in arrDex[num]:
                for j in arrDex[num*r]:
                    for k in arrDex[num*r**2]:
                        if i<j<k:
                            triples.append([i,j,k])
                            numTri += 1
    return numTri, triples
        
    


# In[115]:


counter_index(abrr)


# In[ ]:


def countTriplets(arr, r):
    tri = [None,None,None]
    i = -1
    for num in arr[:-2]:
        tri[0] = num
        i += 1
        for num2 in arr[:i]:
            


# In[119]:


countTriplets(arr, r)

