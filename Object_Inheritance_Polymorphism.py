#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Animal():
    def __init__(self):
        print("Animal creater")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")


# In[3]:


myanimal=Animal()


# In[6]:


myanimal.who_am_i()


# In[7]:


myanimal.eat()


# In[17]:


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am dog")
    def bark(self):
        print("Woof!")


# In[19]:


mydog=Dog()


# In[20]:


mydog.who_am_i()


# In[22]:


mydog.eat()


# In[36]:


class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says woof"


# In[ ]:





# In[37]:


class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says meow"


# In[38]:


niko=Dog("niko")
felix=Cat("felix")


# In[39]:


print(niko.speak())


# In[40]:


print(felix.speak())


# In[47]:


for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


# In[48]:


def pet_speak(pet):
    print(pet.speak())


# In[49]:


pet_speak(niko)


# In[50]:


pet_speak(felix)


# In[51]:


class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[58]:


class Dog(Animal):
    def speak(self):
        return self.name+ " says woof!"


# In[59]:


class Cat(Animal):
    def speak(self):
        return self.name+ " says meow!"


# In[60]:


fido=Dog("Fido")


# In[61]:


isis=Cat("Isis")


# In[62]:


print(fido.speak())


# In[63]:


print(isis.speak())


# In[ ]:




