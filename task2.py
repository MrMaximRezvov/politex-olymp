cryptname = "HTIJ"

#Шифрование сдвигом вправо

for i in range(1, 27):
    name = ''
    # if i == 8:
        # continue
    for j in range(len(cryptname)):
        name += chr(int(ord(cryptname[j])) - i)
    print(i, ' = ', name)