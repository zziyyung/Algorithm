# 큰 수의 법칙

## 내 풀이
n, m, k = map(int, input().split())
list = list(map(int, input().split()))
list = sorted(list, reverse=True)

cnt = 0
sum = 0

for i in range(m):
    if cnt != k:
        sum += list[0]
        cnt += 1
        print("if : ", cnt,sum)
    else:
        sum += list[1]
        cnt = 0
        print("else : ",cnt,sum)

print(cnt, sum)

## 책01 : 단순하게 푸는 예시 ( 주어진 문제의 범위에서는 풀리나 범위가 더 커지면 시간초과로 에러 )
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때 마다 m에서 -1을 해 0까지 만들기
    if m == 0:
        break
    result += second # 위에 k 범위까지 하고 남은 값들을 두번째 큰 수로 더하기
    m -= 1

print(result)

## 책02 : 수학적 아이디어로 효율적이게
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