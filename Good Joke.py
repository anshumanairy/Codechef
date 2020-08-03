#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def joke():
    T=int(input(""))
    for i in range(0,T):
        N=int(input(""))
        l1=[""]*N
        for j in range(0,N):
            s=input("")
            l1=list(list(map(int,str(s).split())))
            X=l1[0][0]
            Y=l1[0][1]

