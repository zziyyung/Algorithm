num=input("1<=N<=10,000 1<=K<=N :")
a,b=num.split()

A=int(a)
B=int(b)

yaksu=[i for i in range(1, A+1) if A%i == 0]

print(f'{A}의 약수는 {yaksu} 총{len(yaksu)}개이다.')

if B > len(yaksu):
    print('0')
else:
    print(yaksu[B-1])

#yaksu = []
# for i in range(1,A+1):
#     if A%i==0:
#         yaksu.append(i)
#     else:
#         continue
#print(f'{A}의 약수는 {yaksu} 총{len(yaksu)}이다.')

#if B > len(yaksu):
#    print('0')
#else:
#    print(yaksu[B-1])

#정윤님
try:
    n, k = map(int, input('숫자를 입력해 주세요').split())
    if not (1 <= n <= 10000 and 1 <= k <= n): # 예외 범위 정하기
        raise Exception('잘못 입력하셨습니다.')
    # a=[i for i in range(1, A+1) if A%i == 0]
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)

    print(a[k - 1])
except IndexError:
    print(0)
except Exception as e:
    print(e)

#혜인님
while True:
    N, K = map(int, input().split())
    if 1 <= N <= 10000:
        break

K_list = []     # 약수 저장 리스트

for i in range(1, N+1):
    if N % i == 0:
        K_list.append(i)
    else:
        continue

if len(K_list) < K:
    print('0')
else:
    print(K_list[K-1])

#재영님
N = int(input('자연수를 입력하시오: '))
numN =[]
for i in range(1,N+1):
    if N >= 1 and N <= 10000:
        if N % i == 0:
            numN.append(i)

    else:
        print("1 이상 10,000 이하의 자연수를 입력하시오.")
        break
print(numN)

print("약수의 개수: ",len(numN))
K = int(input('원하는 순서의 약수를 입력하시오: '))


if K > len(numN):
    print(0)
else:
    print(numN[K-1])




