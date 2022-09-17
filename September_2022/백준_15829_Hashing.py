import sys
from string import ascii_lowercase

alphabet = list(ascii_lowercase)
n = int(sys.stdin.readline().strip())
s = list(sys.stdin.readline().strip())
ans = 0
idx = 0

for i in s :
    ans += (alphabet.index(i)+1) * 31**idx
    idx += 1

print(ans%1234567891)