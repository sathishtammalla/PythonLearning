def stringlist():
    """String List Demo"""
    cities = ['Seattle', 'LA', 'San Diego', 'NY']
    print("Entries in my list {}".format(cities))
    print("Printing only NY from the list")
    for c in cities:
        if c == 'NY':
            print(c)

    print('Changing the LA to Boston')

    # Using Enumerate
    for index, city in enumerate(cities):
        if city == 'LA':
            print('City Name LA found Changing it to Boston')
            print(city)
            cities[index] = 'Boston'

    print("Entries in my list after the change {}".format(cities))

    print('Using List Comprehension')
    # Using List comprehension  creating a full slice of list to avoid creating another
    # object by just assigning to the same cities list variable
    cities[:] = ['Redmond' if city == 'Boston' else city for city in cities]
    print(cities)

    print('Length of my cities list {}'.format(len(cities)))

    print('Adding more cities, Portland, Hyd, Delhi, Mumbai and SFO')
    cities.extend(['Portland', 'Hyd', 'Delhi', 'Mumbai', 'SFO'])

    print("Entries in my list after the change {}".format(cities))

    print('Length of my cities list {}'.format(len(cities)))


stringlist()
