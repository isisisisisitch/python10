"""
1. 如果有钱，则可以上车
    2. 上车后，如果有空座，可以坐下
    上车后，如果没有空座，则站着等空座位
如果没钱，不能上车
"""
# 假设用 money = 1 表示有钱, money = 0表示没有钱; seat = 1 表示有空座，seat = 0 表示没有空座
money = 0
seat = 1
if money >= 1:
    print('get on the bus')
    if seat >= 1:
        print('there is an available seat')
    else:
        print('there is no available seat')
else:
    print('can not get on the bus')