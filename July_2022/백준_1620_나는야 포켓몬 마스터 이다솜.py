import sys

n, m = map(int, sys.stdin.readline().split())

pokemonBook = {}
pokemonBook2 = {}

for i in range(1, n+1) :
    a = sys.stdin.readline().strip()
    pokemonBook[i] = a
    pokemonBook2[a] = i

for k in range(m) :
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit() == True :
        print(pokemonBook[int(quiz)])
    else :
        print(pokemonBook2[quiz])