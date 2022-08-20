# 두 배열의 원소 교체

# # N개의 원소와 최대 K번의 바꿔치기
# N , K = map(int,input().split())
#
# # A,B의 원소들
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
#
# # 원소를 바꿔 최댓값 구하기
# # A의 원소는 오름차순으로 , B의 원소는 내림차순으로
# Asum = 0
#
# sortA = sorted(A)
# sortB = sorted(B,reverse=True)
#
# for i in range(N):
#     if i < K:
#         if sortA[i] <= sortB[i]:
#             Asum += sortB[i]
#         else:
#             Asum += sortA[i]
#     else:
#         Asum += sortA[i]
#
# print(Asum)


# 책 답안
N , K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break
print(sum(A))