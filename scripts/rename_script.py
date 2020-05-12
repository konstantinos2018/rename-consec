# -*- coding: utf-8 -*-
# =============================================================================
# Imports
# =============================================================================
import os
from renamepy import renamefuncs as refun
import datetime as dt

cdir = 'H:\Bells Palsy project\clips_and_photos\Backup'
fnames = os.listdir(cdir)
fextens = {'Image': ['jpg', 'jpeg'],
          'Video': ['mp4']
          }

fnames = refun.keep_foi(fnames, fextens, ftype='Image')
fnames_orig = fnames  # keep original

# ***I could have renamed the names of files with the new delimiter also ***
fnames = refun.standardize_delimiter(fnames, old_delim='-', new_delim='_')

fdates = refun.extract_dates(fnames)

# starting (reference) date
start_date = dt.datetime(2019, 2, 19)
fdate_diff = refun.dates_diff(fdates, start_date)  # calculate differences

# sort original
_, fnames_orig = refun.sort_dates_names(fdate_diff, fnames_orig)
# sort later current version
fdate_diff, fnames = refun.sort_dates_names(fdate_diff, fnames)

# change name of file
fnames_new = refun.name_change(fnames_orig, fdate_diff)

for old_name, new_name in zip(fnames_orig, fnames_new):
    os.rename(os.path.join(cdir, old_name), os.path.join(cdir, new_name))