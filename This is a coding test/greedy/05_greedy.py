# 모험가 길드

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여
# 여행을 떠날 수 잇는 그룹 수의 최댓값 출력

N = int(input())
numList = list(map(int,input().split()))
numList.sort()

group = 0
cnt = 0 #  현재 그룹에 포함된 모험가의 수

for i in numList:
    cnt += 1
    if cnt >= i :
        group += 1
        cnt = 0

print(group)