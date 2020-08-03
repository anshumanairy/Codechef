#!/usr/bin/env python
# coding: utf-8

# In[1]:


def zco():
    N=int(input(""))
    list1=[""]*N
    list1=list(map(int,input("")))
    j=0
    h=0
    g=0
    f=0
    e=0
    d=0
    c=0
    for i in range(N):
        
        f=f+1
        
        if g==0:
            if h<f:
                h=f
                j=i
                f=0
        if list1[i]==1:
            c=c+1
            g=g+1
        
        if list1[i]==2:
            g=g-1
            if d<c:
                d=c
                e=i
            c=0
        
        
    print(d,e,h,j)

zco()


# In[17]:


zco()


# In[ ]:




