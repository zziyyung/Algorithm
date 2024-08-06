# 외벽 점검
from itertools import permutations # 순열

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    answer = len(dist) + 1 # 왜 ?

    # 0부터 length -1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구를 투입
                    if count > len(dist):  # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

## 풀이 2
import math
from itertools import permutations


def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = math.inf

    for start in range(weakSize):
        for d in permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weakSize):
                nextPos = start + i  # nextPos == 인덱스값
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt - 1]:  # 첫번째 친구가 사용할 인덱스는 0이라 -1
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):  # 초과되지 않았는가 ?
                minCnt = min(minCnt, cnt)
    if minCnt == math.inf:
        return -1
    return minCnt