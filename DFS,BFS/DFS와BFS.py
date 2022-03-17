import sys
from collections import deque

def dfs(n):
    visited[n]=True
    print(n,end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n): 
    queue=deque([n]) #큐 생성
    visited[n]=True #첫번째 노드 방문처리
    while queue:
        v=queue.popleft() #1번 팝하고 v에 저장
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

N,M,V=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort() #정렬 필요 [5,1]x [1,5]o


visited=[False]*(N+1)
dfs(V)
print()
visited=[False]*(N+1)
bfs(V)