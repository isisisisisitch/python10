#求3个整数的平均数


def sum(list):
    res = 0
    for i in range(len(list)):
        res += list[i]

    return res


def avgNum(list):

    return sum(list)/len(list)



list=[1,2,3,4,5]
print(avgNum(list))