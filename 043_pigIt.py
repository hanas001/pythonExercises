def pig_it(text):
    textList = list(text.split())
    lineAltered = []
    for i in textList:
        if i.isalpha():
            firstLetter = i[0]
            line = i[1:] + firstLetter + 'ay'
            lineAltered.append(line)
        else:
            lineAltered.append(i)

    return (' '.join(lineAltered))

# print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !