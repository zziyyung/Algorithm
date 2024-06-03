def solution(nums):
    unique_mon = len(set(nums)) 
    if unique_mon >= (len(nums)/2):
        answer = len(nums)/2
    else:
        answer = unique_mon
    return answer