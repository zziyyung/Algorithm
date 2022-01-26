##함수

##전역
# stack =[None,None,None,None,None]
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

##메인
#push
top +=1
stack[top]='커피'
top +=1
stack[top]='녹차'
top+=1
stack[top]='꿀물'

print(stack)

#pop
data=stack[top]
stack[top]=None #뺏던 자리 값 지우기
top -=1
print('팝-->' ,data)

data=stack[top]
stack[top]=None
top -=1
print('팝-->' ,data)

data=stack[top]
stack[top]=None
top -=1
print('팝-->' ,data)

print(stack)