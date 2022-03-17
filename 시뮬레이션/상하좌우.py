n=int(input())
plans=input().split()
x,y=1,1

moves=['U','D','L','R'] #(1,1) (1,2) (1,3)
dx=[-1,1,0,0] #U=x-1 D=x+1 L=0 R=0
dy=[0,0,-1,1] #U=0 D=0 L=y-1 R=y+1

for plan in plans:
    for i in range(len(moves)):
        if plan==moves[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)

#뭔가 한칸씩 처리를 하려고 할때 dx,dy를 사용하는것 같다 
#미로 탈출 문제랑 유사하다(bfs)
#음료수 얼려 먹기는 한덩이로 처리를 하는거라서 dx,dy를 사용하지 않는다.(dfs)