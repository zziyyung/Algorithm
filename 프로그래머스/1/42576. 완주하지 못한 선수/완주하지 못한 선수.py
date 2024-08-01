def solution(participant, completion):
    answer = ''
    # 1. 정렬한다
    participant.sort()
    completion.sort()

    # 2. 반복문 돌면서 비교한다
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 전부 다 돌아도 없을 경우에 마지막 주자가 미완주자
    return participant[-1]