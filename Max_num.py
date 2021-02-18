# -*- coding: utf-8 -*-
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
ans=data[-1]*k*(m//k)+data[-2]*(m%k)

print(ans)
