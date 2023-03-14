import sys, itertools

while True :
    ipt = sys.stdin.readline().strip()
    if ipt == '0' :
        break
    nums = list(map(int, ipt.split(' ')))[1:]

    case = list(itertools.combinations(nums, 6))
    for i in case :
        i = list(i)
        print(*i, end='\n')
    print()