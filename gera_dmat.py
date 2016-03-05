#!/usr/bin/python -u
# -*- coding: utf8 -*-
import sys
import cPickle
import scipy
from multiprocessing import Queue,Process
from pdist2 import pdist3

def worker(in_q,out_q):
    while True:
     args = in_q.get()
     d = pdist3(args[0],args[1])
     out_q.put(d)
      
if __name__ == '__main__':
# Matriz de amostras x atributos
 db = cPickle.load(open(sys.argv[1]))
 data1 = scipy.array(db.values())[:,1:]
# Numero de amostras
 Nobj = data1.shape[0]
# Numero de partições de data1 para processamento paralelo
 Npart = 2
# Cpu's empregadas no cálculo
 Ncpu = 2

# Gera as partições (Npart listas de indices das linhas de data1)
 limits_hi= scipy.linspace(Nobj/Npart,Nobj,Npart).astype(int)
 limits_lo = scipy.linspace(0,Nobj,Npart,endpoint = False).astype(int)
 idx =[scipy.arange(lo,hi) for lo,hi in zip(limits_lo,limits_hi)]
 print idx

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
 
# Aqui vai dormir, acordando para cada resultado
# parcial 
 l = [out_q.get() for i in scipy.arange(len(idx))]

 for p in threads:
  p.terminate()

# Calcula matriz de distancias
 dmat = scipy.zeros((Nobj,Nobj))
 for d in l:
  dmat = dmat + d
# Salva resultado
 with open(sys.argv[1],'wb') as f:
  cPickle.dump(dmat, f)
  cPickle.dump(db,f) 
