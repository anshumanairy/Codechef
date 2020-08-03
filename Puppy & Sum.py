#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sum1():
    T=int(input(''))
    list1=[""]*T
    for i in range(0,T):
        r=input("")
        D,N=map(int,r.split())
        k=0
        sum=N
        while(D!=0):
            for j in range(0,sum):
                k=k+j
            sum=k
            D=D-1
        list1[i]=k
    print(*list1,sep='\n')
sum1()


# In[ ]:




