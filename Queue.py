from collections import deque
queue = deque()
queue.appendleft(23)
queue.appendleft(43)
queue.appendleft(76)
queue.appendleft(90)
print(queue)
queue.pop()
print(queue)