import sys, math

n, k = map(int, sys.stdin.readline().split())
up = 1
for i in range(k) :
    up *= n-i

num = up // math.factorial(k)
print(int(num % 10007))