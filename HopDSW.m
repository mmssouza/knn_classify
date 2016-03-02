function nDist = HopDSW(vTAS1,vTAS2,hs)
% nDist = HopDSW(vTAS1,vTAS2,hs) returns approximate DSW distance, nDist,
% between vTAS1 and vTAS2 with hopping step hs.
%
% Note: use of this code is allowed only with written approval.
% Written by Naif Alajlan, najlan@ksu.edu.sa
% Copyrights are preserved, 2008.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
w = 3; % width of the Sakoe-Chiba band
n = length(vTAS1);
D = inf(n,n);
TAS_qq = [vTAS1 vTAS1 vTAS1];
TAS_d = vTAS2;
%
nC = 0;
for k = 1 : hs : n
    nC = nC + 1;
    TAS_q = TAS_qq(k:k+n-1);
    D(1,:) = abs(TAS_q-TAS_d(1));
    D(:,1) = abs(TAS_d-TAS_q(1))';
    for ii = 2 : n
        for jj = max(2,ii-w):min(n,ii+w)
            D(ii,jj) = abs(TAS_q(ii)-TAS_d(jj)) + min([D(ii-1,jj-1),D(ii-1,jj),D(ii,jj-1)]);
        end
    end
    dist1(nC) = D(n,n)/n;
end
ix = find(dist1 == min(dist1));
nC = 0;
p = (ix-1)*hs + 1;
for k = n+p-hs+1 : n+p+hs-1
    nC = nC + 1;
    TAS_q = TAS_qq(k:k+n-1);
    D(1,:) = abs(TAS_q-TAS_d(1));
    D(:,1) = abs(TAS_d-TAS_q(1))';
    for ii = 2 : n
        for jj = max(2,ii-w):min(n,ii+w) 
            D(ii,jj) = abs(TAS_q(ii)-TAS_d(jj)) + min([D(ii-1,jj-1),D(ii-1,jj),D(ii,jj-1)]);
        end
    end
    dist11(nC) = D(n,n)/n;
end
%
% flipping transformation
nC = 0;
for k = 1 : hs : n
    nC = nC + 1;
    TAS_q = fliplr(TAS_qq(k:k+n-1));
    D(1,:) = abs(TAS_q-TAS_d(1));
    D(:,1) = abs(TAS_d-TAS_q(1))';
    for ii = 2 : n
        for jj = max(2,ii-w):min(n,ii+w) 
            D(ii,jj) = abs(TAS_q(ii)-TAS_d(jj)) + min([D(ii-1,jj-1),D(ii-1,jj),D(ii,jj-1)]);
        end
    end
    dist2(nC) = D(n,n)/n;
end
ix = find(dist2 == min(dist2));
nC = 0;
p = (ix-1)*hs + 1;
for k = n+p-hs+1 : n+p+hs-1
    nC = nC + 1;
    TAS_q = fliplr(TAS_qq(k:k+n-1));
    D(1,:) = abs(TAS_q-TAS_d(1));
    D(:,1) = abs(TAS_d-TAS_q(1))';
    for ii = 2 : n
        for jj = max(2,ii-w):min(n,ii+w)
            D(ii,jj) = abs(TAS_q(ii)-TAS_d(jj)) + min([D(ii-1,jj-1),D(ii-1,jj),D(ii,jj-1)]);
        end
    end
    dist22(nC) = D(n,n)/n;
end
nDist = min([dist11 dist22]);