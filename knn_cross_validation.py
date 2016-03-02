#!/usr/bin/python


# Code source: Gael Varoqueux
# Modified for Documentation merge by Jaques Grobler
# License: BSD
import warnings
import numpy as np
from sklearn import neighbors,cross_validation,metrics
import sys
import cPickle
from oct2py import Oct2Py
from functools import partial
 
# import some data to play with
warnings.simplefilter("ignore")
oc = Oct2Py()
n = 3
fd = partial(Oct2Py().HopDSW,hs = n)

db = cPickle.load(open(sys.argv[1],'r'))
Y = np.array([db[i][0] for i in db.keys()]).astype(int)
X = np.array([db[i][1:] for i in db.keys()])
print X

 
clf = neighbors.KNeighborsClassifier(n_neighbors = 3,metric= fd,  n_jobs=1)
          
it = cross_validation.KFold(Y.size,n_folds = 10)
res = cross_validation.cross_val_score(clf,X,Y,cv = it,scoring = "f1_weighted")
print  cn+': ',res.mean(),res.std()
  
