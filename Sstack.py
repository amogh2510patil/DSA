from collections import deque
stack = deque()
stack.append(23)
stack.append(243)
stack.append(13)
stack.append(549)
stack.append(420)
t = stack
s = stack.copy()
stack.pop()
print(stack)
print(s)
print(t)