"""
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""
import re

line = "the-stealth-warrior"
# line = "The_Stealth_Warrior"
# line = "A-B-C"
# line = ""


def to_camel_case(text):
    if text:
        camelCase = []
        text_processed = re.split("[-_]", text)
        # print(text_processed)
        for i in range(len(text_processed)):
            item = text_processed[i]
            # print(item[0])
            if i > 0:
                firstLetter = list(item)[0].upper()
                # print(firstLetter)
            else:
                firstLetter = list(item)[0]

            upperLst = list(item)
            upperLst[0] = firstLetter
            upperLst = "".join(upperLst)
            # print(upperLst)
            camelCase += upperLst

        return "".join(camelCase)
    else:
        return text


print(to_camel_case(line))
