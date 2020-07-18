num_list = [3,5,4,7,2,0,1]

for i in range(len(num_list)):#i 是最左端的下标
    min_index = i

    for j in range(i+1,len(num_list)):
        if (num_list[j] < num_list[min_index]):
            min_index = j

    temp = num_list[i]
    num_list[i] = num_list[min_index]
    num_list[min_index] = temp


print(num_list)