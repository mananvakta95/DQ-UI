# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:04:08 2019

@author: nidhagga
"""

import pandas as pd
import completeness_check
import completeness_grouping

filename = 'loan.csv'
group_threshold = 10  # threshold to create groups

#=============================================================================
#### Generate Report
#===========================================================================
def data_report(data):
    missing_value = (pd.Series(completeness_check.missing_fields(data).any(),name='Null_Check')).replace({True:'NULL',False:'NOT NULL'})
    new_df = pd.DataFrame(missing_value)
    category = data.nunique()
    #m=data.apply(lambda x: x.duplicated())
    #new_df = (pd.concat([pd.Series(completeness_check.missing_fields(data).any(),name='Null_Check'),pd.Series(m.any(),name='Duplicates')],axis=1).replace({True:'Y',False:'N'}))
    new_df['Percentage_of_Missing_Values'] = completeness_check.perc_missing(data)
    #new_df['Primary_key']= new_df.apply(completeness_check.p_key1, axis=1)
    new_df['categories'] = category
    new_df['Sub-segment']= completeness_check.group_possibility(new_df,group_threshold)
    final_output = new_df.drop(['categories'],axis=1)
    return new_df
