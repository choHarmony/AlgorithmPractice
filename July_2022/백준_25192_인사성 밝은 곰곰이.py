import sys

n = int(sys.stdin.readline())
cnt = 0
nameset = set()

for i in range(n) :
    chat = str(sys.stdin.readline().strip())
    while i <= n :
        if i == 0:
            break
        elif chat != 'ENTER' :
            nameset.add(chat)
            break
        elif chat == 'ENTER' :
            cnt += len(nameset)
            nameset = set()
            break
cnt += len(nameset)

print(cnt)