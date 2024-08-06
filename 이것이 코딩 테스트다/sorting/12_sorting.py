# 실패율

def solution(N, stages):
    length = len(stages)
    result = []
    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        length -= count
        result.append((i, fail))
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    answer = [res[0] for res in result]
    return answer