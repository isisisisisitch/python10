dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1 #key

# 对字典进行拆包，取出来的是字典的key
print(a)  # name
print(b)  # age

print(dict1[a])  # TOM
print(dict1[b])  # 18