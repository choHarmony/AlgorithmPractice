import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for i in range(1, n+1) :
    q.append(i)

while True :
    if len(q) == 1 :
        break
    else :
        q.popleft()
        q.append(q.popleft())

print(q.popleft())