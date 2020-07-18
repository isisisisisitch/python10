name_list = ['Tom', 'Lily', 'Rose']

name = input('plz input your name：')

if name in name_list:
    print(f'your input name is {name}, already exists')
else:
    print(f'your input name is {name}, avalilable')