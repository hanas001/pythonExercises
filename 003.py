file = open('someText.txt', 'w')

file.write('Hi ')
file.write('there')

file.close()

# f = open('someText.txt')
# text = f.read()
# print(text)

for line in open('someText.txt'): print(line)

help(file.seek)