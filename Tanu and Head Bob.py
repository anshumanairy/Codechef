#!/usr/bin/env python
# coding: utf-8

# In[12]:


import string
def bob():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        list2=[""]*N
        c=input("")
        list2=list(c)
        d=0
        e=0
        for j in range(0,len(list2)):
            if list2[j]=="I":
                d=d+1
            if list2[j]=="Y":
                e=e+1
        if d>0:
            list1[i]="INDIAN"
        if (d==0 and e!=0):
            list1[i]="NOT INDIAN"
        if (d==0 and e==0):
            list1[i]="NOT SURE"
        
    print(*list1,sep='\n')
bob()


# In[ ]:




