#!/usr/bin/env python
# coding: utf-8

# In[2]:


def cupcakes():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        if(N%2==0):
            r=(N/2)+1
            list1[i]=int(r)
        else:
            r=(N+1)/2
            list1[i]=int(r)
    print(*list1,sep='\n')
cupcakes()


# In[ ]:




