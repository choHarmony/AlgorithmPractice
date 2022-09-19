import sys

n = int(input())

for _ in range(n) :
    s = list(sys.stdin.readline().strip())
    i, j = 0, 1
    for idx in range(1, len(s)) :
        if s[idx] > s[idx-1] :
            if i < idx :
                i = idx
    for idx in range(1, len(s)) :
        if s[idx] > s[i-1] :
            if j < idx :
                j = idx

    if i != 0 and j != 0 :
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = list(reversed(s[i:]))

    print(''.join(s))