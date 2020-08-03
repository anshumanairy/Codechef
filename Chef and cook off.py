#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cook():
    N=int(input(""))
    list1=[""]*N
    for i in range(0,N):
        list2=[""]*5
        c=input("")
        list2=list(map(int,c.split()))
        d=0
        for j in range(0,5):
            if list2[j]==1:
                d=d+1
        if d==0:
            list1[i]="Beginner"
        if d==1:
            list1[i]="Junior Developer"
        if d==2:
            list1[i]="Middle Developer"
        if d==3:
            list1[i]="Senior Developer"
        if d==4:
            list1[i]="Hacker"
        if d==5:
            list1[i]="Jeff Dean"
    print(*list1,sep='\n')
cook()


# In[ ]:




