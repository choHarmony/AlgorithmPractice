t = int(input())

for i in range(t):
    k = int(input())  # 층
    n = int(input())  # 호

    past = []
    present = []
    floor = 0
    tmp = False

    while True :
        for j in range(1, n+1):
            if not tmp:
                past.append(j)
            present.append(sum(past[:j]))
        if floor == k :
            break
        else :
            floor += 1
            past = present
            present = []
            tmp = True

    print(past[-1])