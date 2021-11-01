# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:38:16 2019

@author: mvakta
"""
import os
def filepath(filename):
    path=os.getcwd()
    fullpath=(path+'\\'+filename)
    return fullpath



filepath("syndicate bank RFP.pdf")
