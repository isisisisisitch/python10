#map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表返回。

# 需求：计算`list1`序列中各个数字的2次方。
list1 = [1, 2, 3, 4, 5]

def func(num):
    return num ** 2

res = map(func,list1)
print(list(res))#[1, 4, 9, 16, 25]


