import sys

t = int(input())

for i in range(t) :
    n = int(input())
    dic = {}
    cnt = 1
    for k in range(n) :
        a = sys.stdin.readline().strip().split(' ')
        try :
            dic[a[1]] += 1
        except :
            dic[a[1]] = 1
    for j in dic.values() :
        cnt *= j+1
    print(cnt-1)