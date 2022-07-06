# 숫자 카드 게임

# min(),max() 사용

N,M = map(int,input().split())

num = 0

# 한 줄씩 리스트화하기
for i in range(N):
    numList = list(map(int,input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    minNum = min(numList)
    # num에 값 넣어주기
    num = max(minNum,num)

print(num)

# 이중 for문 사용

N,M = map(int,input().split())

num = 0

for i in range(N):
    numList = list(map(int, input().split()))

    # 현재 줄에서 가장 작은 수 찾기
    # 나동빈 풀이 ) 문제에서 범위가 10000 이하의 숫자로 제한되었기 때문에 수 비교를 위해 범위 밖으로 최소값 먼저 설정 ?
    min_value = 10001

    for j in range(numList):
        min_value = min(min_value,j)

    num = max(num,min_value)

print(num)