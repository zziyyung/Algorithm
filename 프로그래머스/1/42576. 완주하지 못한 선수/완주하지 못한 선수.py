# 풀이1. srot & loop , O(n log n)
def solution(participant, completion):
    answer = ''
    # 1. 각각 정렬한다, O(n log n),O(m log m)
    participant.sort()  
    completion.sort()   
    #print(participant,completion)

    # 2. 반복문 돌면서[O(m)] 비교한다[O(1)
    for i in range(len(completion)):     
        if participant[i] != completion[i]:  
            return participant[i]

    # 전부 다 돌아도 없을 경우에 마지막 주자가 미완주자 , O(1)
    return participant[-1]  


# 풀이2. 해시, O(n)
# 해시 = key, value
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    # 1. participant list의 hash를 구하고, hash 값을 더한다, O(n)
    for part in participant:  
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 2. completion list의 hash를 구하고 hash 값을 뺀다, O(m)
    for comp in completion: 
        sumHash -= hash(comp)

    # 3. 남은 값 = 완주하지 못한 사람, 남은 hash값을 통해 사람을 반환한다 , O(1)
    return hashDict[sumHash]  



# 풀이3. Counter, O(n)
# collections 모듈의 Counter 클래스 사용, 빼기 연산 가능
from collections import Counter
def solution(participant, completion):
    # 1. participant의 Counter를 구한다, O(n)
    c_participant = Counter(participant)
    # 2. completion의 Counter를 구한다, O(m)
    c_completion = Counter(completion)
    # 3. partipant - complention 후, 키값을 읽어온다  , O(n),O(1)
    answer = c_participant-c_completion

    # 번외. 짧게 쓰기
    # answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"]))


