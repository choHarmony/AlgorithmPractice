keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try :
        line = input()
        new_line = ''

        for i in line :
            if i == ' ' :
                new_line += ' '
                continue
            else :
                i_idx = keyboard.index(i)
                new_line += keyboard[i_idx-1]

        print(new_line)
    except :
        break