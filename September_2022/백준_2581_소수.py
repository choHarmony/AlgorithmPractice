m = int(input())
n = int(input())
lst = []

for i in range(m, n+1) :
    num = 2
    while num < i :
        if i % num == 0 :
            break
        else :
            num += 1
    else :
        lst.append(i)

if 1 in lst :
    lst.remove(1)

if not lst :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))