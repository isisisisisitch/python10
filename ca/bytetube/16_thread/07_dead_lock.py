import threading

#0.创建互斥锁
#解决方法：
#1。结束函数 return
#2。异常捕获

lock = threading.Lock()

#1.创建任务
#需求：多线程同时根据index在list中取值，要保证同一时刻只能有一个线程取值
def get_val_from_list(index):
    print(threading.current_thread())

    lock.acquire()
    my_list = [10, 11, 12]
    try:
        print(threading.current_thread(),"+",my_list[index])

    except Exception as result:
        print(result)

    #print(threading.current_thread(),"lock release")
    lock.release()


if __name__ == '__main__':
# 2.创建线程
    for i in range(10):
        sub_thread = threading.Thread(target=get_val_from_list, args=(i,))

        # 3.启动线程
        sub_thread.start()


