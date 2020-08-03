#!/usr/bin/env python
# coding: utf-8

# In[1]:


def kitchen():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        list2=[""]*N
        list3=[""]*N
        c=input("")
        list2=list(map(int,c.split()))
        f=input("")
        list3=list(map(int,f.split()))
        d=list2[0]
        for j in range(1,N):
            e=list2[j]
            list2[j]=list2[j]-d
            d=e
        r=0
        for k in range(0,N):
            if(list2[k]>=list3[k]):
                r=r+1
        list1[i]=r
    print(*list1,sep='\n')
kitchen()


# # 
