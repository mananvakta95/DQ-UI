# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:59:29 2019

@author: nidhagga
"""

import pandas as pd
#import numpy as np

#=============================================================================
# Function to read filename
#=============================================================================

def read(filename):
    df = pd.read_csv(filename)
    return df

# Function to identify the missing values
#=========================================
def missing_fields(data):
    missing_value = data.isna()
    return missing_value

#=============================================================================
# Function  for missing percentage
#=============================================================================
def perc_missing(data):
    perc_missing = ((data.isna()).sum() * 100 / data.index.size).round(2)
    return perc_missing


#=============================================================================
# Function to identify primay keys
#=============================================================================
def p_key1(data):
     if data['Duplicates'] == 'N' and data['Null_Check'] == 'N':
        Value = 'Y'
     else:
        Value = 'N'
     return Value

#=============================================================================
# Function for group possibility
#=============================================================================
def group_possibility(data,threshold):
    gp=[]
    print(threshold)
    for i in data['categories']:
        if i < threshold:
            gp.append('YES')
        else:
            gp.append('NO')                                  
#    final_output['Group_Possibility']= gp
    return(gp)
