import math
N,M=map(int,input().split())
b=[]
s=[]
for i in range(N):
    a=list(map(int,input().split()))
    b.append(a)
    s.append([])
for i in range(N):
    for j in range(M):
        s[i].insert(j,0)
for i in range(N):
    for j in range(M):
        if ((i!=0 or j!=0) and b[i][j]==1):
            c=0
            if((i-1)>=0 and b[i-1][j]==1):
                c=c+1
            if((i+1)<N and b[i+1][j]==1):
                c=c+1
            if((j+1)<M and b[i][j+1]==1):
                c=c+1
            if((j-1)>=0 and b[i][j-1]==1):
                c=c+1
            if((i-1)>=0 and (j+1)<M and b[i-1][j+1]==1):
                c=c+1
            if((i+1)<N and (j+1)<M and b[i+1][j+1]==1):
                c=c+1
            if((i-1)>=0 and(j-1)>=0 and b[i-1][j-1]==1):
                c=c+1
            if((i+1)<N and (j-1)>=0 and b[i+1][j-1]==1):
                c=c+1
            s[i][j]=c
m=s[0][0]
for i in range(N):
    for j in range(M):
        if m<s[i][j]:
            m=s[i][j]
if m==0:
    print("No suitable girl found")
else:
    q=[]
    for i in range(N):
        for j in range(M):
            if m==s[i][j]:
                q.append([i,j])
    d=[]
    x1=0
    y1=0
    for i in q:
        x2=i[0]
        y2=i[1]
        dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
        d.append(dist)
    di=set(d)
    if len(d)!=len(di):
        print("Polygamy not allowed")
    else:
        bride=min(d)
        for i in range(0,len(d)):
            if d[i]==bride:
                print((q[i][0]+1),":",(q[i][1]+1),":",m)
    


            
