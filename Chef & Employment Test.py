#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
def employ():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        c=input("")
        N,K=map(int,c.split())
        list2=[""]*N
        d=input("")
        list2= list(map(int,d.split()))
        list2.sort()
        z=list2[N-1]
        for j in range(0,K):
            x=random.randint(z+1,z+10)
            list2.append(x)
        list2.sort()
        if (len(list2)%2==0):
            y=((len(list2)/2)+((len(list2)/2)+1))/2
            list1[i]=list2[int(y)-1]
        else:
            y=(len(list2)+1)/2
            list1[i]=list2[int(y)-1]
    print(*list1,sep='\n')
employ()


# In[ ]:




