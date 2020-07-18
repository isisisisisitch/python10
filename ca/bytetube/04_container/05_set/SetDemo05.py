list1 = ['a', 'b', 'c', 'd', 'e']

# for i in enumerate(list1):
#     print(i)

for index, char in enumerate(list1, start=1):
    print(f'下标是{index}, 对应的字符是{char}')