directA = "abcdefg"
reversedA = ""

for i in range(len(directA)+1):
    if i > 0:
        reversedA += directA[-i]

print(reversedA)
