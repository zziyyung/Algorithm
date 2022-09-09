# 백준1181 단어 정렬

import sys

n = int(sys.stdin.readline())
alpha = []

for _ in range(n):
    alpha.append(sys.stdin.readline().strip())

alphaSet = set(alpha)
alphaList = list(alphaSet)

alphaList.sort()   # 선 문자열 정렬
alphaList.sort(key=len)  # 후 길이로 재정렬

for i in alphaList:
    print(i,end='\n')

