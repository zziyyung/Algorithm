# 큰 수의 법칙

# ## 내 풀이
# N,M,K = map(int,input().split())
# numList = list(map(int,input().split()))
#
# # 1. 가장 큰 값을 max함수로 구하고
# # 2. 그 다음 큰 값을 가장 큰 값을 제외한 리스트에서 다시 max함수로 구한다
# maxNum1 = max(numList)
# # 가장 큰 수를 리스트에서 제거하기
# numList.remove(maxNum1)
# maxNum2 = max(numList)
#
# # 반복이 필요한가 ?
# # 1. M // K 만큼 maxNum1을 곱할 수 있다 = 몫값*(K*maxNum1)
# # 2. M % k 만큼 maxNum2를 더할 수 있다 = 나머지값*maxNum2
# # 3. 위의 두개를 더한다
#
# q = M//K
# r = M % K
#
# result = (q*(K*maxNum1)) + (r*maxNum2)
# print(result)

## 책01 : 단순하게 푸는 예시 ( 주어진 문제의 범위에서는 풀리나 범위가 더 커지면 시간초과로 에러 )
# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1  # 더할 때 마다 m에서 -1을 해 0까지 만들기
#     if m == 0:
#         break
#     result += second # 위에 k 범위까지 하고 남은 값들을 두번째 큰 수로 더하기
#     m -= 1
#
# print(result)
#
# ## 책02 : 수학적 아이디어로 효율적이게
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)