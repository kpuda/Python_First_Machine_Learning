#!/usr/bin/env python
# coding: utf-8

# ### import libs

# In[3]:


import pandas as pd
import os
import glob


# ## merge all csv's together

# In[5]:


#Merge the 12 months of sales data into single csv
df=pd.read_csv('./Sales_data/Sales_April_2019.csv')

files = [file for file in os.listdir('./Sales_Data')]

all_months_data=pd.DataFrame()

for filename in files:
    df = pd.read_csv('./Sales_Data/'+filename)
    all_months_data=pd.concat([all_months_data,df])

all_months_data.to_csv('all_data.csv',index=False)


# In[6]:


all_data = pd.read_csv('all_data.csv')
all_data.head()


# ###clean up data! Removing NaN rows and rows where in 'Order Date' is value 'Or'

# In[22]:


all_data=all_data.dropna(how='all')
all_data=all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head()


# In[ ]:


##Convert columns to correct type


# In[38]:


all_data['Quantity Ordered']= pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each']=pd.to_numeric(all_data['Price Each'])


# ### Add month column

# In[39]:


all_data['Month']= all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
all_data.head()


# In[ ]:


### Add a sales column


# In[40]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# In[89]:


all_data['City']= all_data['Purchase Address'].apply(lambda x: f"{x.split(',')[1].lstrip()} {x.split(',')[2].lstrip()}")
all_data


# In[83]:


grouped_sales=all_data.groupby('Month').sum()


# In[66]:


import matplotlib.pyplot as plt

months=range(1,13)

plt.bar(months,grouped_sales['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel("Month")
plt.show()


# ### What city had the highest number of sales

# In[80]:


grouped_sales


# In[88]:


city_group=all_data.groupby('City').sum()
city_group


# In[94]:


months=all_data['City'].unique()

plt.bar(months,grouped_sales['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel("City")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




