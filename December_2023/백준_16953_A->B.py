nums = list(map(int, input().split(" ")))
a = nums[0] # 시작 숫자
b = nums[1] # 목표 숫자
cnt = 0

while b != a :
    if b < a :
        print(-1)
        break
    else :
        if str(b)[-1] == "1":
            b = int(str(b)[:-1])
            cnt += 1
        elif int(b) % 2 == 0:
            b //= 2
            cnt += 1
        else:
            print(-1)
            break
else :
    print(cnt+1)