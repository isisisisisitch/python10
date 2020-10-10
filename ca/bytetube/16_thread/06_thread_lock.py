import threading
import time

#全局量
g_sum = 0

#创建互斥锁
lock = threading.Lock()

#1.创建任务
#循环100万次进行累加任务
def task1():
    current_thread = threading.current_thread()
    print("current_thread:", current_thread)
    #上锁
    lock.acquire()
    for i in range(10):
        global g_sum
        g_sum = g_sum + 1

        print("task1 res:", g_sum,current_thread)
        # 释放锁
    # lock.release()



#2.创建线程

if __name__ == '__main__':

    #2.创建子线程

    task1_thread = threading.Thread(target=task1, name="task1_thread")
    task2_thread = threading.Thread(target=task1, name="task2_thread")

    task1_thread.start()
    #让当前线程（主线程）等待add_data_thread子线程执行结束之后，再继续执行
    #time.sleep(1)
    #task1_thread.join()
    task2_thread.start()

#3.启动线程