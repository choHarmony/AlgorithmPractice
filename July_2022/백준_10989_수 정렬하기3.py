import sys

n = int(sys.stdin.readline())

count = [0] * 10001

for i in range(n) :
    count[int(sys.stdin.readline())] += 1

for k in range(10001) :
    if count[k] != 0 :
        for j in range(count[k]) :
            print(k)