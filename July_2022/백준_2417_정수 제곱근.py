from math import ceil
import sys

n = int(sys.stdin.readline())

if ceil(n**0.5) ** 2 >= n :
    print(ceil(n**0.5))
else :
    print(ceil(n**0.5)+1)