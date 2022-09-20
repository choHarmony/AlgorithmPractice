n = int(input())

def fibonacci(n) :
    lst = [0] * n
    lst[0], lst[1] = 1, 1
    dycnt = 0
    for i in range(2, n) :
        dycnt += 1
        lst[i] = lst[i-1] + lst[i-2]
    return lst[-1], dycnt

print(*fibonacci(n))