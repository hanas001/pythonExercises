import decimal
import math
bacterias = int(input())
# bacterias = 536870911
# bacterias = 343000816


bacteriasBowl = 0
intermediateResult = bacterias
# print("IR",intermediateResult)
counter = 1

while intermediateResult > 2:
    try:
        if intermediateResult % 2 == 0:
            intermediateResult = intermediateResult/2
            # print("irOdd", intermediateResult)
        else:
            intermediateResult = int(intermediateResult/2)
            # print("irEven", intermediateResult)
            counter += 1
    except:
        break

print(counter)