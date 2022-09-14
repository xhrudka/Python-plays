#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Check if the variable is in the current range
def ran_check(num,low,high):
    if num in range(low,high):
        print('Variable is in the range')
    else:
        print('Variable ius not in the range')


# In[19]:


ran_check(5,0,10)


# In[2]:


# Count upper and lower letter
def up_down(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String: ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


# In[3]:


up_down("Hello Baby")


# In[ ]:




