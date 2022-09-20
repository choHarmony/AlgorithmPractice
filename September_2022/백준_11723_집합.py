import sys

s = set()
m = int(input())

for _ in range(m) :
    do = sys.stdin.readline().strip().split(' ')
    if len(do) > 1 :
        cmd = do[0]
        num = int(do[1])
    else :
        cmd = do[0]

    if cmd == 'add' :
        s.add(num)
    elif cmd == 'remove' :
        if num in s :
            s.remove(num)
    elif cmd == 'check' :
        if num in s :
            print(1)
        else :
            print(0)
    elif cmd == 'toggle' :
        if num in s :
            s.remove(num)
        else :
            s.add(num)
    elif cmd == 'all' :
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif cmd == 'empty' :
        s = set()