import sys

n = int(sys.stdin.readline())
stk = []

for i in range(n) :
    cmd = sys.stdin.readline().strip()
    if cmd[:3] == 'pus' :
        stk.append(int(cmd[5:]))
    elif cmd[:3] == 'pop' :
        if len(stk) == 0 :
            print(-1)
        else :
            print(stk[-1])
            del stk[-1]
    elif cmd[:3] == 'siz' :
        print(len(stk))
    elif cmd[:3] == 'emp' :
        if len(stk) == 0 :
            print(1)
        else :
            print(0)
    elif cmd[:3] == 'top' :
        if len(stk) == 0 :
            print(-1)
        else :
            print(stk[-1])