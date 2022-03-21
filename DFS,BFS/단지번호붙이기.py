n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

grp=[]
cnt=0
dx=[-1,1,0,0] #상하좌우 
dy=[0,0,-1,1]

def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return False

    if graph[x][y]==1: #1일 때
        cnt+=1  #카운트를 1 올리고
        graph[x][y]=0 #방문한 곳을 0으로 변경 
        for i in range(4):
            dfs(x+dx[i],y+dy[i]) 
        return True

for i in range(n): #graph를 돌면서
    for j in range(n): 
        if dfs(i,j)==True: #다 돌고 True를 반환하면 (방문처리가 되었으면)
            grp.append(cnt) #grp에 cnt를 추가
            cnt=0 #cnt 값 초기화

print(len(grp))
grp.sort()
for i in grp:
    print(i)