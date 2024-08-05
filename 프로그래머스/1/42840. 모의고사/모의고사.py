# 풀이1. loop & enumerate , O(N)
def solution(answers):
    # 1. 수포자 3명의 패턴을 각각 정의한다, O(1)
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]

    # 2. 수포자 3명의 맞춘 개수를 담을 리스트를 선언한다, O(1)
    score = [0] * 3
    result = []

    # 3. enumerate를 사용해 한명씩 점수를 비교하면서 맞춘 개수를 카운트한다, O(N)
    for idx, answer in enumerate(answers):
        if answer == supo1[idx%len(supo1)]:
            score[0] += 1
        if answer == supo2[idx%len(supo2)]:
            score[1] += 1
        if answer == supo3[idx%len(supo3)]:
            score[2] += 1

    # 4. 맞춘 개수를 비교하여 최대값을 도출한다, O(1)
    for idx, s in enumerate(score,1):
        if s == max(score):
            result.append(idx)

    return result

print(solution([1,3,2,4,2]))
