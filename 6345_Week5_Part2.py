#!/usr/bin/env python
# coding: utf-8

# In[22]:


import geopandas as gpd


# In[23]:


path_to_data = "/GIS/Data/5201/Final Project/Maine_Coastal_Bluffs-shp/Maine_Coastal_Bluffs.shp"


# In[25]:


gdf = gpd.read_file(path_to_data)


# In[26]:


gdf


# In[27]:


import pandas


# In[84]:


type(gdf)


# In[85]:


gdf.head(6)


# In[ ]:





# In[19]:


bar = gdf.plot.bar(x='OBJECTID', y='Shape__Len',)


# In[ ]:


bar


# In[ ]:





# In[ ]:





# In[ ]:




