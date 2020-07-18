row = 1
# e = 1

while row < 5:
    col = 0
    while col < row:#打印*的个数和行数相同，所以可以利用row作为col的循环判断条件
        print('*', end=' ')
        col += 1
    print('\n')
    row += 1
    # e += 1


