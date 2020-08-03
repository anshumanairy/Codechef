#!/usr/bin/env python
# coding: utf-8

# In[2]:


def friend():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        c=input("")
        s=set(list(map(int,c.split(" "))))
        list1[i]=len(s)
    print(*list1,sep='\n')
friend()


# ## 
