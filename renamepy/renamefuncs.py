# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:40:25 2020

@author: KostaGeo
@email: kvlachos.geo@gmail.com
@linkedin: www.linkedin.com/in/kostasvlachosgrs
"""

def extract_extension(fname):
    """Extract the extension of a given file
    
    Args:
        fname = string of the filename
        
    Returns:
        extension = string of the extension
    """
    temp = fname.split('.')
    extension = temp[-1]  # last element of list (i.e. extension)
    
    return extension