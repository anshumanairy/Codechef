#!/usr/bin/env python
# coding: utf-8

# In[3]:


def two():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        x=int(input(""))
        f=x%10
        
        if f==0:
            list1[i]=0
            
        elif(f!=5):
            list1[i]=-1
        
        else:
            e=0
            while(e!=1):
                x=x*2
                if(x%10==0):
                    e=1
                    list1[i]=1
                
    print(*list1,sep='\n')
two()


# In[ ]:




