"""Write a Python program that takes mydict = { “Game”: “NFL”, “Team”: “Seahwaks”, “City”: “Seattle”} and print mydict.
Print the value of “Team” key using mydict[“Team”]
Print the value of “Team” key using mydict,get(“Team”)
Change the value of “Game” = “XFL”
Print all the key names in the dictionary using for loop.
Print all the key values in the dictionary using for loop.
Check if key “Team” exists and print Yes, it exists.
Remove “Game” using pop method.
Add “Year” = “1980” to the mydict.
Remove using popitem method (which one does it remove?)
Clear all the items in the mydict.
"""

print('Dictionaries Exercises....')
mydict = {'Game': 'NFL', 'Team': 'Seahwaks', 'City': 'Seattle'}
print(f'Printing the items in the dictionary {mydict}')

print('Printing the value of "Team" key using dict("team")')

print(f'Team Key is -> {mydict["Team"]}')

print(f'Printing team name using dict.get option  --> {mydict.get("Team")}')

print('Changing the value of game to XFL ')
mydict['Game'] = 'XFL'

print(f'After Changing the value of game dict is -> {mydict}')
print('Printing all the key names in the dictionary using for loop')
for key in mydict.keys():
    print(f'Key : {key}')

print('Printing all the key and Value names in the dictionary using for loop')
for key,value in mydict.items():
    print(f'Key : {key}  Value : {value}')

print('Check if key “Team” exists and print Yes, it exists.')
if 'Team' in mydict:
    print('Yes, key "Team" exists in Dictionary ')

print('Remove “Game” using pop method.')
mydict.pop('Game')
print(f'Printing the items in the dictionary after Pop {mydict}')

print('Add “Year” = “1980” to the mydict.')
mydict['Year'] = '1980'
print(f'Printing the items in the dictionary after Add {mydict}')

print('Remove using popitem method (which one does it remove?)')

popitem = mydict.popitem()
print(f'Popped Item from dict {popitem} and dict is {mydict}')

print('Clear all the items in the mydict.')
mydict.clear()
print(f'Cleared Dict {mydict}')