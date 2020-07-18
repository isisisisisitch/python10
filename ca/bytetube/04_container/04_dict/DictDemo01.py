dict1 = {'name': 'Tom', 'age': 20, 'gender': 'M'}
print(dict1.get('name'))  # Tom
print(dict1.get('id', 110))  # 110
print(dict1.get('id'))  # None