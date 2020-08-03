#!/usr/bin/env python
# coding: utf-8

# In[1]:


def valid():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        c=input("")
        A,B,C=map(int,c.split())
        if(A+B+C==180):
            list1[i]="YES"
        else:
            list1[i]="NO"
    print(*list1,sep="\n")
valid()


# In[ ]:




