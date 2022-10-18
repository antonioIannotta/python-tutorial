newfile = open("test.txt", "r")

while True:
    line = newfile.readline()
    if len(line) == 0:
        break
    print(line)

newfile.close()