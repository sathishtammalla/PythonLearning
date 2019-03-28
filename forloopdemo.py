def forloopall():
    num = [1, 2, 3, 4, 5]
    print('Numbers in the list :{}'.format(str(num)))
    print('Printing all numbers using For loop')
    for i in range(len(num)):
        print(num[i])


def forloopcond():
    num = [1, 2, 3, 4, 5]
    print('Numbers in the list :{}'.format(str(num)))
    print('Printing all numbers except anything greater than 4')
    for i in range(len(num)):
        if (num[i]) < 4:
            print(num[i])


def forloopexcept():
    num = [1, 2, 3, 4, 5]
    print('Numbers in the list :{}'.format(str(num)))
    print('Printing all numbers except  4')
    for i in range(len(num)):
        if (num[i]) != 4:
            print(num[i])


forloopexcept()

forloopcond()

forloopall()
