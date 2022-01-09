I=lambda:map(int,input().split()) # 출처: BOJ @ jh05013
N,Q=I()
d=[0]*(N+1)
for _ in range(Q):
    q,x,y=I()
    if q==1:d[x]+=y
    else:print(sum(d[x:y+1]))