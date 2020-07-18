# 定义函数
#
def sum(num1, num2):
    """ 求和函数 """
    result = num1 + num2
    return result

#
def multi(num1,num2):
    """ 求积函数 """
    result = num1 * num2
    return result

# 调用函数
res = multi(sum(1,2),sum(2,2))
print(res)
help(sum)
help(multi)