"""
6
1 1 1
2 2 3
3 3 2
5 10 2
11 13 1
1 4 4
"""

table = []

while True:
    try:
        l = input()
    except EOFError:
        break
    table.append(l)

tries = int(table[0])
table.pop(0)

# print(tries)
# print(table)

for i in range(tries):
    # print(i)
    # print(table[i])
    raws = table[i].split()
    # print(raws)

    friends = int(raws[-1])
    width = int(raws[0])
    height = int(raws[1])
    # print(width)
    # print(width, height, friends)
    # print(type(width))
    counter = 0

    resultW = width
    resultH = height

    if resultH % 2 == 0:
        resultH, resultW = resultW, resultH
        while resultW % 2 == 0:
            try:
                counter += 2
                resultW = resultW/2
                resultH = resultH

                while resultH % 2 == 0:
                    try:
                        counter += 2
                        resultH = resultH / 2
                        resultW = res
                    except:
                        break
            except:
                break
    else:
        counter = 1


    # print("counter",counter)
    if counter >= friends:
        print("YES")
    else:
        print("NO")