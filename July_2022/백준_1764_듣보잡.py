import sys

n, m = map(int, sys.stdin.readline().split())

hear = [str(sys.stdin.readline().strip()) for _ in range(n)]
see = [str(sys.stdin.readline().strip()) for _ in range(m)]

hearsee = hear + see
cnt = {}
count = 0
lst = []

for i in hearsee :
    try :
        cnt[i] += 1
    except :
        cnt[i] = 1

for key, value in cnt.items() :
    if value == 2 :
        count += 1
        lst.append(key)

lst.sort()
print(count)
print(*lst, sep='\n')