
import multiprocessing


#list
#1.add 2.read
#1.创建任务
import time

g_list = list()
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:",i)
        time.sleep(0.5)

    print("after add:", g_list)


def read_data():
    print("read:", g_list)


#2.创建子进程
add_data_process = multiprocessing.Process(target=add_data)
read_data_process = multiprocessing.Process(target=read_data)

#3.启动进程
add_data_process.start()
print("main:", g_list)
read_data_process.start()