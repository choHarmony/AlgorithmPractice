import sys

dic = {}
cnt = 0

while True :
    name = sys.stdin.readline().strip()
    if not name :
        break
    else :
        try :
            dic[name] += 1
            cnt += 1
        except :
            dic[name] = 1
            cnt += 1

dic = sorted(dic.items())

for key, value in dic :
    print('%s %.4f' %(key, value / cnt * 100))