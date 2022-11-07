import sys

k, l = map(int, sys.stdin.readline().split())
lst = []
dic = {}
success = []

for i in range(l) :
    student = str(sys.stdin.readline().strip())
    lst.append(student)
    try :
        dic[student] += 1
    except :
        dic[student] = 1

for j in lst :
    if dic[j] == 1 :
        success.append(j)
    elif dic[j] >= 2 :
        dic[j] -= 1

if k <= len(success) :
    for m in range(k) :
        print(success[m], end='\n')
else :
    for n in range(len(success)) :
        print(success[n], end='\n')