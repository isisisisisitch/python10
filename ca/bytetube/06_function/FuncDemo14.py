#filter(func, lst)函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象。如果要转换为列表, 可以使用 list() 来转换。

# 需求：找出所有的偶数

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(num):
   return  num % 2 == 0

res = filter(func,list1)#<filter object at 0x1010ec358>
print(res)

print(list(res))#[2, 4, 6, 8, 10]