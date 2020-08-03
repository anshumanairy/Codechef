#!/usr/bin/env python
# coding: utf-8

# In[2]:


def chess():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        j=N
        s=0
        while j>0:
            s=s+(j*j)
            j=j-2
        list1[i]=s
    print(*list1,sep='\n')
chess()


# In[ ]:




