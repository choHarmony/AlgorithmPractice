import sys

n = int(sys.stdin.readline())
members = []

for i in range(n) :
    member = sys.stdin.readline().strip()
    age = int(member.split(' ')[0])
    name = member.split(' ')[1]
    members.append((age, name))

members.sort(key = lambda x : (x[0]))

for i in members :
    print(*i)