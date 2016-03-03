import scipy

def pdist2(X,dist_func):
 N = X.shape[0]
 p = scipy.zeros((N,N))
 for i,a in zip(scipy.arange(N),X):
   for j,b in zip(scipy.arange(i,N),X[i:]):
    p[i,j] = dist_func(a,b)
 p = p + p.transpose()
 return p

def pdist3(X,dist_func,idx,pid):
 N = X.shape[0]
 print X.shape
 p = scipy.zeros((N,N))
 for i in idx:
  for j in scipy.arange(i,N):
   try:
    p[i,j] = dist_func(X[i],X[j])
   except:
    print i,j,pid
 return  p + p.transpose()

