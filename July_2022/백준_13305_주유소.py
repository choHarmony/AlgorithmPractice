import sys

n = int(sys.stdin.readline())
km = [int(x) for x in sys.stdin.readline().split()]
moneyperliter = [int(x) for x in sys.stdin.readline().split()]
res = 0

if set(tuple(moneyperliter)) == {1} :
    print(sum(km))

else :
    res += moneyperliter[0] * km[0]
    money = moneyperliter[0]
    for i in range(1, len(km)) :
        if money > moneyperliter[i] :
            money = moneyperliter[i]
            res += money * km[i]
        else :
            res += money * km[i]
    print(res)