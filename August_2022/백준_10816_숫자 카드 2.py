import sys

n = int(sys.stdin.readline().strip())
dic = {}
ans = []
nums = [int(n) for n in sys.stdin.readline().split()]

for i in nums :
    try :
        dic[i] += 1
    except :
        dic[i] = 1

m = int(sys.stdin.readline().strip())
find = [int(m) for m in sys.stdin.readline().split()]

for i in find :
    if i in dic.keys() :
        ans.append(dic[i])
    elif i not in dic.keys() :
        ans.append(0)

print(*ans)