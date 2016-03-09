import scipy
from oct2py import Oct2Py

def pdist2(X,dist_func):
 N = X.shape[0]
 p = scipy.zeros((N,N))
 for i,a in zip(scipy.arange(N),X):
   for j,b in zip(scipy.arange(i,N),X[i:]):
    p[i,j] = dist_func(a,b)
 p = p + p.transpose()
 return p

def pdist3(X,idx,q):
 N = X.shape[0]
 p = scipy.zeros((N,N))
 oc = Oct2Py()
 for i in idx:
  for j in scipy.arange(N):
   if i != j:
    try:
     oc.push(['A','B'],[X[i],X[j]])
     p[i,j] = oc.eval('HopDSW(A,B,hs = 2);')
    except:
     print i,j
  q.put(scipy.hstack((i,p[i]))) 	  
 q.put(scipy.hstack((-1,scipy.zeros(N)))) 
 oc.exit()

