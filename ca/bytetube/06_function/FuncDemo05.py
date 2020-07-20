def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]

    return sum


sum = add(1,2,3,4,5)
print(sum)