import sys

n = int(sys.stdin.readline())
ipt = str(sys.stdin.readline().strip()).split('*')
a = len(ipt[0])
b = len(ipt[1])

for i in range(n) :
    file = str(sys.stdin.readline().strip())
    if ipt[0] == file[:a] and ipt[1] == file[-b:] and len(file) >= a+b :
        print('DA')
    else :
        print('NE')