from collections import Counter

colls = ['Write a Python program that takes mylist = ["WA", "CA", "NY"] and add “IL” to the list.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print the list.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print position/Index of CA in the list using list index function.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print position/index of each item in the list using list index function.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and sort the list using list sort function.',
         'Write a Python program that takes mylist = ["Seattle", "Bellevue", "Redmond", “Issaquah”] and print it using for loop.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print it respective state names (Ex: WA is Washington] for each item in the list.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times WA appeared in the list.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times WA and CA appeared in the list.',
         'Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times each state appeared in the list.',
         'Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print sum of all the items in the list.',
         'Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print large number from the list.',
         'Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print middle number from the list.',
         'Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”] and print the string that appeared more than once.',
         'Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”] and remove duplicates from the list.',
         'Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”, “POR”, “KEN”, “NJC”] and remove all even items in the list.',
         'Write a Python program that takes mylist = [“CALIFORNIA”, “SEATTLE”, “PIT”] and print number of characters in each item in the list.',
         'Write a Python program that takes list1 = [“WA”, “CA”] and list2 = [“Washinton”, “California] and create a list3 = [“WA”, “Washington”, “CA”, “California”].',
         'Write a Python program that takes mylist = [6, 2, 7, 3, 4, 5] and sort the list ascending without using sort function.',
         'Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print second largest number from the list.',
         'Write a Python program that takes mytuple = ("WA", "CA", "NY") and print the tuple using for loop',
         'Write a Python program that takes mytuple = ("WA", "CA", "NY") and print first item using index.',
         'Write a Python program that takes mytuple = ("WA", "CA", "NY") and change first item = “NJ” and print.',
         'Write a Python program that takes mytuple = ("WA", "CA", "NY") and check if “CA” exists and print.',
         'Write a Python program that takes mytuple = ("WA", "CA", "NY") and print length of the tuple.'
         ]

# print(colls)

print(colls[0])
mylist = ['WA', 'CA', 'NY']
print(f'Items in list : {mylist}')
print("Adding 'IL' to the list")
mylist.append('IL')
print(f'Items in list after adding : {mylist}')

print(colls[1])
print(f'Current Items in mylist  : {mylist}')

print(colls[2])
print(f'Index position of "CA" is  : {mylist.index("CA")}')

print(colls[3])
for index, value in enumerate(mylist):
    print(f'Index : {index} Value : {value}')

print(colls[4])
mylist = ['WA', 'CA', 'NY', 'IL', 'WA', 'CA', 'WA']
print(f'My list is before sorting {mylist}')
mylist.sort()
print(f'The Sorted list is : {mylist}')

print(colls[5])
cities = ["Seattle", "Bellevue", "Redmond", "Issaquah"]
print(f'Cities in the list {cities}')
print('Looping and printing each city')
for c in cities:
    print(c)

print(colls[6])
states = ['WA', 'CA', 'NY', 'IL']
st_name = ['Washington', 'California', 'New York', 'Illinois']
print(f'Printing full names of the STATES {states}')
for index, value in zip(states, st_name):
    print(f'{index} - {value}')

print(colls[7])
states = ['WA', 'CA', 'NY', 'IL', 'WA', 'CA', 'WA']
print(f'States in the list {states}')
print(f'Count of "WA" in the list {states.count("WA")}')

print(colls[8])
states = ['WA', 'CA', 'NY', 'IL', 'WA', 'CA', 'WA']
print(f'States in the list {states}')
print(f'Count of "WA" and "CA" in the list {states.count("WA")} and {states.count("CA")}')

print(colls[9])
states = ['WA', 'CA', 'NY', 'IL', 'WA', 'CA', 'WA']
print(f'States in the list {states}')
print(f'Count of each element in the list  {Counter(states)}')
for key, value in dict(Counter(states)).items():
    print(f'State :{key} Count : {value}')

print(colls[10])
l = [1, 2, 3, 4, 5]
print(f'Items in the list {l}')
print(f'Printing sum of all the items : {sum(l)}')

print(colls[11])
l = [1, 2, 3, 4, 5]
print(f'Items in the list {l}')
print(f'Printing largest number in the list : {max(l)}')

