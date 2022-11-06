import sys

t = int(sys.stdin.readline())

for i in range(t) :
    n = int(sys.stdin.readline())
    cnt = 0
    k = 5
    while k <= n :
        cnt += n // k
        k *= 5
    print(cnt)