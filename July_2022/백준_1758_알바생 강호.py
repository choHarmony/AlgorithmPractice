import sys

n = int(sys.stdin.readline())
tiplst = []
tip = 0
i = 1

for k in range(n) :
    tip_think = int(sys.stdin.readline())
    tiplst.append(tip_think)

tiplst.sort(reverse=True)

for j in tiplst :
    a = j - (i-1)
    if a >= 0 :
        tip += a
    i += 1

print(tip)