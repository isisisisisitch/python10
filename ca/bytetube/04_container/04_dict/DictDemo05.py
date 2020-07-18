#2.Write a Python program to sum all the items in a dictionary.
grade_dict = {'Math':100,'physics':95,'English':90}
sum = 0
for value in grade_dict.values():
    sum += value

print(sum)