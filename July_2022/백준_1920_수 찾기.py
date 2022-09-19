import sys

n = int(sys.stdin.readline())
nums = [int(x) for x in input().split()]
nums.sort()

m = int(sys.stdin.readline())
quiz = [int(x) for x in input().split()]

start = 0
end = len(nums) - 1

for i in quiz :
    start = 0
    end = len(nums) - 1

    while start <= end :
        mid = (start + end) // 2
        if i == nums[mid] :
            print(1)
            break
        elif i > nums[mid] :
            start = mid + 1
        else :
            end = mid - 1
    else :
        print(0)