#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores
import numpy as np

diretorio = sys.argv[1]
raio = 15
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.aii(diretorio+im_file,raio)
   tmp = tmp/(scipy.pi*raio**2)
   db[im_file] = scipy.hstack((cl[im_file],tmp))
   if np.isnan(db[im_file]).any():
    print im_file
cPickle.dump(db,open(sys.argv[2],"wb"))
