# 백준 11399 ATM

# 줄 서 있는 사람의 수 N
# 돈을 인출하는데 걸리는 시간 P
# 돈을 인출하는데 필요한 시간의 합의 최솟값

# P를 가장 작은 시간 기준으로 정렬

N = int(input())
time = list(map(int,input().split()))

# 재정렬
time.sort()

# 합 더하기
sum = 0

for i in range(N):
    for j in range(i+1):
        sum += time[j]

print(sum)


# 방법 2
# for i in range(1,n):
#     arr[i] += arr[i-1]
#

# 방법 3
# for i in range(1, N+1):
#     answer += sum(P[:i])