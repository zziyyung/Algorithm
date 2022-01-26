##이진검색 (실무에서 아주 중요 !)
import random
##함수
def binSearch(ary,fData):
    pos=-1 #못 찾으면 return pos
    start=0
    end=len(ary)-1
    while (start <= end) :
        mid=(start+end)//2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start=mid+1
        else:
            end=mid-1

    return pos

##전역
SIZE=10
dataAry=[random.randint(1,99) for _ in range(SIZE)]
findData=dataAry[random.randint(0,SIZE-1)]
dataAry.sort()  #정렬


##메인
print('배열: ',dataAry)
position=binSearch(dataAry,findData)
if position ==-1: #못 찾음
    print(findData,'없어요')
else:
    print(findData,'가',position,'에 있음')