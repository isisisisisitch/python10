
#外层循环控制行数
#里层循环控制列数

row = 0

while row < 4:
    col = 0
    while col < 4:
        print("*" , end="  ")
        col += 1

    print()

    row += 1

