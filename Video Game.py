#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def game():
    list1=[""]*2
    r=input("")
    l1=list(map(int,str(r).split()))
    w=l1[0]
    h=l1[1]
    l2=[""]*w
    s=input("")
    l2=list(map(int,str(s).split()))
    c=input("")
    l3=[""]*len(c)
    l3=list(map(int,str(c).split()))
    x=0
    t=0
    for i in range(0,len(c)):
        
        if l3[i]==0:
            break
        if l3[i]==1 and t!=0:
            t=t-1
        if l3[i]==2 and t<w-1:
            t=t+1
        if l3[i]==3 and x==0 and l2[t]!=0:
            l2[t]=l2[t]-1
            x=1
        if l3[i]==4 and x==1 and l2[t]<h:
            l2[t]=l2[t]+1
            x=0
    print(' '.join(map(str,l2)))
game()


# In[ ]:




