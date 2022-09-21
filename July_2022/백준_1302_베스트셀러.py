import sys

n = int(sys.stdin.readline())
d = {}
lst = []

for i in range(n) :
    book = sys.stdin.readline().strip()

    try :
        d[book] += 1
    except :
        d[book] = 1

max_value = max(d.values())

for key, value in d.items() :
    if value == max_value :
        lst.append(key)

lst.sort()
print(lst[0])