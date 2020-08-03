#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math
def card():
    T=int(input(""))
    for i in range(0,T):
        a, b = map(int, input().split())
        x1=int(round((2*(a+b)+math.sqrt((4*((a+b)**2))-12*a*b))/6))
        x2=int(round((2*(a+b)-math.sqrt((4*((a+b)**2))-12*a*b))/6))
        x=min(x1,x2)
        print("{} {}".format(x,x*(a-x)*(b-x)))

card()                            


# In[ ]:




