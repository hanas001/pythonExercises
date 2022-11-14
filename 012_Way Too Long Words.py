"""
9
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
contents
abcdefghij
indentation
tried
select
lines
DELETE
"""

# print("Enter/Paste your content")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

# print("printed contents",contents)

cycles = int(contents[0])

for i in range(cycles+1):
    # print(i)
    if i > 0:
        # print(contents[i])
        if len(contents[i]) > 10:
            compressedWord = contents[i][0] + str(len(contents[i]) - 2) + contents[i][-1]
            print(compressedWord)
        else:
            print(contents[i])
