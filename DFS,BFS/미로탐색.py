from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4): #동서남북 4면 체크
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1 #지점까지의 거리를 기존 위치까지의 거리+1로 설정
                queue.append((nx,ny))
    return graph[n-1][m-1] #맨 아랫줄에 위치하게 되면 리턴

print(bfs(0,0))
#알고리즘 책 미로탈출이랑 똑같은 문제
#지나야 하는 최소의 칸 수를 출력한다라는 조건이 있으면 이와 같은 알고리즘을 사용하면 된다.