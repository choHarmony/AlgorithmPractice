n, m, b = map(int, input().split())
land = sum([list(map(int, input().split())) for _ in range(n)], [])
time = 0
dic = {}

for k in range(min(land), 257) :
    if sum(land)+b < n*m*k:
        continue
    else :
        for i in land :
            if i >= k :
                time += (i-k) * 2
            else :
                time += k-i
        dic[time] = k
        time = 0

print(min(dic.keys()), dic[min(dic.keys())])