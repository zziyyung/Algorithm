from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, item):
        # queue2에 새로운 요소를 추가
        self.queue2.append(item)

        # queue1의 모든 요소를 queue2로 이동
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # queue1과 queue2를 교환
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # queue1에서 요소를 제거하여 반환
        if self.queue1:
            return self.queue1.popleft()
        else:
            return None

    def top(self):
        # queue1의 첫 번째 요소를 반환
        if self.queue1:
            return self.queue1[0]
        else:
            return None

    def empty(self):
        # queue1이 비어 있으면 스택도 비어 있는 것으로 간주
        return not self.queue1


# 사용 예시
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 출력: 3
print(stack.top())  # 출력: 2
print(stack.empty())  # 출력: False
print(stack.pop())  # 출력: 2
print(stack.pop())  # 출력: 1
print(stack.empty())  # 출력: True