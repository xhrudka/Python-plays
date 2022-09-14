#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prvni_funkce():
    print("Hello")


# In[4]:


prvni_funkce()


# In[8]:


def druha_funkce():
    '''
    DOCSTRING: Information about the fuction
    INPUT: no input...
    Output: Hello...
    '''
    print('Hello')


# In[9]:


help(druha_funkce())


# In[13]:


def pozdrav(name):
    print("Čau " +name)


# In[14]:


pozdrav('Jeffe')


# In[15]:


def pozdrav2(name):
    return ("Nazdar "+name)


# In[16]:


pozdrav2("Jeffe")


# In[24]:


result = pozdrav2("Jeff ")


# In[25]:


print(result)


# In[30]:


# Find out if the word is a string?
def dog_check(mystring):
    if "dog" in mystring:
        return True
    else:
        return False


# In[31]:


dog_check("My dog")


# In[32]:


def dog_advance_check(mystring):
    return "dog" in mystring.lower()


# In[34]:


dog_advance_check("catty")


# In[43]:


def pig_latin(word):
    first_letter=word[0]
    # check if vowel
    if first_letter in "aeiou":
        pig_word = word +"ay"
    else:
        pig_word=word[1:]+first_letter+"ay"
    return pig_word


# In[45]:


pig_latin("Jeffik")


# In[ ]:




