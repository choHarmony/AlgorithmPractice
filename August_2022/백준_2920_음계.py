music = input().strip().split(' ')
music = list(map(int, music))

if sorted(music) == music :
    print('ascending')
elif sorted(music, reverse=True) == music :
    print('descending')
else:
    print('mixed')