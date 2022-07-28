# 음료수 얼려먹기 (DFS)

n, m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 좌표 방문처리
        graph[x][y] = 1
        # 상하좌우 위치 모두 재귀적으로 확인
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)