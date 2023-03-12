import heapq, sys

n = int(input())
heap = []

for i in range(n) :
    x = int(sys.stdin.readline())
    if len(heap) == 0 and x == 0 :
        print(0)
    elif x == 0 :
        print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap, (abs(x), x))