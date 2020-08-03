# f = open('test.txt', 'r')
#
# con = f.readlines()
# print(con)
#
# f.close()


f = open('test.txt', 'r')

content = f.readline()
print(f'first line：{content}')

content = f.readline()
print(f'second line：{content}')

# 关闭文件
f.close()