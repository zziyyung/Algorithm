def solution(participant, completion):
    answer = ''
    # 1. 정렬한다
    participant.sort()
    completion.sort()

    # 2. 반복문 돌면서 비교한다
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    if answer == '':
        answer = participant[-1]
    return answer