import heapq

class PriorityQueue:
    def __init__(self):
        self.heap= []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority,item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        return None

    def is_empty(self):
        return len(self.heap) == 0

pq = PriorityQueue()
pq.push("task1", 1)
pq.push("task2", 5)
pq.push("task3", 3)

print(pq.pop())  # 출력: task1 (가장 낮은 우선순위)
print(pq.pop())  # 출력: task2
print(pq.pop())  # 출력: task3