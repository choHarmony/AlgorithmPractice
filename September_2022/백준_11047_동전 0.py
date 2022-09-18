import sys

n, k = map(int, sys.stdin.readline().split())
money = []
coin = 0

for i in range(n) :
    money.append(int(sys.stdin.readline().strip()))

for j in reversed(money) :
    if j <= k :
        coin += k // j
        k -= (k//j) * j
        continue

print(coin)