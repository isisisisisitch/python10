import time


try:
    #mode empty: default ---> read
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产生了异常，那么就会捕获到
        # 比如 按下了 ctrl+c
        print('The read data was unexpectedly terminated')
    finally:
        f.close()
        print('close file')
except:
    print("no such file")