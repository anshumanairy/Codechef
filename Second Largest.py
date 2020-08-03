#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def second():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        c=input("")
        list2=[""]*3
        list2=list(map(int,c.split()))
        list2.sort()
        list1[i]=list2[1]
    print(*list1,sep='\n')
second()

