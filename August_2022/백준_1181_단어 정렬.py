import sys

n = int(sys.stdin.readline())
wordset = set()
dic = {}
lenlst = []
lst2 = []
ans = []

for i in range(n) :
    word = sys.stdin.readline().strip()
    wordset.add(word) # 중복 단어 거르기

for j in wordset :
    dic[j] = len(j) # 단어 key, 단어 길이 value

wordlst = sorted(dic, key=lambda x:dic[x]) # 단어 길이대로만 정렬한 리스트. 사전순은 반영 안됨
for value in dic.values() :
    lenlst.append(value)
lenlst = sorted(list(set(lenlst)))

for i in wordlst :
    if len(i) == lenlst[0] :
        lst2.append(i)
    else :
        lst2.sort()
        for k in lst2 :
            ans.append(k)
        lst2 = [i]
        del lenlst[0]
lst2.sort()

for j in lst2 :
    ans.append(j)

print(*ans, sep='\n')