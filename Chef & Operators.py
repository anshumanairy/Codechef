#!/usr/bin/env python
# coding: utf-8

# In[2]:


T=int(input(""))
for i in range(0,T):
    l1=[""]*2
    x=""
    r=input("")
    l1=list(map(int,r.split()))
    if (l1[0]<l1[1]):
        x=x+"<"
    elif (l1[0]>l1[1]):
        x=x+">"
    else :
        x=x+"="
print(x)


# In[ ]:




