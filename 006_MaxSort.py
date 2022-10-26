randomNumbers = [5, 53, 133, 85, 1001, 90, 1, 100, 4, 2, 14, 22, 997, 4, 200]
max = 0
# min = 0
randomNumbersSorted = []

while len(randomNumbers) > 0:

       for i in range(len(randomNumbers) - 1):
              if randomNumbers[i] > max:
                     max = randomNumbers[i]
                     positionMax = i
              else:
                     pass
                     # min = randomNumbers[i]
                     # positionMin = i

       randomNumbers.pop(positionMax)
       # randomNumbers.pop(positionMin)
       randomNumbersSorted.insert(0, max)
       # randomNumbersSorted.insert(-1, min)
       max = 0
       positionMax = 0
       # min = 0
       # positionMin = 0

       print(randomNumbers)
       print(randomNumbersSorted)
