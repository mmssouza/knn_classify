#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores as desc
import numpy as np

sigma = 24.
diretorio = sys.argv[1]
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = desc.curvatura(diretorio+im_file,scipy.array([sigma]),method = 'octave').curvs[0]
   db[im_file] = scipy.hstack((cl[im_file],tmp))
   if np.isnan(db[im_file]).any():
    print im_file,tmp
cPickle.dump(db,open(sys.argv[2],"wb"))
