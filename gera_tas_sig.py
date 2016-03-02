#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores
import numpy as np

diretorio = sys.argv[1]

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db1 = {}
db2 = {}
for im_file in cl.keys():
   tmp1 = descritores.TAS(diretorio+im_file,method='octave').sig
   db1[im_file] = scipy.hstack((cl[im_file],tmp1))
   if np.isnan(db1[im_file]).any():
    print '1 '+im_file
   if len(sys.argv) == 4:
    tmp2 = descritores.fTAS(diretorio+im_file)
    db2[im_file] = scipy.hstack((cl[im_file],tmp2))
    if np.isnan(db2[im_file]).any():
     print '2 '+im_file

cPickle.dump(db1,open(sys.argv[2],"wb"))
if len(sys.argv) == 4:
 cPickle.dump(db2,open(sys.argv[3],"wb"))
