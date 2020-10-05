
import threading
import time


#1.创建任务
def coding():
    #获取当前线程
    current_thread = threading.current_thread()
    print("coding:",current_thread)
    for i in range(10):
        print("coding...")
        time.sleep(0.5)


def debugging():
    # 获取当前线程
    current_thread = threading.current_thread()
    print("debugging:", current_thread)

    for i in range(10):
        print("debugging...")
        time.sleep(0.5)


#2.创建线程（线程和任务进行捆绑）
coding_thread = threading.Thread(target=coding,name="coding_thread")
debugging_thread = threading.Thread(target=debugging,name="debugging_thread")

#3.启动线程
debugging_thread.start()
coding_thread.start()


#4.注意事项：线程执行是无序的，具体哪个线程先执行是由操作系统来决定的