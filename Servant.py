#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def servant():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        if N<10:
            list1[i]="What an obedient servant you are!"
        else:
            list1[i]=-1
    print(*list1,sep='\n')
servant()


# In[ ]:




