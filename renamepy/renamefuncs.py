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


def keep_foi(fnames, fextens, ftype):
    """Given a list of filenames, keep the filenames of interest (foi)
    based on the given info
    
    Args:
        fnames = list of strings of  the filenames
        fextens = dictionary {'Image': list of image files' extensions,
                              'Video': list of video files' extensions
                              }
        ftype = string with one key of fextens dictionary
        
    Returns:
        fnames_foi = list of filenames of interest (foi)
    """
    
    fnames_foi = []
    
    for name in fnames:
        for exten in fextens[ftype]:
            if exten in extract_extension(name):
                fnames_foi.append(name)

#    [name for name in fnames for exten in fextens['Image'] if exten in extract_extension(name)]

    return fnames_foi