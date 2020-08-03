#!/usr/bin/env python
# coding: utf-8

# In[33]:


import math
def fit():
    T=int(input(""))
    l1=[""]*T
    j=1
    k=0
    t=0
    for i in range(0,T):
        B=int(input(""))
        n=(B/4)
        n=math.floor(n)
        if n<1:
            l1[i]=0
        elif (n==1 and B%4<2):
            l1[i]=1
        else:
            if k==0:
                n=n+(2**j)
                t=n
                l1[i]=n
                k=1
            else:
                k=0
                l1[i]=t
                j=j+1
    for i in range(0,T):
        print (l1[i])
fit()


# In[ ]:




