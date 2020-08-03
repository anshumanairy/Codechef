#!/usr/bin/env python
# coding: utf-8

# In[2]:


def guard():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        c=input("")
        a,b=map(int,c.split())
        list1[i]=str(a).trim+" "+str(a+b)
    print(*list1,sep='\n')
guard()


# In[ ]:




