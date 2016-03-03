function Dmat = pdist3(X,idx)
 N = size(X)(1);
 Dmat = zeros(N,N);
 for i = idx
  for j = 1:N
   if i != j
    Dmat(i,j) = HopDSW(X(i,:),X(j,:),hs = 3);
   end
  end
 end

