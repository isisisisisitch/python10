
import threading
import time
#1.创建任务



def task():
    while True:
        print("task executing...")
        time.sleep(0.3)

if __name__ == '__main__':

    #2.创建线程
    sub_thread = threading.Thread(target=task)
    #指定新创建子线程为守护主线程
    sub_thread.setDaemon(True)

    #3.启动线程
    sub_thread.start()

    time.sleep(1)

    print("over")
