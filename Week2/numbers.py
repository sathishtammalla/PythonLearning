# Write a Python program that takes x = 1, y = 1.1, and z = 1.2j and print it.
# Write a Python program that takes x = 1, y = 1.1, and z = 1.2j and print their data type using type function. Ex: print(type(x))
# Write a Python program that takes y = 1.1, and z = “9” and cast them to int using int(y).
# Write a Python program that takes y = 1.1, and z = “9” and cast them to float using float(y).
# Write a Python program that takes y = 1.1, and z = “9” and cast them to string using str(y).

print('Numbers Exercise')
print('Write a Python program that takes x = 1, y = 1.1, and z = 1.2j and print it.')
x = 1
y = 1.1
z = 1.2j
print(f'Value of x : {x}')
print(f'Value of y : {y}')
print(f'Value of z : {z}')

print('Printing the data types of x, y, z variables')

print(f'type of x : {type(x)}')
print(f'Value of y : {type(y)}')
print(f'Value of z : {type(z)}')

print('Write a Python program that takes y = 1.1, and z = “9” and cast them to int using int(y).')
y = 1.1
z = '9'
print(f'Value of y : {y} type of y : {type(y)} and converting to int {int(y)}')
print(f'Value of z : {z} type of z : {type(z)} and converting to int {int(z)}')

print('Write a Python program that takes y = 1.1, and z = “9” and cast them to float using float(y).')
y = 1.1
z = '9'
print(f'Value of y : {y} type of y : {type(y)} and converting to float {float(y)}')
print(f'Value of z : {z} type of z : {type(z)} and converting to float {float(z)}')

print('Write a Python program that takes y = 1.1, and z = “9” and cast them to string using str(y).')
y = 1.1
z = 9.1j
print(f'Value of y : {y} type of y : {type(y)} and converting to String {str(y)}')
print(f'Value of z : {z} type of z : {type(z)} and converting to String {str(z)}')
