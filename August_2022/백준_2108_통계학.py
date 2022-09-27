import sys

n = int(sys.stdin.readline())
lst = []
dic = {}

for i in range(n) :
    a = int(sys.stdin.readline())
    lst.append(a)
    try :
        dic[a] += 1
    except :
        dic[a] = 1
lst.sort()

print(round(sum(lst) / len(lst))) # 산술평균

if len(lst) % 2 == 0 : # 중앙값
    print((lst[len(lst)//2] + lst[len(lst)//2+1])/2)
else :
    print(lst[(len(lst)-1)//2])

freq = [j for j, k in dic.items() if max(dic.values()) == k] # 최빈값
if len(freq) == 1 :
    print(freq[0])
else :
    freq.remove(min(freq))
    print(min(freq))

print(lst[-1]-lst[0]) # 범위