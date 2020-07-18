# # 1. 接收用户输入
# num = input('plz input your luck num：')
#
# # 2. 打印结果
# print(f"your luck num is {num}")
#
#
# # 3. 检测接收到的用户输入的数据类型 -- str类型
# print(type(num))
#
# # 4. 转换数据类型为整型 -- int类型
# print(type(int(num)))

# 1. float() -- 转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))

# 2. 01_str() -- 转换成字符串类型
num2 = 10
print(type(str(num2)))

# 3. 03_tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))


# 4. 02_list() -- 将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))

# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))