import sys

a, b, c = map(int, sys.stdin.readline().split()) # 일반, 특별, 서비스
ord_cost = 0
spe_cost = 0
cnt = 0

ordinary = [str(sys.stdin.readline().strip()) for _ in range(a)]
ord_dic = {}
for i in ordinary :
    ord_dic[i.split()[0]] = int(i.split()[1])

special = [str(sys.stdin.readline().strip()) for _ in range(b)]
spe_dic = {}
for k in special :
    spe_dic[k.split()[0]] = int(k.split()[1])

service = [str(sys.stdin.readline().strip()) for _ in range(c)]

n = int(sys.stdin.readline()) # 메뉴 주문 개수

menu = [str(sys.stdin.readline().strip()) for _ in range(n)]
for j in menu :
    if j in ord_dic.keys() :
        ord_cost += ord_dic[j]
        cnt += 1

    else :
        if j in spe_dic.keys() :
            spe_cost += spe_dic[j]
            cnt += 1

if ord_cost >= 20000 and ord_cost + spe_cost >= 50000 and n-cnt == 1 :
    print('Okay')
elif ord_cost >= 20000 and ord_cost + spe_cost >= 50000 and n-cnt == 0 :
    print('Okay')
elif ord_cost >= 20000 and ord_cost + spe_cost < 50000 and n-cnt == 0 :
    print('Okay')
elif ord_cost > 0 and spe_cost == 0 and n-cnt == 0 :
    print('Okay')
else :
    print('No')