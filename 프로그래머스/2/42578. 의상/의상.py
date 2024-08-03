# 풀이1. 해시 O(N)
def solution(clothes):
    # 1. hash map을 만들어 옷을 종류별로 구분하기
    hash_map = {}
    # 이중 for문에서 변수명을 지정해 바로 값을 가져오는 python for문에서 지원되는 기능, O(N)
    for cloth, type in clothes:
        # hash map에 type이 존재하는지 확인하고 있다면 +1, 없다면 0으로 초기화
        hash_map[type] = hash_map.get(type,0) + 1

    # 2. 각 key 별로 none (안입는 경우)도 포함하여 모든 경우의 수 구한다, O(K)
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)

    # 3. (none,none) 경우의 수 -1 빼준다 O(1)
    return answer-1


# 풀이2. Counter, O(N)
from collections import Counter
from functools import reduce
def solution(clothes):
    counter = Counter([type for cloth, type in clothes])
    answer = reduce(lambda acc, cur : acc * (cur+1), counter.values(), 1)
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
