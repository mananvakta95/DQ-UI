# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:06:48 2019

@author: nidhagga
"""

#import completeness_check
import completeness_display
import pandas as pd
from itertools import combinations



totalcombs = []
originalcols = []
grname = []
missingcounts = []
recordcount =[]

def grouping_missing(data):
    cols = [c for c in list(df) if data[c].nunique() <= 5 and data[c].nunique() != 0]

    for i in range(1,len(cols)):
        combs = combinations(cols,i)
        for i in list(combs):
            print(i)
            totalcombs.append(i)

    # Create grouping based on particular group
    grouped = df.groupby(totalcombs[6])
    return grouped


def grouping_missing_report(data):
    originalcols.append('group_name')

    for col in data.columns:
        originalcols.append(col)

    # Adding new coulmn total record count for each group
    originalcols.append('Total record count')

    countdf = pd.DataFrame(index=range(0,15),columns=originalcols)

    for col in df.columns:
        indcount = []
        for name,group in grouped:
            indcount.append((group.count().max() - group.count())[col])

        missingcounts.append(indcount)
        countdf[col] = indcount


    for name,group in grouped:
        grname.append("_".join(name))
        recordcount.append(group.count().max())


    #final dataframe reflecting NULL values for each column
    countdf['group_name'] = grname
    countdf['Total record count'] = recordcount[0:15]
    return countdf


#data1 = grouping_missing_report(df)
