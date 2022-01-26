##함수
# def train(a,b):
#     cal=(2n+1)*b - n*a

# for n in range(1,11): #어차피 10번이니까 1,11아니고 10넣어도 됨
#     input()
#     a,b=input().split()
#     cal=[]
#     ccal=((2*int(n))+1)*int(b) -(int(n)*int(a))
#     cal.append(ccal)
#     print(max(cal))

#########구글링

# x=x_max=0
# for _ in range(10):
#     a,b=map(int,input.split())
#     if x_max<x-a+b:
#         x_max=x-a+b
#     x=x-a+b
# print(x_max)

#########
# import sys
# input=sys.stdin.readlines() #input 입력시 시간초과 문제로 사용
#
# # 정윤님
# customers = []  # 타고 내리는 승객의 수
# current = []  # 현재 탑승하고 있는 승객의 수
# sum_ = 0
# max_ = 0
# for i in range(10):
#     in_, out_ = map(int, input.split())
#     customers.append((in_, out_))  # 타고 내리는 승객의 수 customers리스트에 추가하기
#     sum_ += (customers[i][1] - customers[i][0])  # 현재 열차에 탑승해 있는 승객의 수 구하기
#     current.append(sum_)  # 현재 열차에 탑승해 있는 승객의 수를 current리스트에 추가
#     if current[i] > max_:
#         max_ = current[i]  # 현재 탑승해 있는 열차 승객 수의 최대값 구하기
# print(max_)
# print(customers)
# print(current)

#혜인님

import sys
input=sys.stdin.readline

hap = 0     # 기차 탑승 인원
max = 0     # 기차 최대 탑승 인원

for i in range(10):
    # 순서대로 내린 사람, 탄 사람
    a, b = map(int, input().split())
    hap = hap - a + b

    # 최대값보다 크면 max에 대입
    if hap > max:
        max = hap

print(max)



import sys

current=0
maxpass=0

for i in range(10) :
    A, B=map(int, sys.stdin.readline().split())
    current-=A
    current+=B
    if maxpass < current : maxpass=current

print(maxpass)