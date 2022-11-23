"""
3
2014 2016 2015

1
2050
"""

line = []

while True:
    try:
        l = input()
    except EOFError:
        break
    line.append(l)

groups = line[0]
line.pop(0)

numbers = line[0].split()

sum = 0
for i in range(int(groups)):
    digit = int(numbers[i])
    sum += digit

graduationYear = sum//int(groups)
print(graduationYear)