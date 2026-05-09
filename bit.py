binli = []

num = 81

while num > 0:
    binli.append(num & 1)
    num >>= 1

binli.reverse()

print(binli)