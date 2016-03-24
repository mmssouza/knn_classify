#!/usr/bin/python -u
# -*- coding: utf8 -*-
import sys
import cPickle
import scipy
from multiprocessing import Queue,Process
from pdist2 import pdist3
from numpy import histogram

def worker(in_q,out_q):
  args = in_q.get()
  pdist3(args[0],args[1],out_q)
      
if __name__ == '__main__':
 f = open(sys.argv[2],"wb")
# Matriz de amostras x atributos
 db = cPickle.load(open(sys.argv[1]))
 #aux = scipy.array(db.values())
 #data1,labels = aux[:,1:],aux[:,0]
 #labels = aux[:,0]
 labels = scipy.array([x[0] for x in db.values()])
 cPickle.dump(labels,f)
# data1 = scipy.rand(40,125)
# Numero de amostras
 data1 = scipy.array([histogram(x[1:],bins = 50,range = (0.,1.),normed = True)[0] for x in db.values()])
 Nobj = data1.shape[0]
# Cpu's empregadas no cálculo
 #Ncpu = multiprocessing.cpu_count()
 Ncpu = 2
# Gera as partições (Npart listas de indices das linhas de data1)
 limits_hi= scipy.linspace(Nobj/Ncpu,Nobj,Ncpu).astype(int)
 limits_lo = np.hstack((0,limits_hi[0:limits_hi.shape[0]-1]))
 idx =[scipy.arange(lo,hi) for lo,hi in zip(limits_lo,limits_hi)]

# Filas para comunicar com threads
 in_q,out_q = Queue(),Queue()
# Ativa as threads
 threads = []
 for i in range(Ncpu):
  t =  Process(target=worker,args=(in_q,out_q))
  threads.append(t)

 for p in threads:
  p.start()
  
# Passa matriz e indices para que cada thread calcule 
# uma parte da matriz de distâncias
 for i in idx:
  in_q.put([data1,i])
 
 aux = 0;
 while aux != Ncpu:
  a = out_q.get()
  print a
  if a[0] == -1:
   aux = aux + 1   
   continue
  cPickle.dump(a,f)
 f.close()
# Aqui vai dormir, acordando para cada resultado
# parcial 
# l = [out_q.get() for i in scipy.arange(len(idx))]

# for p in threads:
#  p.terminate()
 
 for p in threads:
  p.terminate()
  
# Calcula matriz de distancias
# dmat = scipy.zeros((Nobj,Nobj))
# for d in l:
#  dmat = dmat + d
# Salva resultado
# with open(sys.argv[1],'wb') as f:
#  cPickle.dump(dmat, f)
#  cPickle.dump(db,f) 
