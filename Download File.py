#!/usr/bin/env python
# coding: utf-8

# In[3]:


def download():
    TC=int(input(""))
    list1=[""]*TC
    for i in range(0,TC):
        c=input("")
        N,K=map(int,c.split())
        s=0
        for j in range(0,N):
            e=input("")
            T,D=map(int,e.split())
            if K>=T and K>0:
                K=K-T
                T=0
            if T>K:
                T=T-K
                K=0
            s=s+(T*D)
        list1[i]=s
    print(*list1,sep='\n')
download()


# In[ ]:




