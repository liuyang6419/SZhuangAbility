import os

path = 'ca/'

f = os.listdir(path)
print(f)
n = 0
for i in f:
    oldname = path + f[n]
    newname = path + 'a' + str(n + 1) + '.jpg'
    print(oldname)
    os.rename(oldname, newname)
    print(oldname, " - > ", newname)
    n += 1
