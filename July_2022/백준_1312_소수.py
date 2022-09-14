import sys

a, b, c = map(int, sys.stdin.readline().split())
cnt = 0
lst = []

rest = a % b

while rest != 0 :
    lst.append((rest * 10) // b)
    rest = (rest * 10) % b
    cnt += 1

    if cnt == 1000000 :
        break

if c > len(lst) : 
    print(0)
else : 
    print(lst[c - 1])