n = int(input())
lst = [int(n) for n in input().split()]
time = 0

for k in range(len(lst)+1) :
    time += sum(sorted(lst)[:k])

print(time)