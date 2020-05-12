# -*- coding: utf-8 -*-
# =============================================================================
# Imports
# =============================================================================
import os
from renamepy import renamefuncs as refun
cdir = 'H:\Bells Palsy project\clips_and_photos\Backup'
fnames = os.listdir(cdir)
fextens = {'Image': ['jpg', 'jpeg'],
          'Video': ['mp4']
          }

fnames = refun.keep_foi(fnames, fextens, ftype='Image')
