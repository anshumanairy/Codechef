#!/usr/bin/env python
# coding: utf-8

# In[1]:


def host():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        if N in (2010,2015,2016,2017,2019):
            list1[i]="HOSTED"
        else:
            list1[i]="NOT HOSTED"
    print(*list1,sep='\n')
host()


# In[ ]:




