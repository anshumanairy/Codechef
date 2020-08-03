#!/usr/bin/env python
# coding: utf-8

# In[3]:


def inoi():
    C=int(input(""))
    F=int(input(""))
    list1=[[""]]*F
    
    for i in range (0,F):
        x, y, z=map(int, input().split())
        list1[i]=[x,y,z]
    
    for i in range(0,C):
        for j in range(0,3):
            if list1[i[j]]==i+1:
                for k in range(i+2,C):
                    
        
inoi()    
    
        


# In[ ]:




