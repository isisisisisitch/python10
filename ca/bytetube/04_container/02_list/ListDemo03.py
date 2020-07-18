# name_list = ['Tom', 'Lily', 'Rose']
#
# # 结果：报错提示：name 'name_list' is not defined
# del name_list#删除对象 --->删除对象在计算机中的内存
# print(name_list)#name 'name_list' is not defined

# name_list = ['Tom', 'Lily', 'Rose']
#
# del name_list[0]
#
# # 结果：['Lily', 'Rose']
# print(name_list)


# name_list = ['Tom', 'Lily', 'Rose']
#
# del_name = name_list.pop(1)
#
# # 结果：Lily
# print(del_name)
#
# # 结果：['Tom', 'Rose']
# print(name_list)

name_list = ['Rose', 'Tom', 'Lily', 'Rose']

name_list.remove('Rose')

# 结果：['Tom', 'Lily']
print(name_list)