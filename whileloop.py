import sys
def whileloop():
    """While Loop Practice"""
    x = 9
    y = 1
    print('While Loop Demo Printing from {0} to {1}'.format(x,y))
    while x >= y:
        print(x)
        x -= 1

def whileloopasc():
    """While loop ascending Order"""
    x = 9
    y = 1
    print('While Loop Demo Printing from {0} to {1}'.format(y, x))
    while y <= x:
        print(y)
        y += 1

#
# whileloop()
# whileloopasc()

if __name__ == '__main__':
    print('While Loop Print Ascending or Descending..')
    print('To Print Ascending Order, Type A , for Descending Type D')
    # print(str(sys.argv[1]))
    order = input()
    if order == 'D':
        whileloop()
    elif order == 'A':
        whileloopasc()
    else:
        print("Order entered is Invalid...enter A or D for ordering")









