n = int(input())		# 컴퓨터의 수
m = int(input())		# 연결된 컴퓨터 쌍의 수

# 인접리스트 graph 선언 및 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):							# 연결된 컴퓨터 쌍의 수만큼 반복
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)
print(graph)

visited = [0] * (n+1)	# 방문처리 : 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리


def dfs(v): #1-2-3-5-6까지만 4-7 무시
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited)
print(sum(visited)-1)	