#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,dep_amt):
        self.balance = self.balance+dep_amt
        print(f"Added {dep_amt} to the balance")
        
    def withdrawal(self, wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry non enough funds!")
    def __str__(self):
        return f"Owner:{self.owner} \nBalance: {self.balance}"          


# In[22]:


a=Account("Sam",500)


# In[4]:


a.owner


# In[5]:


a.balance


# In[6]:


print(a)


# In[18]:


a.deposit(100)


# In[23]:


a.withdrawal(600)


# In[24]:


print(a)


# In[26]:


a.str()


# In[ ]:





# In[ ]:




