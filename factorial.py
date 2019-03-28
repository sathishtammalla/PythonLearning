5# Regular Factorial Function
def factorial(n):
    num = n
    fact = 1
    if n > 900:
        print('Number is too big..Enter a number less than 900')
        n = 1
    while num > 1:
        fact = fact * num
        num = num - 1
        #print(fact)
    print('Factorial of  ' + str(n)  + ' is   ' + str(fact))

# Recursive Factorial Function 
def rec_fact(n):
    return 1  if(n <=1) else (n * rec_fact(n-1))

def check_if_number(n):
    try:
        n = int(n)
        rn = 'Y'
        return rn
    except:
        rn = 'N'
        return rn

# Global Infinite Loop....
print('This is a Factorial Program....'+'\n')
while True:
    print('Enter a number between 1 and 900 to find a factorial or press x to exit')
    entry = input()
    if entry == 'x'  or entry =='X':
        print('Thanks for using Factorial Program.! Hope you found it useful!')
        break
    #else if
    else:
        if check_if_number(entry) == 'Y':
            #factorial(int(entry))
            if int(entry) > 900:
                print('Number is too big..Enter a number less than 900')
            else:
                print('Factorial of '+ entry +' is ' + str(rec_fact(int(entry))))
        else:
            print("This is not a Valid number..please enter a Positive number")
