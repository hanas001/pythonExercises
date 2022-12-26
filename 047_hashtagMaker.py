def generate_hashtag(s):
    wordList = s.split()
    # print('wlst',wordList)
    hash = []


    length = len(s)
    if length == 0:
        return False

    for item in wordList:
        # lengthItem = len(item)
        # if lengthItem > 140:
        #     return False
        item = item.capitalize()
        hash.append(item)

    hashT = '#' + str(''.join(hash))

    if len(hashT) > 141:
        return False
    return hashT



# a = " Hello there thanks for trying my Kata"   #"#HelloThereThanksForTryingMyKata"
# a = "    Hello     World   "
# a = ""
# a = 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'
# a = 'c i n'
# a = 'PPkOjNDttAd JdDbFMeoeQ  qoKlYQUTRMl RoJUVSdUudn CEjirDZhxoo  mnoDWJSCVN rRofekFklAf iiEsuWfu he DColsSEQMtz xuHbTArNtYz RcwCLxethqK ZRYTmtOzbUi'       #False should equal '#PpkojndttadJddbfmeoeqQoklyqutrmlRojuvsduudnCejirdzhxooMnodwjscvnRrofekfklafIiesuwfuHeDcolsseqmtzXuhbtarntyzRcwclxethqkZrytmtozbui'
a = 'YNgmHvZrCB MrKNvrHSHaf wYJyTJTIIwL DOq OWXFmRr HHeXLStehrt DsmxaZcfSHn losKSSpDzxI eTEdNnLkyyc EQRvxKXqQTH zStPtSPtbhi TKbwKZlNPHl EfzZlFtG Ro xsPoeaDefo  pn  bFoSNLS ulaZvEvZWip UgJJGWQlKmZ rYgKrOzu'

print(generate_hashtag(a))
# print(generate_hashtag(b))