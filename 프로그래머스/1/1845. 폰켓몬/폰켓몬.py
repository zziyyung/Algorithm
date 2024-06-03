def solution(nums):
    unique_mon = len(set(nums)) 
    if unique_mon >= (len(nums)/2):
        answer = len(nums)/2
    else:
        answer = unique_mon
    return answer

# 다른 사람 풀이 
# min() 함수로 대소비교 