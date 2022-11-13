#!/usr/bin/env python
# coding: utf-8

# In[58]:


import matplotlib.pyplot as plt


# In[59]:


fig, ax = plt.subplots()


# In[60]:


States = ['NY', 'MI', 'WI', 'CO']


# In[61]:


Counts = [55, 39, 35, 33]


# In[ ]:





# In[85]:


bar_colors = ['tab:green']


# In[86]:


ax.bar(States, Counts, color=bar_colors)


# In[87]:


ax.set_ylabel('Ski Mountains')


# In[88]:


ax.set_title('Ski Mountains by State')


# In[92]:


plt.bar(States, Counts, color=bar_colors)


# In[7]:


import matplotlib.pyplot as plt


# In[1]:


import numpy as np


# In[ ]:





# In[ ]:





# In[15]:


category_names = ['Ski Resorts', 'National Forests',]

results = {
    'NY': [55, 2],
    'CO': [33, 11],
    'UT': [21, 6]
}

def demographics(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                       label=colname, color=color)
        
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
             loc='lower left', fontsize='small')
    
    return fig, ax
    
demographics(results, category_names)
plt.show()


# In[ ]:





# In[ ]:




