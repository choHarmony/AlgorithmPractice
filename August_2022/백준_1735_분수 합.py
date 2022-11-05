import sys
import math

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

n = (a*d+b*c) / b*d

e, f = a*d+b*c, b*d
k = math.gcd(e, f)

print(int((a*d+b*c) / k), end=' ')
print(int(b*d / k))