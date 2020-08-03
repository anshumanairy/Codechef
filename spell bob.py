#!/usr/bin/env python
# coding: utf-8

# In[1]:


import timeit
start = timeit.default_timer()
def chef():
    T=int(input(""))
    list1=[""]*T
    list2=[""]*T
    for i in range(0,T):
        list1[i]=list(input(""))
        list2[i]=list(input(""))
        if ((list1[i][0]=='o' or list2[i][0]=='o')and(list1[i][1]=='b' or list2[i][1]=='b')and(list1[i][2]=='b' or list2[i][2]=='b')):
            list3[i]="yes"
        elif ((list1[i][0]=='b' or list2[i][0]=='b')and(list1[i][1]=='o' or list2[i][1]=='o')and(list1[i][2]=='b' or list2[i][2]=='b')):
            list3[i]="yes"
        elif ((list1[i][0]=='b' or list2[i][0]=='b')and(list1[i][1]=='b' or list2[i][1]=='b')and(list1[i][2]=='o' or list2[i][2]=='o')):
            list3[i]="yes"
        else:
            list3[i]="no"
    print(*list3,sep='\n')
stop = timeit.default_timer()
print (stop - start) 


# In[ ]:


chef()


# In[ ]:




