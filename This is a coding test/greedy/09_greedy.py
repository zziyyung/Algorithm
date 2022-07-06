# 볼링공 고르기

import time

start_time = time.time()  # 측정 시작

##### 나의 풀이

N,M = map(int,input().split())
data = list(map(int,input().split()))

sum = 0
count = N-1

# 등차수열 (합 구하기
for _ in range(len(data)):
    sum += count
    count = count - 1

#print(sum)

# 리스트 내 중복값 카운트하기
# 구글링 set 자료형 !

dup = len(data) - len(set(data))

print(sum-dup)

##### 책 풀이

array = [0] * 11  # 배열 내 11개 요소 생김 0~11 ( 0번째는 버리고 1~10 사용)
# print(array)

for x in data:
    array[x] += 1

#print(array)

result = 0

for i in range(1,N+1):   # 1부터 n까지 각 무게에 대하여 처리
    N -= array[i]  # B가 선택할 수 있는 경우의 수
    result += array[i] * N

print(result)


# 프로그램 소스코드
end_time = time.time()  # 측정 종료
print('time :', end_time - start_time)  # 수행시간 출력
