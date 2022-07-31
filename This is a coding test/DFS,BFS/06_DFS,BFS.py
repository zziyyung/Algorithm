# 백준 14502 : 연구소

# 1. 정보 입력받기
n,m = map(int,input().split())
data = [ list(map(int,input().split())) for _ in range(n) ]

# 벽을 설치한 뒤의 맵 리스트 (?)
temp = [ [0]*m for _ in range(n)]

# 2. 4가지 이동방향 설정하기 ( 상, 우, 하, 좌 )
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# ?
result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(x,y)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용해 울타리를 설치하면서 , 매번 안전 영역의 크기 계산
def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result,get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
