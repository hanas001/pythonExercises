# Return a list of 2-element tuples, representing
# the 2-person conversations that take place, in
# the order in which they take place.
# The length of your list will be measured to see
# if it is of the shortest possible length, i.e.
# uses the fewest number of conversations possible
# for the given value of n.

def optimal_conversations(n):
    addedNumbers = []
    connections = []
    resultingList = []
    users = dict()
    for i in range(1, n+1):
        # print(i)
        usr = "user_" + str(i)
        users[usr] = str(i)
        # for j in range(1, n+1):
        #     if i > j:
        #         connections.append(i)
        #         connections.append(j)
        #         connectionsTuple = tuple(connections)
        #         resultingList.append(connectionsTuple)
        #         connections = []
    # print(users)

    for i in range(1, len(users)+1):
        keyName = "user_" + str(i)
        for j in range(1, len(users)+1, 1):
            keyNameNext = "user_" + str(j)
            if i > j:
                if str(i) not in users[keyName] and  str(i) not in users[keyNameNext]:
                    list1 = []
                    list2 = []
                    listAll = []
                    # print(keyName)
                    # print(type(keyName))
                    # print(users[keyName], 'user i connects to ', 'user j', users[keyNameNext])
                    list1 = str(users[keyName])
                    list2 = str(users[keyNameNext])

                    listAll = list1 + list2
                    # listAll = set(listAll)
                    # print(listAll)
                    users[keyName], users[keyNameNext] = listAll, listAll

                # print(i)

        # print(users)
        # connections = i + (i+1)
        # print (connections)
    print(users)
    key = set(users['user_3'])
    print(key, 'user_3')


    return resultingList

# print(optimal_conversations(2))
# print(optimal_conversations(3))
print(optimal_conversations(4))
# print(len(optimal_conversations(4)))
#
# print(optimal_conversations(5))
# print(len(optimal_conversations(5)))