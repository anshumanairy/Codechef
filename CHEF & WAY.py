#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def street():
    s1=input("")
    N,K=map(int,str(s1).split())
    l1=[""]*N
    s2=input("")
    l1=list(map(int,str(s2)))
    for i in range(0,N):
        d=0
        for j in range(1,N):
            z=l1[j]-l1[i]
            if ((z>=1)and(z>K)):
                

