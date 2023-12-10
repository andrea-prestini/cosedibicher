# f = open("filetestuale.txt", "r")
# print(f.read())
# f.close()

'''
usare with con i file è più sicuro perchè si occupa autonomamente di chiuderlo nel momento in cui il codice è stato eseguito!
'''
'''
with open("filetestuale.txt", "r") as f:
    for line in f:
        print(line)
'''

with open("filetestuale.txt", "r") as f:
    print(f.read())

print("=" * 40)

with open("filetestuale.txt", "r") as f:
    for line in f:
        if "pen" in line:
            print("trovato:\n",line)
        