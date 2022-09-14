#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Dog():
    # Class object attribute
    # Sane for any instance of a class
    species="mammal"
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

    # Operation / actions = Methods
    def bark(self,number):
        print("Woof! My name is {} and number {}".format(self.name,number))


# In[2]:


my_dog = Dog("Golden", "Jeff")
# Shift + Tab shows class details


# In[3]:


my_dog.bark(10)


# In[33]:


class Circle():
    # Class object attribute
    pi=3.14
    def __init__(self, radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


# In[34]:


my_circle=Circle(30)
# Override default value - radius


# In[35]:


my_circle.radius


# In[36]:


my_circle.get_circumference()


# In[38]:


my_circle.area


# In[ ]:




