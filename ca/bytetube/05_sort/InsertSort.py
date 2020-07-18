num_list = [3,5,4,7,2,0,1]
for i in range(len(num_list)):#i 是最左端的下标
    for j in range(i,0,-1):
        # num_list[j]有顺序的序列的最大值（即有序序列最右端值），num_list[j-1]无序序列的最左端值
        if num_list[j] < num_list[j-1]:
            temp = num_list[j]
            num_list[j] = num_list[j - 1]
            num_list[j - 1] = temp

print(num_list)
