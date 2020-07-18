#1.Write a Python script to merge two Python dictionaries.
dict1={'name':'dal','age':30 , 'weight': 62}
dict2={'job':'sde','addr':'van'}
new_dict = dict1.copy()
new_dict.update(dict2)

print(new_dict)