# 확인하기


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

# 테스트
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # 3
print(s.peek())  # 2
print(s.is_empty())  # False