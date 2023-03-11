import sys

n, m = map(int, sys.stdin.readline().split())
tree = sys.stdin.readline().strip().split(' ')
tree = list(map(int, tree))
cut = 0

start = 0
end = max(tree)

while start <= end :
    mid = (start + end) // 2
    cut = 0
    for i in tree :
        if i-mid >= 0 :
            cut += i-mid
            if cut >= m :
                start = mid + 1
                break
    else :
        end = mid - 1
print(end)