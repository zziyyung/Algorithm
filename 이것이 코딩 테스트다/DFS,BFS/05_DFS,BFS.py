# 특정 거리의 도시 찾기

from collections import deque

# 1. 정보 입력 받기

n,m,k,x = map(int,input().split())

# 1-1. 인접 리스트 형태로 graph 구성
graph = [ [] for _ in range(n+1) ]  # 도시의 개수만큼(n+1) 리스트 생성
for _ in range(m):   # 도로의 개수만큼 반복해서 값 입력 받기 !!
    a,b = map(int,input().split())
    graph[a].append(b)

# 2. 거리 초기화
distance = [-1] * (n+1)  # 왜 n+1 ?
distance[x] = 0 # 출발 지점에서 출발 지점으로 갈 때의 최단 거리는 항상 0

# 3. 너비 우선 탐색 시작
queue = deque([x])

while queue:
# 큐가 없어질 때 까지 !!!!!
    now = queue.popleft()

    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            queue.append(next_city)

# 4. 최단거리가 k인 모든 도시 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

# 5. 만족하는 경우가 없다면 -1 출력
if check == False:
    print(-1)

