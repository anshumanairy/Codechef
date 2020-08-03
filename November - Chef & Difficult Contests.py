#!/usr/bin/env python
# coding: utf-8

# In[8]:


def diff():
    T=int(input(""))
    list1=[""]*T
    for i in range(0,T):
        c=input("")
        a,b=map(int,c.split())
        if(a==b):
            list1[i]="YES"
        elif(abs(a-b)>2):
            list1[i]="NO"
        else:
            e=0
            for j in range(10,0):
                for k in range(0,2):
                    if k==0:
                        a=a+d
                        b=b+(d-1)
                        if(a==b):
                            list1[i]="YES"
                            e=e+1
                    else:
                        a=a+(d-1)
                        b=b+d
                        if(a==b):
                            list1[i]="YES"
                            e=e+1
            if e==0:
                list1[i]=="NO"
    print(*list1,sep='\n')
diff()


# In[ ]:




