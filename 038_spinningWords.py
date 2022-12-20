def spin_words(sentence):
    sentList = list(sentence.split())
    for i in range(len(sentList)):
        item = sentList[i]
        if len(item) > 4:
            # print('word is 5 letters or more', i )
            rev = item[:: -1]
            sentList[i] = rev

            # print('reversed word', rev)

    # print(sentList)
    sentence = ' '.join(sentList)
    # print(sentence)

    return sentence

print(spin_words("This sentence is a sentence"))
print(spin_words("Hey fellow warriors"))