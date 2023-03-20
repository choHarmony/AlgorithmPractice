import sys

t = int(sys.stdin.readline())

for i in range(t) :
    dic = {'(': 0, ')': 0}
    s = sys.stdin.readline().strip()
    if s[0] == ')':
        print('NO')
        continue
    elif s[-1] == '(':
        print('NO')
        continue
    for k in s :
        if k == '(' :
            dic[k] += 1
        elif k == ')' and dic['('] >= 1 :
            dic[k] += 1
            dic['('] -= 1
            dic[')'] -= 1
        elif k == ')' :
            dic[k] += 1
    if dic['('] == 0 and dic[')'] == 0 :
        print('YES')
    else :
        print('NO')
