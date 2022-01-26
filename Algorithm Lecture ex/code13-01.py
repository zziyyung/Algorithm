import random

##함수
def seqSearch(ary,fData):
    pos=-1 #못 찾으면 return pos
    size=len(ary)
    for i in range(0,size,1): #=range(size)
        if (ary[i] == fData):
            pos=i
            break
    return pos

##전역
SIZE=10
dataAry=[random.randint(1,99) for _ in range(SIZE)]
findData=dataAry[random.randint(0,SIZE-1)]


##메인
print('배열: ',dataAry)
position=seqSearch(dataAry,findData)
if position ==-1: #못 찾음
    print(findData,'없어요')
else:
    print(findData,'가',position,'에 있음')