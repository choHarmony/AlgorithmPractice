import sys
import math

m, n = map(int, sys.stdin.readline().split())

ary = [True for i in range(n+1)]

for k in range(2, int(math.sqrt(n))+1) :
    if ary[k] == True :
        j = 2
        while k * j <= n :
            ary[k*j] = False
            j += 1

for i in range(2, n+1) :
    if ary[i] and i >= m :
        print(i, end='\n')