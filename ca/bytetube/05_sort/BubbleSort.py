num_list = [3,5,4,7,2,0,1]

count = len(num_list)-1#比较轮数
while count >0 :
    for j in range(0,count):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j + 1] = temp

    count -= 1


print(num_list)