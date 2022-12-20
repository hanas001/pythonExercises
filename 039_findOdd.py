def find_it(seq):
     uniqueNumbers = list(set(seq))
     uniqueCount = []
     # print('unique numbers', uniqueNumbers)
     for i in range(len(uniqueNumbers)):
          item = uniqueNumbers[i]
          # print(item)
          uniqueCount += [0]

     print('unique count numbers', uniqueCount)

     # for count, value in enumerate(seq):
     #      print(count, value)

     for number, item in enumerate(uniqueNumbers):

          count = seq.count(item)
          print('number', number, 'item', item, ' count', count)
          uniqueCount[number] = count

          if count%2 > 0:
               # print('item', item, ' count', count)
               oddCounter = item
               # return item

     print('uniques counter', uniqueCount)
     return oddCounter


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
# print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
# print(find_it([10]))
# print(find_it([5,4,3,2,1,5,4,3,2,10,10]))