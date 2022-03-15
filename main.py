n=int(input())
plans=input().split() #R
x,y=1,1

steps=['U','D','L','R']
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for plan in plans:
    for i in range(len(steps)):
        if plan==steps[i]: #R==R
            nx=x+dx[i] #1
            ny=y+dy[i] #2
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)