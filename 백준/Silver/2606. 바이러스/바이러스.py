import sys

# 노드, 간선 입력 받기
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

# 노드 연결상태 graph로 그리기
graph = [[] for _ in range(n+1)]

for i in range(m):
    index, val = map(int,input().split())
    graph[index].append(val)
    # key point : 언제나 1부터 등장한다는 보장이 없기 때문
    graph[val].append(index)

# 방문 체크
visited = [False] * (n+1)

def dfs(graph, v, visted):
    visted[v] = True

    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

dfs(graph,1,visited)
print(sum(visited)-1)
