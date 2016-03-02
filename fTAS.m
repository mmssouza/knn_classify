function [vTAS] = fTAS(mCount)
% vTAS = fTAS(mCount) accepts a 2xN matrix, mCount, where 
% the first and second rows represent the x and y coordinates
% of the boundary points, and returns the triangle area signature, vTAS.
%
% Note: use of this code is allowed only with written approval.
% Written by Naif Alajlan, najlan@ksu.edu.sa
% Copyrights are preserved, 2008.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nN = length(mCount);
vX = mCount(1,:);
vY = mCount(2,:);
%
for ts = 1 : nN/2-1
    vXa = [vX(nN-ts+1:nN) vX(1:nN-ts)];
    vYa = [vY(nN-ts+1:nN) vY(1:nN-ts)]; 
    vXc = [vX(ts+1:nN) vX(1:ts)];
    vYc = [vY(ts+1:nN) vY(1:ts)];
    vD = 0.5*(vX.*(vYc-vYa) + vXc.*(vYa-vY) + vXa.*(vY-vYc));
    mTAS(ts,:) = vD/max(vD);
end
vTAS = mean(mTAS);