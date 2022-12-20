def minIndex(list):
    minSum = 0
    sumList = []

    for k in range(len(list)):
        customers = list[k]
        sum = 0
        for i in customers:
            sum += i
        sumList.append(sum)
    min = sumList[0]
    index = 0

    for j in range(len(sumList)):
        item = sumList[j]
        if item < min:
                min = item
                index = j
    return index

# a = [[2,3,3], [10,20,4], [12,13,3], [1,2,1], []]
# a = [[10], []]
# print('index of minimum sum is', sum(a))

def queue_time(customers, n):

    cashiers = []
    for i in range(n):
        name = []
        cashiers.append(name)
    # print('cashiers',cashiers)

    # print('customers', customers)

    while customers:
        for i in range(len(customers)):
            index = minIndex(cashiers)
            # print('min Sum index', index)

            # print('customer zero', customers[0])
            cashiers[index].append(customers[0])
            # print('customers in cashiers queue', cashiers)

            # print('customers', customers)
            customers.pop(0)

    cashiersSum = 0
    for k in range(len(cashiers)):
        # print('k', cashiers[k])
        customers  = cashiers[k]
        # print('customers', customers)

        sum = 0
        for l in customers:
            sum += l

        # print('sum is', sum)
        if sum > cashiersSum:
            cashiersSum = sum


    return cashiersSum


# print(queue_time([5,3,4], 1))
# print(queue_time([2,2,3,3,4,4], 2))
# print(queue_time([10,2,3,3], 2))
# print(queue_time([2,3,10], 2))
# print(queue_time([1,2,3,4,5], 100))
# print(queue_time([1,2,3,4,5], 1))
# print(queue_time([2], 5))
print(queue_time([], 1))