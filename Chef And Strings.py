#!/usr/bin/env python
# coding: utf-8

# In[3]:


def strings():
    
    N=int(input(""))
    list1=[""]*N
    for i in range(0,N):
        list1[i]=input("")
    Q=int(input(""))
    while(Q!=0):
        L, R, C, P = input().split()
        L=int(L)
        R=int(R)
        C=int(C)
        t=0
        for j in range(L-1,R):
            if P in list1[j]:
                t=t+1
        print (t)
        Q=Q-1

strings()


# In[ ]:




