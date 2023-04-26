#!/usr/bin/env python
# coding: utf-8

# In[31]:


import requests
from bs4 import BeautifulSoup as soup


# In[115]:


header = {'Origin': 'https://www.1mg.com',
'Referer': 'https://www.1mg.com/search/all?filter=true&name=Paracetamol',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


# In[116]:


url = 'https://www.1mg.com/search/all?filter=true&name=Paracetamol'
html = requests.get(url=url,headers=header)
html.status_code


# In[117]:


bsobj = soup(html.content,'lxml')
bsobj


# In[119]:


bsobj.findAll('span',{'class':'style__pro-title___3zxNC'})


# In[121]:


product_name = []

for name in bsobj.find_all('span', {'class':'style__pro-title___3zxNC'}):
    product_name.append(name.text.strip())
len(product_name)


# In[122]:


len(product_name)


# In[143]:


pack_size = []

for size in bsobj.findAll('div',{'class':'style__pack-size___254Cd'}):
    pack_size.append(size.text.strip())


# In[142]:


mrp=[]
for size in bsobj.findAll('div',{'class':'style__price-tag___B2csA'}):
    mrp.append(size.text.strip())


# In[108]:


len(product_name)


# In[132]:


d1 = {'pname':product_name,'psize':pack_size,'mrp':mrp}


# In[133]:


import pandas as pd


# In[149]:


df = pd.DataFrame.from_dict(d1)
df


# In[152]:


df.to_csv('1mg.csv')

