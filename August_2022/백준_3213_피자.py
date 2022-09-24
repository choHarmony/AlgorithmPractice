import sys
from math import ceil

n = int(sys.stdin.readline())
pizza = {'1/2' : 0, '1/4' : 0, '3/4' : 0}
pizza_num = 0

for i in range(n) :
    a = sys.stdin.readline().strip()
    if a == '1/2' :
        pizza['1/2'] += 1
    elif a == '1/4' :
        pizza['1/4'] += 1
    elif a == '3/4' :
        pizza['3/4'] += 1

if pizza['1/4'] > pizza['3/4'] :
    pizza_num += pizza['3/4']
    pizza['1/4'] -= pizza['3/4']
    pizza_num += ceil((0.5 * pizza['1/2']) + (0.25 * pizza['1/4']))
elif pizza['1/4'] == pizza['3/4'] :
    pizza_num += pizza['3/4']
    pizza['1/4'] = 0
    pizza['3/4'] = 0
    pizza_num += ceil(pizza['1/2'] / 2)
else :
    pizza_num += pizza['1/4']
    pizza['3/4'] -= pizza['1/4']
    pizza['1/4'] = 0

    if pizza['1/2'] % 2 == 1 :
        pizza_num += (pizza['1/2'] - 1) // 2
        pizza_num += pizza['3/4'] + 1
    elif pizza['1/2'] == 1 :
        pizza_num += 1 + pizza['3/4']
    else :
        pizza_num += pizza['1/2'] // 2
        pizza_num += pizza['3/4']

print(pizza_num)