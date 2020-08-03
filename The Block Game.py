#!/usr/bin/env python
# coding: utf-8

# In[4]:


def block():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        n=N
        s=0
        while(n>0):
            d=n%10
            s=(s*10)+d
            n=n//10
        if s==N:
            list1[i]="wins"
        else:
            list1[i]="losses"
    print(*list1,sep='\n')
block()


# In[ ]:




