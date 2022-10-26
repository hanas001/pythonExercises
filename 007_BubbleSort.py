randomNumbers = [5, 53, 133, 85, 1001, 90, 1, 100, 4, 2, 14, 22, 997, 4, 200]

l = len(randomNumbers)
for i in range(l - 1):
       for j in range(0, l - i - 1):
              if randomNumbers[j]>randomNumbers[j+1]:
                     flag = True
                     randomNumbers[j], randomNumbers[j+1]=randomNumbers[j+1], randomNumbers[j]


print(randomNumbers)

