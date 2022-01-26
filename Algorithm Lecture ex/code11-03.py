#선택정렬 (완전)

import random
##함수  ##많이 사용함!
def selectionSort(ary):
    n=len(ary)  #데이터 개수
    for cy in range(0,n-1) : #사이클은 데이터 -1
        minIdx = cy
        for i in range(cy+1, n):
            if (ary[minIdx] > ary[i]):
                minIdx = i
        ary[cy] , ary[minIdx] =ary[minIdx] ,ary[cy]
    return ary

##전역
dataAry=[random.randint(100,200) for _ in range(8)]

##메인
print('정렬 전 :' ,dataAry)
dataAry=selectionSort(dataAry)

print('정렬 후 :' ,dataAry)