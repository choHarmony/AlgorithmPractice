import sys

nA, nB = map(int, sys.stdin.readline().split())
A = set([int(nA) for nA in sys.stdin.readline().split()])
B = set([int(nB) for nB in sys.stdin.readline().split()])

if len(A-B) == 0 :
    print(0)
else :
    print(len(A-B))
    print(*sorted(list(A-B)))