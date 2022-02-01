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