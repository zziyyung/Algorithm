# 백준 2309번

## 함수 선언부
def combination(ary):
    n=len(ary)
    sumN=sum(ary)
    for i in range(n-1):
        for j in range(i+1,n):
            if sumN - (ary[i] + ary[j]) == 100:
                remove1 = ary[i]
                remove2 = ary[j]
    ary.remove(remove1)
    ary.remove(remove2)


def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for j in range(i+1,n):
            if (ary[minIdx]>ary[j]):
                minIdx=j
        ary[i],ary[minIdx]=ary[minIdx],ary[i]
    return ary

## 전역 변수부
i=0
List=[]
while i<9:
    num=int(input())
    if (num >100) or (num in List):
        print("다시 입력")
        break
    else:
        List.append(num)
    i+=1

## 메인 코드

combination(List)
selectionSort(List)
print('\n'.join(map(str,List)))




# #혜인님
#     # 9명의 키 입력
#     num = [int(input()) for i in range(9)]
#
#     # 전체 합에서 2명을 제외하면 합이 100
#     sumN = sum(num)
#     a, b = 0, 0
#
#     for i in range(9):
#         for j in range(i + 1, 9):
#             if (sumN - num[i] - num[j]) == 100:
#                 a = num[i]
#                 b = num[j]
#     num.remove(a)  # for문에서 지워버리면 index 길이가 안 맞으니까 밖에서 remove()
#     num.remove(b)
#
#     # 순서대로 정렬 후 출력
#     num.sort()  # 변수로 저장하지 않고 sort()로 정렬만!
#
#     # 출력
#     for i in range(7):
#         print(num[i])
#
# #정윤님
# height = [int(input()) for _ in range(9)]
# a1, a2 = 0, 0
# # [20,7,23,19,10,15,25,8,13]
# for i in range(len(height)):
#     for j in range(i + 1, len(height)):
#         if sum(height) - (height[i] + height[j]) == 100:
#             a1 = height[i]
#             a2 = height[j]
# height.remove(a1)
# height.remove(a2)
#
# for i in range(len(height)):
#     sort_height = i
#     for j in range(i + 1, len(height)):
#         if height[j] < height[sort_height]:
#             height[j], height[sort_height] = height[sort_height], height[j]
# print('\n'.join(map(str, height)))
