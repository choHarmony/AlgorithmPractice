import sys

n, p = map(int, sys.stdin.readline().split())
w, l, g = map(int, sys.stdin.readline().split())
hacklst = []
hacknamelst = []
score = 0

for i in range(p) :
    hack_player = sys.stdin.readline().strip()
    hacklst.append(hack_player)
    hacknamelst.append(hack_player[:-2])

for j in range(n) :
    player = sys.stdin.readline().strip()
    if player not in hacknamelst :
        score -= l
        if score < 0:
            score = 0
    else :
        for k in hacklst :
            if player == k[:-2] and k[-1] == 'W' :
                score += w
                if score >= g:
                    print("I AM NOT IRONMAN!!")
                    quit()
            elif player == k[:-2] and k[-1] == 'L' :
                score -= l
                if score < 0 :
                    score = 0

print("I AM IRONMAN!!")