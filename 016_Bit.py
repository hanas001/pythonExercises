"""
2
X++
--X
"""
line = []
while True:
    try:
        l = input()
    except EOFError:
        break
    line.append(l)

# print("Line", line)
score = 0
x=0
for i in range(1, int(line[0])+1):
    # print(i)
    for j in line[i]:
        # print(j)
        if j == "+":
            score += 1
        elif j == "-":
            score -= 1
        else:
            pass
print(score//2)