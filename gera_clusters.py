#!/usr/bin/python

import numpy
import numpy.random
import pylab
import cPickle
import sys

cl = [1,2,3]
rho = [0.1,0.2,0.05]
mu = [[2.,5.],[1.,-1.],[-1.8,2.5]]
s = [[.05,.3],[0.09,0.9],[0.2,0.5]]
ns = [125,155,100]

X = []
for c,m,s,r,n  in zip(cl,mu,s,rho,ns):
 X1 = numpy.random.normal(m[0],s[0],n)
 X2 = numpy.random.normal(m[1],s[1],n)
 Y1 = r*X1 + numpy.sqrt(1 - r**2)*X2
 for y,x in zip(Y1,X1):
  X.append([c,y,x])
 
c = ['r','b','g']
for aux in X:
 print aux[0],aux[1],aux[2]
 pylab.plot(aux[1],aux[2],'o'+c[aux[0]-1])

f = open(sys.argv[1],"wb")
cPickle.dump(numpy.array(X),f)
f.close()
pylab.show()