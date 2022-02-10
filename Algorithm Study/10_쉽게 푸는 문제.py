# 백준 1292번
# 틀렸습니다
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 ..

import sys
## 함수 선언부

def numbers(a,b):
    numbers_list = []
    for i in range(1,46): #수열 범위 지정 어떻게 ? while?
        for j in range(1,i+1):
            # print(i)
            numbers_list.append(i)
    return sum(numbers_list[a-1:b])

        # 1 = 1
        # 2 = 2 2
        # 3 = 3 3 3
        # 별찍기 ?

## 전역 변수부

a,b=map(int,sys.stdin.readline().split())
# print(N)

## 메인 코드

print(numbers(a,b))



#혠님
# 구간의 시작과 끝을 나타내는 정수 A, B
A, B = map(int, input().split(' '))

# 구간에 속하는 숫자 만들기 (1000개)
# 1부터 44까지 만들면 990개 + 45 숫자 10개 추가
sequence = []
for i in range(45):
    for j in range(1, i+1):
        sequence.append(int(i))

for k in range(10):
    sequence.append(int(45))

# 구간에 속하는 숫자의 합
sum = 0
for i in range(A-1, B):
    sum += sequence[i]

print(sum)

# 쩡님
try:
    N = int(input())
    a = [i for i in map(int, input().split())]
    if len(a) != N:
        raise Exception("숫자의 개수를 확인해 주세요!")
    prime_num = 0
    for i in a:
        b = [j for j in range(1, i + 1) if i % j == 0]
        if len(b) == 2:
            prime_num += 1
    print(prime_num)
except Exception as e:
    print(e)

