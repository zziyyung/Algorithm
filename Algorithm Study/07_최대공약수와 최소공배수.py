#백준 2609번
#### 런타임 에러(IndexError)!

##함수 선언부
def commonDivisor(num):
    List=[]
    for i in range(1,num+1):
        if num%i==0:
            List.append(i)
    return List

def commonMultiple(num):
    List=[]
    for i in range(1,11):
        List.append(num*i)
    return List

##전역 변수부
import sys
a,b=map(int,sys.stdin.readline().split())
# 10,000이하의 자연수


##메인 코드

#최대공약수 :
# 나머지가 0인 것들을 리스트로 반환 후,
# 대소비교하여 같은 것들(리스트 개수 안 맞으니 이중 for문?)을 재 리스트로 반환 후,
# 마지막 것 출력(=제일 큰 수)
#
# // : 몫 , % :나머지

aDivisor=commonDivisor(a)
bDivisor=commonDivisor(b)

greatCommonDivisor=[]
for i in range(len(aDivisor)):
    for j in range(len(bDivisor)):
        if aDivisor[i]==bDivisor[j]:
            greatCommonDivisor.append(bDivisor[j])
print(greatCommonDivisor[-1])

#최소공배수 :
# 배수 중 처음으로 일치하는 수
# 일단은 10개로 개수 제한 해보겠슴둥

aMultiple=commonMultiple(a)
bMultiple=commonMultiple(b)
leastCommonMultiple=[]

for k in range(len(aMultiple)):
    for l in range(len(bMultiple)):
        if aMultiple[k] == bMultiple[l]:
            leastCommonMultiple.append(bMultiple[l])
            break
print(leastCommonMultiple[0])


###유클리드호제법

##함수 선언부
def gcd(a,b):
    if (b>a):
        a,b=b,a
    while (b!=0):
        a=a%b
        a,b=b,a
    return a

def lcm(a,b):
    result=(a*b)//gcd(a,b)
    return result

##전역 변수부
import sys
a,b=map(int,sys.stdin.readline().split())

##메인 코드
print(gcd(a,b))
print(lcm(a,b))


###내장함수
import math
import sys
a,b=map(int,sys.stdin.readline().split())

print(math.gcd(a,b))
print(math.lcm(a,b))

###숏코딩
a,b=map(int,input().split());L=a*b
while b:a,b=b,a%b
print(a,L//a)

##쩡님
n, m = map(int, input().split())
n_fips = [i for i in range(1, n + 1) if n % i == 0]  # factorization in prime factors(소인수 분해)
m_fips = [j for j in range(1, m + 1) if m % j == 0]
nm_gcd_lst = []  # 공약수 리스트
# print(n_fips)
# print(m_fips)

for i in range(len(n_fips)):
    if n_fips[i] in m_fips:
        nm_gcd_lst.append(n_fips[i])
nm_gcd = nm_gcd_lst[len(nm_gcd_lst) - 1]
print(nm_gcd)  # 최대 공약수

n_rem = n // nm_gcd
m_rem = m // nm_gcd
nm_lcm = nm_gcd * n_rem * m_rem
print(nm_lcm)  # 최소 공배수

#혠님

## 방법 1

# 두 개의 자연수를 입력 받음 (10000이하의 자연수)
while True:
    a, b = map(int, input().split(' '))
    if 1 <= a <= 10000 and 1 <= b <= 10000:
        break

# 둘 중 큰 수가 max_num, 작은 수가 min_num
max_num, min_num = 0, 0

if a < b:
    min_num = a
    max_num = b
else:
    min_num = b
    max_num = a

## 최대공약수 구하기
# 최대공약수는 둘 중 작은 수보다는 무조건 작으니까 min_num부터 시작
for i in range(min_num, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

## 최소공배수 구하기
# max_num부터 두 수를 곱한 수까지 반복 / 최소공배수는 max_num보다는 무조건 큼
for i in range(max_num, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break
