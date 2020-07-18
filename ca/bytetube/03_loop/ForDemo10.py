#
# #外层循环控制行数
# #里层循环控制列数
#
# row = 0
#
# while row < 4:
#     col = 0
#     while col < 4:
#         print("*" , end="  ")
#         col += 1
#
#     print()
#
#     row += 1
# for 临时变量 in 序列:
# #     重复执行的代码1
# #     重复执行的代码2
# #     ......

for row in range(0,4):
    for col in range(0,4):
        print("*", end="  ")

    print()