with open('wayTooLongWords.txt') as file:
    lines = file.readlines()
word = input()

for word in lines:
    word = word.strip()
    if len(word) >= 10:
        # print(word)
        compressedWord = word[0]+str(len(word)-2)+word[-1]
        print(compressedWord)
    else:
        print(word)