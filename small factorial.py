#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fact():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        f=1
        for j in range(2,N+1):
            f=f*j
        list1[i]=f
    print(*list1,sep='\n')
fact()


# In[ ]:




