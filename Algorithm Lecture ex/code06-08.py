##함수

#스택 꽉 찾는지 확인
def isStackFull():  #is니까 t or f 대부분
    global SIZE,stack,top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data): #데이터 넘겨 받아 푸쉬
    global SIZE, stack, top
    if (isStackFull() == True) :
        print('스택 꽉 찼음 !')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):  #==도 상관 없음
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()) : #(isStackEmpty() == True) 촌시러
        print("스택 텅~")
        return
    data=stack[top]
    stack[top]=None
    top -=1
    return data

def peek(): #맨 위에 뭐 있는지 확인만
    global SIZE, stack, top
    if (isStackEmpty()):  # (isStackEmpty() == True) 촌시러
        print("스택 텅~")
        return
    return stack[top]


##전역
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1


##메인
push('커피1')
push('커피2')
push('커피3')
push('커피4')
push('커피5')
print(stack)
push('커피6')

retData=pop()
print('팝-->',retData)
retData=pop()
print('팝-->',retData)
retData=pop()
print('팝-->',retData)
retData=pop()
print('팝-->',retData)
print(stack)

print('다음 예정-->',peek())