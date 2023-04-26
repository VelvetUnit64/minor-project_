#!/usr/bin/env python
# coding: utf-8

# In[40]:


import requests
from bs4 import BeautifulSoup as soup


# In[109]:


header = {'Origin': 'https://www.pharmeasy.com',
'Referer': 'https://pharmeasy.in/search/all?name=cetrizen',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


# In[110]:


url = 'https://pharmeasy.in/search/all?name=cetrizen'
html = requests.get(url=url,headers=header)
html.status_code


# In[111]:


obj = soup(html.content,'lxml')
obj


# In[112]:


mrp=[]
for price in obj.findAll('div',{'class':'ProductCard_gcdDiscountContainer__CCi51'}):
    k=price.text.strip()
    index = 3
    output = k[0:6]
    mrp.append(output)
mrp
j=len(mrp)


# In[113]:


product_name = []

for name in obj.findAll('h1',{'class':'ProductCard_medicineName__8Ydfq'}):
    product_name.append(name.text.strip())
product_name
k=len(product_name)
m=j-k
if(m!=0):
    product_name=product_name[:m]
len(product_name)


# In[114]:


d1 = {'pname':product_name,'mrp':mrp}


# In[115]:


import pandas as pd


# In[116]:


df = pd.DataFrame.from_dict(d1)
df


# In[117]:


df.to_csv('pharmeasy.csv')

