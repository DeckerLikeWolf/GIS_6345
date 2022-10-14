#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[3]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[4]:


map1 = gis.map('Burlington, VT')


# In[5]:


map1


# In[ ]:





# In[8]:


# Item Added From Toolbar
# Title: VT Data - Burlington Zoning - Overlay Districts | Type: Feature Service | Owner: pbrangan
item = gis.content.get("ab92f77ed38a4134a271049d7ad3ed58")
item


# In[9]:


map1.add_layer(item)


# In[ ]:





# In[ ]:




