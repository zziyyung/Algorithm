# 백준 18405 : 경쟁적 감염

from collections import deque

# 1. 정보 입력 받기
n , k = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n)]

# 1-1. 바이러스에 대한 정보 담는 리스트 생성
data = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j)) # 바이러스의 종류 , 시간, x위치 , y위치

# 1-2. 정렬 이후에 큐로 옮기기
data.sort()
q = deque(data)

target_s , target_x , target_y = map(int,input().split())


# 2. 네가지 방향 설정
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 3. BFS 진행
while q:
    virus,s,x,y = q.popleft()
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 or nx < n or ny >= 0 or ny < n :
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))

print(graph[target_x - 1][target_y - 1])
