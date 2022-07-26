# 치킨 배달
from itertools import combinations

n , m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
chicken , house = [] , []

for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            house.append((r,c))
        elif data[r][c] == 2:
            chicken.append((r,c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합
candidates = list(combinations(chicken,m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    for hx,hy in house:
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)