# 스택

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])


# 큐
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# print(list(queue))  : deque가 아닌 list 형태로 출력


# 재귀함수

# 팩토리얼 예제 1. 반복문으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 팩토리얼 예제 2. 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적 구현 : ", factorial_iterative(5))
print("재귀적 구현 : ", factorial_recursive(5))
