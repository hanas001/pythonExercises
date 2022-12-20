def optimal_conversations(n):
    connections = []
    resultingList = []

    if n % 2 == 0:
        for i in range(1, n+1, 2):

            for j in range(2, n+1, 2):
                # print(i, 'i')
                # print(j, 'j')

                connections.append(i)
                connections.append(j)
                connectionsTuple = tuple(connections)
                resultingList.append(connectionsTuple)
                connections = []
    else:
        for i in range(1, n+1):

            for j in range(1, n+1):
                if i > j:
                    # print(i, 'i')
                    # print(j, 'j')

                    connections.append(i)
                    connections.append(j)
                    connectionsTuple = tuple(connections)
                    resultingList.append(connectionsTuple)
                    connections = []
    # print(users)


    return resultingList

print(optimal_conversations(2))
print(len(optimal_conversations(2)))

print('for three', optimal_conversations(3))
print(len(optimal_conversations(3)))

print('for four', optimal_conversations(4))
print(len(optimal_conversations(4)))

print(optimal_conversations(5))
print(len(optimal_conversations(5)))

print(optimal_conversations(6))
print(len(optimal_conversations(6)))