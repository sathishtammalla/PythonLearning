exer1 = '1. Write Python program to print “Washington”, then find out it’s length and print it.'
exer2 = '2. Write Python program that asks for first name and last name separately, then print the full name.'
exer3 = '3. Write Python program that takes “washinton” and print “Washington” (convet the first charcter to upper case).'
exer4 = '4. Write Python program that takes “I am living in Washintgon” and find “living” in the string using String find function.'
exer5 = '5. Write Python program that takes “I am living in Washintgon” and find first occurrence of the letter "m" in the string using String index function'
exer6 = '6. Write Python program that takes “I am living in Washintgon” and replace “living” with “not living” in the string using String replace function.'
exer7 = '7. Write Python program that takes “123456” and print True if all the characters in the text are numeric using string isnumeric function.'
exer8 = '8. Write Python program that takes “One day I buy one Tesla car” and print the number of times the value "one" appears in the string using string count function.'
exer9 = '9. Write Python program that takes “zerorez” and revese the string, and then compres with the original and print True if they both are same.'
exer10 = '10. Write Python program that takes “I am living in Washintgon” and check if the string starts with “I” using string startswith function'


def print_line(length):
    line = ''
    for i in range(length):
        line += '-'
    return line


def e1():
    print(print_line(len(exer1)))
    print(exer1)
    city = 'Washington'
    print('Name of the city: {}'.format(city))
    print('Length of the city {0}  is {1}'.format(city, len(city)))


def e2():
    print(print_line(len(exer2)))
    print(exer2)
    print('Enter First Name')
    fname = input()
    print('Enter Last Name')
    lname = input()
    print(f'The Full Name is : {fname.capitalize()} {lname.capitalize()}')


def e3():
    print(print_line(len(exer3)))
    print(exer3)
    city = 'Washington'
    print('Name of the city: {}'.format(city))
    print('Name of the city with Capitalized : {0}'.format(city.capitalize()))


def e4():
    print(print_line(len(exer4)))
    print(exer4)
    text = 'I am living in Snoqualmie, Washington'
    print('Finding "living" in text  : {}'.format(text))
    sub = 'living'
    found = text.find(sub)
    if found >= 0:
        print('Text "{}" found in the sentence "{}"'.format(sub, text))
    else:
        print('Text "{}" not found in the sentence "{}" '.format(sub, text))


def e5():
    print(print_line(len(exer5)))
    print(exer5)
    text = 'I am living in Snoqualmie, Washington'
    print('Finding "n" index position in text  : {}'.format(text))
    sub = 'n'

    try:
        found = text.index(sub)
    except:
        found = -1

    print(f'Index position of "{sub}" is at {found}')


def e6():
    print(print_line(len(exer6)))
    print(exer6)
    text = 'I am living in Snoqualmie, Washington'
    print('Replacing "Snoqualmie" with "Bellevue" in text :  {}'.format(text))
    sub = 'Snoqualmie'
    text = text.replace(sub, 'Bellevue')

    print(f'After replacing --> {text}')


def e7():
    print(print_line(len(exer7)))
    print(exer7)
    num = '12345A'
    num1 = '12345'
    print(f'Checking if {num} has all numbers using is numeric. Result -> {num.isnumeric()}')
    print(f'Checking if {num1} has all numbers using is numeric. Result -> {num1.isnumeric()}')


def e8():
    print(print_line(len(exer8)))
    print(exer8)
    text = 'One day I will buy one Tesla car'
    word = 'one'
    print(f'Count how many times "{word}" is found in text {text}')
    print(f'Count of "{word}" in text "{text}" is : {text.lower().count("one")}')


def e9():
    print(print_line(len(exer9)))
    print(exer9)
    text = 'zerorez'
    print(f'Text to be reversed "{text}"')
    rev = text[::-1]
    print(f'Reversed text is "{rev}"')
    print(f'Compare and print result if both "{text}" and "{rev}" are same  Result --> {text == rev} ')


def e10():
    print(print_line(len(exer10)))
    print(exer10)
    text = 'I live in Snoqualmie'
    print(f'Check if the text "{text}" starts with letter "I", the Result is --> {text.startswith("I")}')


ex_list = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]


def exercises(choice):
    if choice == 0:
        for i in ex_list:
            i()
    else:
        ex_list[int(choice) - 1]()


def strings_demo():
    print('String Exercises...')
    print('Enter a number to run specific exercise, 0 to run all or q to quit')
    exer = {}

    exer['1'] = 'Write Python program to print “Washington”, then find out it’s length and print it.'
    exer['2'] = 'Write Python program that asks for first name and last name separately, then print the full name.'
    exer[
        '3'] = ' Write Python program that takes “washinton” and print “Washington” (convet the first charcter to upper case.)'
    exer[
        '4'] = 'Write Python program that takes “I am living in Washintgon” and find “living” in the string using String find function.'
    exer[
        '5'] = 'Write Python program that takes “I am living in Washintgon” and find first occurrence of the letter "m" in the string using String index function'
    exer[
        '6'] = 'Write Python program that takes “I am living in Washintgon” and replace “living” with “not living” in the string using String replace function.'
    exer[
        '7'] = 'Write Python program that takes “123456” and print True if all the characters in the text are numeric using string isnumeric function.'
    exer[
        '8'] = 'Write Python program that takes “One day I buy one Tesla car” and print the number of times the value "one" appears in the string using string count function.'
    exer[
        '9'] = 'Write Python program that takes “zerorez” and revese the string, and then compres with the original and print True if they both are same.'
    exer[
        '10'] = 'Write Python program that takes “I am living in Washintgon” and check if the string starts with “I” using string startswith function'

    # print(type(exer))

    while True:
        print(print_line(len(exer1)))
        for key, value in exer.items():
            print(f'{key} : {value}')
        print('Enter your choice....')
        entry = input()
        if entry.lower() == 'q':
            print('Exiting the Strings Exercises Demo')
            exit()
        elif entry == '0':
            print('Running All exercises.....')
            exercises(int(entry))
        else:
            if entry.isnumeric():
                print('Checking if the entry is in the range...')
                if entry in exer:
                    print(f'Entry found...executing the exercise {entry}')
                    exercises(entry)
                else:
                    print('Invalid Entry')


strings_demo()
