filename = input("Inserisci il nome di un file: ")
try:
    opened_file = open(filename, "r")
    lines = opened_file.readlines()
    for cnt in range(len(lines)):
        print(lines[cnt])
except:
    print("There is no file with name: " + filename)

