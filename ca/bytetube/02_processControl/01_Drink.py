# age = 20
#
# if age >= 18:
#     print("enjoy!")
#
# print("code is here")

# input接受用户输入的数据是字符串类型，条件是age和整型18做判断，所以这里要int转换数据类型
# age = int(input('plz input your age：'))
#
# if age >= 18:
#     print(f'your age is {age},adult,enjoy your life')
#
#
# print('system closed')

age = int(input('plz input your age：'))

if age >= 18:
    print(f'your age is {age},adult,enjoy your life')

else:
    print(f'your age is {age},You are not allowed ....')

print('system closed')