print(colls[12])
l = [1, 2, 3, 4, 5]
print(f'Items in the list {l}')
print(f'Printing middle number from the list : {(l[int(len(l) / 2)])}')

print(colls[13])
li = ['CAL', 'SEA', 'PIT', 'CAL', 'SEA']
print(f'Items in list {li}')
print(f'Printing items that appeared more than 1 ')
for key, value in dict(Counter(li)).items():
    if value > 1:
        print(f'{key} - {value}')

print(colls[14])
li = ['CAL', 'SEA', 'PIT', 'CAL', 'SEA']
print(f'Items in list {li}')
print(f'Printing items after removing duplicates')
for key, value in dict(Counter(li)).items():
    print(key)

print('Removing duplicates using set..')
st = set(li)
print(st)

print(colls[15])
states = ['CAL', 'SEA', 'PIT', 'CAL', 'POR', 'KEN', 'NJC']
print(f'Items in the list {states}')
print(f'remove only even items from the list and print')
states = states[1::2]
print(states)

print(colls[16])
li = ['CALIFORNIA', 'SEATTLE', 'PIT']
print(f'Items in the list {li}')
print('Printing Characters in each item of the list')
for i in li:
    print(f'Item : {i} No of Chars {len(i)}')

print(colls[17])
list1 = ['WA', 'CA']
list2 = ['Washinton', 'California']
print(f'2 lists {list1} and {list2}')
print('Adding 2 lists')
list3 = list1 + list2
print(f'Items in list 3 after adding {list3}')

print(colls[18])
mylist = [6, 2, 7, 3, 4, 5]
print(f'Items in the list {mylist}')
print('printing items in ascending order without using Sort function')
sort_list = []
for i in range(len(mylist)):
    num = min(mylist)
    sort_list.append(num)
    idx = mylist.index(num)
    mylist.pop(idx)
print(sort_list)

print(colls[19])
li = [4, 5, 2, 8, 3, 1]
print(f'Items in the list {li}')
print('printing the second largest item in the list')
print(f'Second largest number in the list {sorted(li)[-2:-1:]}')

print(colls[20])
mytuple = ('WA', 'CA', 'NY')
print(f'Items in the tuple {mytuple}')
print('Printing them one by one')
for i in mytuple:
    print(i)

print(colls[20])
mytuple = ('WA', 'CA', 'NY')
print(f'Items in the tuple {mytuple}')
print(f'Printing  first item using Index -> {mytuple[0]}')

print(colls[21])
mytuple = ('WA', 'CA', 'NY')
print(f'Items in the tuple {mytuple}')
mytuple = ("NJ",) + mytuple[1::]
print(f'Replacing first item with "NJ" -> {mytuple}')

print(colls[22])
mytuple = ('WA', 'CA', 'NY')
print(f'Items in the tuple {mytuple}')
print(f'Checking if "CA" exists -> {"CA" in mytuple}')

print(colls[23])
mytuple = ('WA', 'CA', 'NY')
print(f'Items in the tuple {mytuple}')
print(f'Printing length of Tuple {len(mytuple)}')

print('Set Exercises.....')
myset = {"NFL", "Cricket", "Baseball"}
print(f'printing set items -- printing without order.... {myset}')
print('Adding "Soccer" to Set ')
myset.add('Soccer')
print(f'printing set items after adding -- printing without order.... {myset}')
print('Using pop to remove item and print which item popped out')
popped = myset.pop()
print(f'Popped out items from set is : {popped}')

print('Set operations...intersect between two sets')
myset1 = {"NFL", "Cricket", "Baseball"}
myset2 = {"NFL", "Cricket", "Soccer"}
myset3 = {"NFL","Cricket"}
print(f' Set 1 {myset1} and set 2 {myset2}')
print(f'Set interset {myset1.intersection(myset2)}')
print(f'Set different 1 minus 2 {myset1.difference(myset2)}')
print(f'Set different 2 minus 1 {myset2.difference(myset1)}')
print(f'Set union {myset2.union(myset1)}')
print(f' Set 1 {myset1} and set 2 {myset3}')
print(f'Set 1 is superset of 3 -> {myset1.issuperset(myset3)}')
