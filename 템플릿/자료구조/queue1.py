# 스택 2개로 큐를 구현하라

class StackQueue:
    def __init__(self):
        # 공간 복잡도 O(n)
        self.in_stack = [] # 입력을 담당할 스택
        self.out_stack = [] # 출력을 담당할 스택

    # 시간복잡도 O(1) :단순히 요소를 추가하는 작업
    def enqueue(self,item):
        # 요소를 in_stack에 추가
        self.in_stack.append(item)

    # 시간 O(1) ~ O(n)
    def dequeue(self):
        # out_stack이 비어있을 경우 = not을 이용해 판단 = 비어있다면 True, 아니면 False
        if not self.out_stack:
            # in_stack의 모든 요소를
            while self.in_stack:
                # 역순으로 out_stack으로 이동
                self.out_stack.append(self.in_stack.pop())

        # 위에서 이동후, out_stack에 값이 있을 경우
        if self.out_stack:
            # out_stack에서 요소를 하나씩 제거 후 반환
            return self.out_stack.pop()
        else:
            # 큐가 비어있을 경우는 None
            return None

    def peek(self):
        # dequeue와 유사하지만 요소를 제거하지 않고 반환함
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return None

    def is_empty(self):
        return not self.in_stack and not self.out_stack


sq = StackQueue()
print(sq.is_empty())
sq.enqueue(3)
print(sq.in_stack)
sq.enqueue(5)
print(sq.in_stack)
sq.dequeue()
print(sq.out_stack)
sq.dequeue()
print(sq.out_stack)
sq.enqueue(9)
print(sq.dequeue())