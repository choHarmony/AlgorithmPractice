import sys

n = int(sys.stdin.readline())
coo = []

for i in range(n) :
    xy = sys.stdin.readline().strip()
    x = int(xy.split(' ')[0])
    y = int(xy.split(' ')[1])
    coo.append((x, y))

coo.sort(key = lambda x : (x[1], x[0]))

for k in coo :
    print(*k)