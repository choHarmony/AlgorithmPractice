n = input()
lst = []

for i in n :
    lst.append(i)

lst.sort(reverse=True)
lst2 = ''.join(lst)
print(lst2)