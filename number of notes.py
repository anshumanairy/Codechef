#!/usr/bin/env python
# coding: utf-8

# In[4]:


def note():
    T=int(input(""))
    
    l1=[""]*T
    for i in range(0,T):
        N=int(input(""))
        k=0
        d=N/100
        k=k+int(d)
        N=N%100
        
        d=int(N)/50
        k=k+int(d)
        N=N%50
        
        d=int(N)/10
        k=k+int(d)
        N=N%10
        
        d=int(N)/5
        k=k+int(d)
        N=N%5
        
        d=int(N)/2
        k=k+int(d)
        N=N%2
        
        d=int(N)/1
        k=k+int(d)
        N=N%1
        
        l1[i]=k
    print(*l1,sep='\n')
note()


# 
