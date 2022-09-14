#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist=[1,2,3]


# In[2]:


class Sample():
    pass


# In[3]:


mysample=Sample()


# In[4]:


mysample


# In[5]:


len(mysample)


# In[6]:


print(mysample)


# In[40]:


class Book():
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        # This definition return strings from objects
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")


# In[41]:


b=Book("Python rocks","Martin",10)


# In[23]:


print(b)


# In[34]:


len(b)


# In[42]:


del b
# Delete variable from the computer memory


# In[ ]:




