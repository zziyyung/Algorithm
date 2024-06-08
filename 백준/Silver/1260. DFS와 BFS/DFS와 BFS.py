# 노드 번호 낮은 순서대로 방문

# 정점, 간선, 시작 정점 번호
n, m, v = map(int, input().split())

# 행렬 만들기, (정점 개수+1 만큼 생성)
# 방문 한다 = 1, 방문하지 않는다 = 0
graph = [[0]*(n+1) for _ in range(n+1)]

# 간선 체크, 방문하는 노드 체크
for i in range(m):
    r, c = map(int, input().split())
    graph[r][c] = graph[c][r] = 1

# 방문 여부 체크
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    # 시작 노드 방문 처리
    visited_dfs[v] = True
    print(v, end=' ')

    # 행렬의 0번째는 사용하지 않기 때문에 1부터 시작
    for i in range(1,n+1):
        # 노드끼리 연결되어 있고, 아직 방문하지 않았다면
        if graph[v][i] == 1 and visited_dfs[i] == False:
            dfs(i)

# deque를 통한 queue 사용
from collections import deque
def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        visited_bfs[v] = True
        print(v, end=' ')

        for i in range(1,n+1):
            if graph[v][i] == 1 and visited_bfs[i] == False:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)