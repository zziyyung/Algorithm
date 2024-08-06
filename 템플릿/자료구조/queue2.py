from collections import deque

queue = deque()

queue.append(4)
queue.append(5)
print(queue.popleft())

stack = []
stack.append(1)
stack.append(2)

print(stack.peek())