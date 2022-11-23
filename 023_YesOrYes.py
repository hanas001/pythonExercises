"""
11
EYS
YES
yES
yes
Yes
YeS
Noo
orZ
yEz
Yas
XES
"""

answers = []

while True:
    try:
        l = input()
    except EOFError:
        break
    answers.append(l)

tries = int(answers[0])
answers.pop(0)

# print(answers)
# print(tries)

for i in range(tries):
    # print(answers[i].upper())
    if answers[i].upper() == 'YES':
        # print(i)
        print("YES")
    else:
        # print(i)
        print("NO")