import sys

k, n = map(int, sys.stdin.readline().split())
lst = []

for i in range(k) :
    sik = int(sys.stdin.readline().strip())
    lst.append(sik)

start = 1
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    line = 0
    line2 = 0
    for j in lst :
        line += j // mid
        line2 += j // (mid+1)

    if line >= n and line2 >= n :
        start = mid + 1
    elif line >= n and line2 < n :
        print(mid)
        break
    else :
        end = mid - 1