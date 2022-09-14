#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Line:
    def __init__(self, coor1, coor2):
        self.coor1=coor1
        self.coor2=coor2
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)


# In[5]:


c1=(3,2)
c2=(8,10)


# In[6]:


myline=Line(c1,c2)


# In[7]:


myline.distance()


# In[8]:


myline.slope()


# In[27]:


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    def volume(self):
        return self.height * 3.14 * (self.radius)**2
    def surface_area(self):
        top=3.14*(self.radius**2)
        return (2*top)+(2*314*self.radius*self.height)


# In[28]:


mycyl=Cylinder(2,3)


# In[29]:


mycyl.volume()


# In[ ]:




