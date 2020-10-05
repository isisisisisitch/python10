import threading
import time


#1.add 2.read
#list
g_list = []
#1.创建任务

def add_data():
    # 获取当前线程
    current_thread = threading.current_thread()
    print("add_data:", current_thread)

    for i in range(5):
        g_list.append(i)
        print("added:",i)
        time.sleep(0.3)

    print("after added:",g_list)



def read_data():
    # 获取当前线程
    current_thread = threading.current_thread()
    print("read_data:", current_thread)
    print("read:", g_list)


if __name__ == '__main__':

    #2.创建子线程

    add_data_thread = threading.Thread(target=add_data, name="add_data_thread")
    read_data_thread = threading.Thread(target=read_data, name="read_data_thread")

    add_data_thread.start()
    #让当前线程（主线程）等待add_data_thread子线程执行结束之后，再继续执行
    #time.sleep(1)
    add_data_thread.join()
    read_data_thread.start()