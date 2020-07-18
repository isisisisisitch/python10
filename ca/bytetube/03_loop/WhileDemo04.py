i = 1
while i <= 5:
    if i == 3:
        print(f'there is a bug，I donot want the{i} apple')
        # 在continue之前一定要修改计数器，否则会陷入死循环
        #i += 1
        continue#退出当次循环,回到while进行判断

    print(f'this is the {i} apple')
    i += 1