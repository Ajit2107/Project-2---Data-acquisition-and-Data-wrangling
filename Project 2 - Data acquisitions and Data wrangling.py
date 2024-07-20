#!/usr/bin/env python
# coding: utf-8

# ## Project 2 - Data acquisitions and Data wrangling

# ### Importing 3 datasets

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data1=pd.read_excel('dataset_1.xlsx')
data1


# In[4]:


data2=pd.read_excel('dataset_2.xlsx')
data2


# In[5]:


data3=pd.read_excel('dataset_3.xlsx')
data3


# ### Method 1-Merging dataset 1 and dataset 2 with Outer joint

# In[7]:


merge_12=pd.merge(data1,data2,on='instant',how='outer')
merge_12


# ### Method 2- Identify unique values

# ###### Col - instant

# In[8]:


print(list(merge_12.instant.unique()),end="")


# ###### Col -holiday

# In[9]:


print(list(merge_12.holiday.unique()),end="")


# ###### Col-weekday

# In[10]:


print(list(merge_12.weekday.unique()),end="")


# In[ ]:





# ### Method 3- Removing unnecessary columns

# In[11]:


d1=merge_12.drop(['season','yr','mnth','Unnamed: 0'],axis=1)
d1


# ### Check the datatype and summary of the dataset

# In[12]:


d1.shape


# In[13]:


d1.info()


# In[14]:


d1.describe()


# ### Checking null values

# In[15]:


d1.isnull().sum()


# ### Filling null values

# In[16]:


d2=d1.fillna(method='ffill')
d2


# In[17]:


d2.isnull().sum()


# ### Validate the correctness 

# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[19]:


plt.figure(figsize=(10,6))
sns.boxplot(d2)


# ### Concatenate with dataset 3

# In[20]:


merge_final=pd.merge(d1,data3,on='instant',how='outer')
merge_final


# ### Checking datatype and summary of new dataset

# In[21]:


merge_final.shape


# In[22]:


merge_final.info()


# In[23]:


merge_final.describe()


# ### Checking Null values

# In[24]:


merge_final.isnull().sum()


# ### Filling Null values

# In[25]:


d_ff=merge_final.fillna(method='ffill')
d_ff


# In[26]:


d_ff.isnull().sum()


# In[27]:


d_bf=d_ff.fillna(method='bfill')
d_bf


# In[28]:


d_bf.isnull().sum()


# In[29]:


plt.figure(figsize=(25,8))
sns.boxplot(d_bf)


# ### Checking Skewness for random columns

# In[37]:


from scipy.stats import skew
import seaborn as sns
import matplotlib.pyplot as plt


# In[47]:


print(skew(d_bf['instant']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['instant'])
plt.show()


# In[49]:


print(skew(d_bf['hr_x']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['hr_x'])
plt.show()


# In[50]:


print(skew(d_bf['casual_x']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['casual_x'])
plt.show()


# In[51]:


print(skew(d_bf['registered_x']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['registered_x'])
plt.show()


# In[52]:


print(skew(d_bf['hr_x']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['hr_x'])
plt.show()


# In[53]:


print(skew(d_bf['cnt_x']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['cnt_x'])
plt.show()


# In[54]:


print(skew(d_bf['registered_y']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['registered_y'])
plt.show()


# In[55]:


print(skew(d_bf['cnt_y']))
    
#to plot skewness histogram
plt.figure()
sns.distplot(d_bf['cnt_y'])
plt.show()


# ### Checking Correlation

# In[56]:


d_bf.corr()


# ### Plotting Heatmap for Correlation

# In[59]:


plt.figure(figsize=(25,8))
sns.heatmap(d_bf.corr(),annot=True)
plt.show()


# In[ ]:




