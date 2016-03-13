#!/usr/bin/python -u
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy

def gera_mat(fname):
  f = open(fname,'rb')
  labels = cPickle.load(f)
  md = []
  while True:
   try: 
    md.append(cPickle.load(f))
   except:
    break
  f.close()
  md = scipy.array(md)
  idx = scipy.argsort(md[:,0])
  md = md[idx]
  #md = scipy.delete(md[idx],scipy.s_[0:1],axis = 0)
  md = scipy.delete(md,0,axis = 1)
  md = md + md.T
  return md,labels

if __name__ == '__main__':
 
 md,cl = gera_mat(sys.argv[1])
 Nobj = md.shape[0]
 Nretr = 40

# Acumulador para contabilizar desempenho do experimento
 tt = 0.

 #print "Calculando bull eye score"
 for i in scipy.arange(Nobj):
  idx = scipy.argsort(md[i])
  classe_retrs = (cl[idx])[0:Nretr]
  n = scipy.nonzero(scipy.array(classe_retrs) == cl[i])
  tt = tt + float(n[0].size)
    
# Bull eye
 print 20*1400,tt
 print tt/float(1400*20)  
