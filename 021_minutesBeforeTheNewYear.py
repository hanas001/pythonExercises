"""
5
23 55
23 0
0 1
4 20
"""
table = []

while True:
    try:
        l = input()
    except EOFError:
        break
    table.append(l)

cycles = int(table[0])
table.remove(table[0])

while cycles:
    try:
        time = table[0].split()
        table.pop(0)
        # print("time", time)
        minutes = int(time[0])*60 + int(time[-1])
        # print("minutes", minutes)
        cycles -= 1
        remainedMinutes = 24*60 - minutes
        print("Minutes left to New Year", remainedMinutes, "minutes")
    except:
        break
