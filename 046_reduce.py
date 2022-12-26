def dirReduc(arr):

    lengthArr = len(arr)
    lengthArrOld = 0

    while lengthArr != lengthArrOld:
        lengthArrOld = lengthArr

        for index in range(len(arr) - 1):
            # print(index)
            one = arr[index]
            two = arr[index+1]

            if one == 'NORTH' and two == 'SOUTH':
                arr[index] = 0
                arr[index+1] = 0
                # print(arr)
            elif one == 'SOUTH' and two == 'NORTH':
                arr[index] = 0
                arr[index + 1] = 0
                # print(arr)
            elif one == 'EAST' and two == 'WEST':
                arr[index] = 0
                arr[index + 1] = 0
                # print(arr)
            elif one == 'WEST' and two == 'EAST':
                arr[index] = 0
                arr[index + 1] = 0
                # print(arr)

        while 0 in arr:
            arr.remove(0)
        # print('arr', arr)


        lengthArr = len(arr)

        # print('ln arr old', lengthArrOld)
        # print('ln arr', lengthArr)

    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
b = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))
print(dirReduc(b))