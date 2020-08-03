#!/usr/bin/env python
# coding: utf-8

# In[1]:


T=int(input())
sum=0
# L=[]
# C=[]
for i in range(0,T):
    N=int(input())
    
    
    C=[""]*N
    s=input("")
    C=list(map(int,str(s).split()))
    
    
#     for i in range(0,N):
#         s=input()
#         s1=int(s)
#         C.append(s1)
    
    L=[""]*N
    t=input("")
    L=list(map(int,str(t).split()))
    
    
    
#     for k in range(0,N):
#         t=input()
#         t1=int(t)
#         L.append(t1)
    
    
    
    h=0
    g=0
    sum=0
    h=C[0]
    for i in range(0,N):
        if h>C[i]:
            h=C[i]
        sum=sum+h*L[i]
    

    
    print (sum)


# In[ ]:




