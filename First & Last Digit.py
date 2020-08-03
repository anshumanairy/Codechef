#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
def digit():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        f=0
        sum=0
        N=int(input(""))
        n=N
        while(n>=10):
            n=int(n)/10
        s=(N%10)+int(n)
        list1[i]=s
    print(*list1,sep='\n')
digit()


# In[ ]:




