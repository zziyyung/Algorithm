# 카드 정렬하기

import heapq

n = int(input())
array = [int(input()) for _ in range(n)]

q = []
for a in array:
    heapq.heappush(q, a)

result = 0
while len(q) != 1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)
    sum_val = one + two
    result += sum_val
    heapq.heappush(q, result)

print(result)