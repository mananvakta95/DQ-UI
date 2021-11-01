#!/usr/bin/env python
# coding: utf-8

# In[151]:


import pandas as pd
from itertools import combinations



pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def identifyValues():
# In[153]:

    df = pd.read_csv (r'C:\Users\Gambit\Desktop\DQ UI\loan.csv')


    # In[154]:


    df.columns


    # In[155]:


    df.nunique()


    # In[156]:


    # In[157]:


    cols = [c for c
            in list(df)
            if df[c].nunique() <= 5 and df[c].nunique() != 0]


    # In[158]:


    cols


    # In[159]:


    df[cols].nunique()


    # In[160]:


    totalcombs = []


    # In[161]:


    for i in range(1,len(cols)):
        combs = combinations(cols,i)
        for i in list(combs):
            totalcombs.append(i)


    # In[162]:


    len(totalcombs)


    # In[163]:


    len(totalcombs[0])


    # In[164]:


    grouped = df.groupby(totalcombs[6])


    # In[191]:


    for name,group in grouped:
            print("_".join(name))
            print(group.isnull().sum())
            #print(group.count().max() - group.count())


    # In[200]:


    len(grouped)


    # In[172]:


    originalcols = []
    originalcols.append('group_name')
    for col in df.columns:
        originalcols.append(col)


    # In[173]:


    originalcols


    # In[207]:


    countdf = pd.DataFrame(index=range(0,15),columns=originalcols)


    # In[208]:


    countdf.index


    # In[211]:


    grname = []
    missingcounts = []
    indcount = []
    i = 0
    for col in df.columns:
        indcount = []
        for name,group in grouped:
            #print("_".join(name))
            #print(group.count().max() - group.count())
            #grname.append("_".join(name))
            #missingcounts.append(group.count().max() - group.count())
            indcount.append((group.count().max() - group.count())[col])
            #countdf[col] = missingcounts
        missingcounts.append(indcount)
        countdf[col] = indcount

    #df['group_name'] = grname
    #df['missing counts'] = missingcounts


    # In[213]:


    for name,group in grouped:
        grname.append("_".join(name))


    # In[214]:


    countdf['group_name'] = grname


    # In[215]:


    return countdf


# In[84]:





# In[ ]:
