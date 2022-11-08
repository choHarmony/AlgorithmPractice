import sys

n, m = map(int, sys.stdin.readline().split())
nset = set()
cnt = 0

for i in range(n) :
    word = sys.stdin.readline().strip()
    nset.add(word)

for k in range(m) :
    check = sys.stdin.readline().strip()
    if check in nset :
        cnt += 1

print(cnt)