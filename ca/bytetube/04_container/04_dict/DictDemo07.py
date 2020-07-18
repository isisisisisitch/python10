#4.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
str = input('enter a string:\t')

dict = {}

for i in range(0, len(str)):
    dict[i] = str[i]

print(dict)