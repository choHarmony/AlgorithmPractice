import sys

while True :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 :
        break
    case = sorted([a, b, c])
    if case[2]**2 == case[0]**2+case[1]**2 :
        print('right')
    else :
        print('wrong')