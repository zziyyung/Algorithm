# 백준 1978번

#소수= 나눴을 때 약수가 자기 자신과 1 , 개수=2개X ->1은 제외
# 실패 , 내가 푼 방법 : 소수의 정의에 충실한 방법이면서 무식하지만 가장 강력한 방법 but, 범위의 모든 소수를 구할 때는 효율적인 방법이 아님

import sys
## 함수 선언부
def getSosu(num):
    cnt = 0
    sosu = []
    for i in num:
        if i == 1:
            continue
        else:
            # 3일 경우, 3%1 3%2 3%3 에서 나머지 0인 것이 2개이면 소수
            for j in range(1, i + 1):
                if i % j == 0:  # 의 개수가 2
                    sosu.append(j)
            if len(sosu) == 2:
                cnt += 1
    return cnt

## 전역 변수부
#T=int(sys.stdin.readline())
#num=list(map(int,sys.stdin.readline().split()))

## 메인 코드
#print(getSosu(num))



#에라토스 테네스의 체 : 소수(Prime Number)판별 알고리즘

import sys

input = sys.stdin.readline

n = int(input())
array = (list(map(int, input().split())))
end = max(array)
#print(end)

check = [i for i in range(end + 1)]  # 숫자와 인덱스를 같게 해주기 위해서 배열길이 +1
check[1] = 0  # 0, 1번째 인덱스는 0으로 두고 2번째부터 인덱스 = 값(숫자) 일치시킬수있도록
count = 0
# 0 0 2 3 4 5 6 7
for i in check[2:]:
    if check[i] == 0:  # 첫시작부터 0이면 다음번으로 뛰기 (4와같이 2로인해 이미 표시된것들)
        continue
    else:
        for j in range(2, (end // i) + 1):  # 자기자신은 뺴야하므로 배수를 만들기위해 곱하는 숫자는 2부터시작, 끝은 배수가 최대숫자를 넘기지 않아야 하므로 end//i로한다.
            if check[i * j] == 0:  # 만약 넘어가고 있는 배수가 이미 체크되었으면 건너띄고
                continue
            else:
                check[i * j] = 0  # 그렇지 않다면 0으로 만들면서 체크한다.
count = 0
for i in array:
    if i in check:
        count += 1

''' check 배열최종 : [0, 0, 2, 3, 0, 5, 0, 7] '''

print(count)


# 혠님
# 소수 : 약수가 본인과 1만 가지는 수

N = int(input())  # 수의 개수 : 100 이하
N_num = list(map(int, input().split()))  # 1000 이하의 자연수

PN_count = 0  # 주어진 수들 중 소수의 개수
for i in range(N):
    N_count = 0  # 각 숫자별 약수의 개수 (초기화)

    for j in range(1, N_num[i] + 1):
        if N_num[i] % j == 0:
            N_count += 1

    if N_count == 2:  # 1과 본인
        PN_count += 1

print(PN_count)
