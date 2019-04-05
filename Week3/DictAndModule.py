#! /usr/bin/env python
import heapq as h
import math
# Dictionary & using Python modules
# Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and print
# Microsoft started in Bellevue
# Amazon started in Seattle
# Boeing started in Everett
# Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and sort (hint: sorted global function) the dictionary and print
# Amazon started in Seattle
# Boeing started in Everett
# Microsoft started in Bellevue
# Write a python script that can take mydict1 = {‘House1’: 1000, ‘House2’: 3000, ‘House3’: 5000} and mydict2 = {‘House1’: 6000, ‘House3’: 8000, ‘House2’: 6000} and to combine two dictionary adding values for common keys.
# Output should be mydict3={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000}
# Write a python script that can take mydict={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000} and print two largest values in the dictionary.
# Hint: use nlargest function in heapq module
# Write a python script that can take x = 3, using loops create three key and value pairs disctionary {1:1, 2:4, 3:6}. If key = 1, value is 1+1, for 2 value is 2+2, etc.
# Write a python script that can take x = 3, using loops create key and value pairs disctionary {4:2, 9:3, 16:4}. If key = 4, value sqrt(4) is 2, for 9 value is 3, etc.
# Hint: use sqrt function in Math module
# Write a python script that can take x = 3, using loops create key and value pairs disctionary {1:1, 2:8, 3:27}. If key = 2, value pow(2) is 8, for 3 value is 27, etc.
# Hint: use pow function in Math module

print('Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and print ')
mydict = {'Bellevue': 'Microsoft', 'Seattle': 'Amazon', 'Everett': 'Boeing'}
print(f'My Dictionary Data {mydict}')
for i in (mydict):
    print(f'{mydict[i]} started in {i}')


print('Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and print in Sorted Order ')
mydict = {'Bellevue': 'Microsoft', 'Seattle': 'Amazon', 'Everett': 'Boeing'}
print(f'My Dictionary Data {mydict}')
for i in sorted(mydict.values()):
    for key, value in mydict.items():
        if value == i:
            print(f'{i} Started in {key}')

print('Exercise 3')

mydict1 = {'House1': 1000, 'House2': 3000, 'House3': 5000}
mydict2 = {'House1': 6000, 'House3': 8000, 'House2': 6000}
mydict3 = {}
for k,v in mydict1.items():
    mydict3[k] = v + mydict2[k]

print(mydict3)

print(' Write a python script that can take mydict={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000} and print two largest values in the dictionary')

mydict = {'House1': 7000, 'House2': 9000, 'House3': 13000}
print('printing two largest values in the dictionary')
print(h.nlargest(2,mydict.values()))

print('Write a python script that can take x = 3, using loops create three key and value pairs disctionary {1:1, 2:4, 3:6}. If key = 1, value is 1+1, for 2 value is 2+2, etc.')

x = 3
mydct = {}
for i in range(1, x+1):
    mydct[i] = i + i

print(f'Printing Dict Values {mydct}')

print('Write a python script that can take x = 3, using loops create key and value pairs disctionary {4:2, 9:3, 16:4}. If key = 4, value sqrt(4) is 2, for 9 value is 3, etc.')

x = 3
newdct = {}
for i in range(2,5,1):
    k = i * i
    newdct[k] = int(math.sqrt(k))

print(f'The New Dict is {newdct}')

print('Printing keys and values with Power of function from Math')

x = 3
newdct = {}
for i in range(1, x+1):
    newdct[i] = int(math.pow(i,i))

print(f'The New Dict is {newdct}')