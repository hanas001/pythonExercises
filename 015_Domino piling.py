"""
2 4
3 3
"""

line = input().split()
dominoSquare = 2*1

fieldSquare = int(line[0])*int(line[1])
# print(fieldSquare)
numberOfDominos = fieldSquare//dominoSquare

print (numberOfDominos)
