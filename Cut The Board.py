#!/usr/bin/env python
# coding: utf-8

# In[6]:


def board():
    T=int(input())
    l2=[""]*T
    for i in range(0,T):
        s=input("")
        l1=[""]*2
        l1=list(map(int,str(s).split()))
        N=l1[0]
        M=l1[1]
        w=(N*M)-(N+M)+1
        l2[i]=w
    for i in range(0,T):
        print (l2[i])
board()


# In[ ]:




