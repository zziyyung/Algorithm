#백준 10818번
import sys
N=int(sys.stdin.readline())
Input=[int(x) for x in sys.stdin.readline().split() if -1000000<=int(x)<=1000000]
#[map(int,sys.stdin.readline().split())] -- >개수 왜 안되지 ?
#리스트 컴프리헨션은 반복문 ! !!!
#list(map(int,sys.stdin.readline().split())) ->됨


if (N != len(Input)) or (N<1) or (N>1000000):
    print("다시 입력")
else:
    minIdx=0
    maxIdx=0
    for i in range(len(Input)):
        if Input[i]<Input[minIdx]:
            minIdx=i
        elif Input[i]>Input[maxIdx]:
            maxIdx=i
    print(f'{Input[minIdx]} {Input[maxIdx]}')


#함수 선언부
#선택정렬 함수
def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for j in range(i+1,n):
            if (ary[minIdx]>ary[j]):
                minIdx=j
        ary[i],ary[minIdx]=ary[minIdx],ary[i]
    return ary

##전역 변수부
import sys
N=int(sys.stdin.readline())
Input=[int(x) for x in sys.stdin.readline().split()]

##메인 코드
selectionSort(Input)
print(f'{Input[0]} {Input[-1]}')


#쩡님

# N개의 정수가 주어질 때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
## 1) 선택정렬....시간초과......ㅜㅜ
# try:
#     n = int(input())
#     a = [i for i in map(int, input().split())]
#     if n != len(a):
#         print(f'정수 {n}개를 적어주세요!')
#     for i in range(len(a)):
#         min_idx = i
#         for j in range(i + 1, len(a)):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[min_idx], a[i] = a[i], a[min_idx]
#     print(a[0], a[len(a) - 1], sep=' ')
# except Exception as e:
#     print(e)



## 2) 성공!
# try:
#     n = int(input())
#     a = [i for i in map(int, input().split())]
#     if n != len(a):
#         print(f'정수 {n}개를 적어주세요!')
#     min_ = 0
#     max_ = 0
#     for i in range(len(a)):
#         if a[i] < a[min_]:
#             min_ = i
#         if a[i] > a[max_]:
#             max_ = i
#     print(a[min_], a[max_])
# except Exception as e: # 20 10 35 30 7
#     print(e)

# i    min
# a[0]=20 a[0]=20 i=0 min_=0
# a[1]=10 a[0]=20 i=1 min_=1
# a[2]=35 a[1]=10 i=2 min_=1



## 3) 삽입 정렬 시간초과....(for문 2개라 그런 것으로 생각됨)
# n = int(input())
# a = [i for i in map(int, input().split())]
# for i in range(1, len(a)):
#     for j in range(i, 0, -1):
#         if a[j] < a[j - 1]:
#             a[j], a[j - 1] = a[j - 1], a[j]
#         else:
#             break
# print(a[0],a[-1])

#혠님

# 첫째 줄에 입력한 정수의 갯수
# while True :
#     N = int(input())
#     if 1 <= N <= 1000000:
#         break
#
# # 둘째 줄에 입력한 N개의 정수
# num = input()
# new_list=list(map(int,num.split()))
#
# # 리스트 정렬 후 최솟값과 최댓값 출력
# new_list.정렬()
# print(f'{new_list[0]} {new_list[len(new_list)-1]}')
