def conditions():
    """IF Condition Check Program"""
    print('IF Conditions Check Program')
    print('Enter a Number for X')
    x = input()
    print("Entered X Value :{0}".format(x))
    print('Enter a Number for Y')
    y = input()
    print("Entered Y Value :{0}".format(y))
    if x < y:
        print('X is less than Y')
    elif x > y:
        print('X is greater than Y')
    else:
        print('X and Y are Equal')


conditions()



