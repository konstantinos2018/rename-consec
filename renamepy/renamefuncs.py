# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:40:25 2020

@author: KostaGeo
@email: kvlachos.geo@gmail.com
@linkedin: www.linkedin.com/in/kostasvlachosgrs
"""
# =============================================================================
# Imports
# =============================================================================
import datetime as dt


def extract_extension(fname):
    """Extract the extension of a given file
    
    Args:
        fname -- string of the filename
        
    Returns:
        extension -- string of the extension
    """
    temp = fname.split('.')
    extension = temp[-1]  # last element of list (i.e. extension)
    
    return extension


def keep_foi(fnames, fextens, ftype):
    """Given a list of filenames, keep the filenames of interest (foi)
    based on the given info
    
    Args:
        fnames -- list of strings of  the filenames
        fextens -- dictionary {'Image': list of image files' extensions,
                              'Video': list of video files' extensions
                              }
        ftype -- string with one key of fextens dictionary
        
    Returns:
        fnames_foi -- list of filenames of interest (foi)
    """
    
    fnames_foi = []
    
    for name in fnames:
        for exten in fextens[ftype]:
            if exten in extract_extension(name):
                fnames_foi.append(name)

#    [name for name in fnames for exten in fextens['Image'] if exten in extract_extension(name)]

    return fnames_foi


def standardize_delimiter(fnames, old_delim, new_delim):
    """Standardize the delimiter that is used in the filenames. The reason for
    this is that different files use different delimiters. For example, part
    of the files use '-' as a delimiter, while others use '_'.
    
    Args:
        fnames -- list of strings of  the filenames
        delim -- string with the new delimiter
        
    Returns:
        fnames_stand -- list of strings of  the filenames with standardized
                       delimiter
    """
    
    fnames_stand = []
    
    for name in fnames:
        fnames_stand.append(name.replace(old_delim, new_delim))
        
    return fnames_stand


def extract_dates(fnames):
    """Extract the dates from filenames into a datetime format
    
    Args:
        fnames -- list of strings of  the filenames
        
    Returns:
        fdates -- list of datetime with the dates of each file
    """
    
    fdates = []
    
    for name in fnames:
        date_temp = name.split('_')
        date_temp = date_temp[1]  # keep date
        date_temp = dt.datetime.strptime(date_temp, '%Y%m%d')  # convert to dt
        
        fdates.append(date_temp)
        
    return fdates


def dates_diff(fdates, start_date):
    """Calculates the difference between dates in a list and a reference date.
    All dates are in datetime format.
    
    Args:
        fdates -- list of datetime with the dates of each file
        start_date = datetime of date of reference
        
    Returns:
        ddiff -- list of integers with the difference in days
    """
    
    ddiff = []
    
    for date in fdates:
        date_temp = date - start_date
        ddiff.append(date_temp.days)
        
    return ddiff


def sort_dates_names(fdate_diff, fnames):
    """Sorts the date differences list and the filenames list based on the
    former
    
    Args:
        fdate_diff -- list of integers with the difference in days
        fnames -- list of strings of  the filenames
        
    Returns:
        fdate_diff_sorted -- fdate_diff sorted
        fnames_sorted -- fnames_sorted based on fdate_diff
    """
    
    temp = sorted(zip(fdate_diff, fnames))
    fdate_diff_sorted, fnames_sorted = zip(*temp)
    
    return list(fdate_diff_sorted), list(fnames_sorted)


def name_change(fnames, fdate_diff):
    """ Change the names of the files to the new desired names with the
    addition of the prefix
    
    Args:
        fnames -- list of strings of  the filenames
        fdate_diff -- list of strings of the filenames
        
    Returns:
        fnames_new -- list of strings of the new filenames
    """
    
    # Initialization
    k = 0
    flag_ddiff = fdate_diff[0]  # flag
    fnames_new = []
    
    for name, ddiff in zip(fnames, fdate_diff):
    
        if flag_ddiff == ddiff:            
            s = 'Day_{0}_{1}_{2}'.format(ddiff, k, name)
            fnames_new.append(s)
            k = k + 1
            
        else:
            k = 0
            flag_ddiff = ddiff
            s = 'Day_{0}_{1}_{2}'.format(ddiff, k, name)
            fnames_new.append(s)
            k = k + 1
        
    return fnames_new

if __name__ == '__main__':
    pass
