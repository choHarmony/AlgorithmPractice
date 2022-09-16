n = int(input())
nums = [int(n) for n in input().split()]
cnt = 0 # 소수 아닌 수 카운트

for i in nums :
    if i == 1 :
        cnt += 1
    for j in range(2, i) :
        if i % j == 0 :
            cnt += 1
            break

print(len(nums) - cnt)