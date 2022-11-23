line = "the_Stealth_Warrior"

def to_camel_case(text):
    cap = False
    newText = ''
    for t in text:
        # print(t)
        if t == '_' or t == '-':
            print(t)
            cap = True
            continue
        else:
            if cap == True:
                print(t)
                t = t.upper()
            newText = newText + t
            print(newText)
            cap = False
    return newText

print(to_camel_case(line))