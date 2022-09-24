import sys

n, m = map(int, sys.stdin.readline().split())
pricelst = []
profit = 0
profitlst = []
cnt = 0

for i in range(m) :
    pricelst.append(int(sys.stdin.readline()))

pricelst.sort(reverse=True)

for k in range(len(pricelst)) :
    price = pricelst[k]
    for j in range(len(pricelst)) :
        if price <= pricelst[j] :
            profit += price
            cnt += 1
            if cnt >= n :
                break
        else :
            continue
    profitlst.append(profit)
    profit = 0
    cnt = 0

print(pricelst[profitlst.index(max(profitlst))], end=' ')
print(max(profitlst))
