"""
3
1 1 0
1 1 1
1 0 0
"""
scores = []
while True:
    try:
        line = input()
    except EOFError:
        break
    scores.append(line)

cycles = int(scores[0])
# print(scores)
line = 0
numberOfSolutions = 0

for i in range(cycles + 1):
    if i > 0:
        str = scores[i].replace(" ","")
        # print(str)
        decision = 0
        line += 1
        for j in str:
            # print(j)
            decision += int(j)
        # print(decision)
        if decision >= 2:
            numberOfSolutions += 1

print(numberOfSolutions)