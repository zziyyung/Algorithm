# 14888번
# 재귀 탐색의 기본 : 연산자 끼워넣기
import sys

# 함수 선언부

# 연산기호 + - * /
# T의 개수보다 1개 적어야함

# 최대 최소  : 비교

# # 전역 변수부
# T = list(map(int,sys.stdin.readline().split()))
# N = list(map(int,sys.stdin.readline().split())) # 들어온 수를 일단 리스트
# a,b,c,d = list(map(int,sys.stdin.readline().split())) # 0 0 0 0

# 메인 코드

T = list(map(int,sys.stdin.readline().split()))


if 1 in T:
    print("1")
if 2 in T:
    print("2")

print(T)

[dfs]
https://butter-shower.tistory.com/223
