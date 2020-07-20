# 3 + 2 + 1
def sum_numbers(num):#num--->3
           #3 + sum_numbers(2)
  #                  |
  #                  |
  #          2+ sum_numbers(1)
  #                  |
  #                  |
           # 1+ sum_numbers(0)
  #                  |
  #                  |
           #sum_numbers(0)=0
    if num == 0:
        return 0
    return num + sum_numbers(num-1)


sum_result = sum_numbers(3)
# 输出结果为6
print(sum_result)

#fib 1,1,2,3,5,8,13,21,34... n=4 --->value = 5