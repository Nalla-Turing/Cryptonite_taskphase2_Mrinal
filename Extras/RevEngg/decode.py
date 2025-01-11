x =  '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
flag = ''
for i in x:
    for j in range(32,127):
        if (ord(i)-j)%256 == 0:
            flag += chr(int((ord(i) - j) / 256)) + chr(j)
            print(flag)
            print(chr(int((ord(i)-j)/256)))
            print(chr(j))
print(flag)