import multiprocessing
import os
import time




#1.指定任务

def coding():
    #获取当前进程（子进程）的编号
    coding_process_id = os.getpid()#coding_process_id: 15688
    print("coding_process_id:", coding_process_id, multiprocessing.current_process())#coding_process_parent_id: 15687

    # 获取当前进程（子进程）的父进程的编号
    coding_process_parent_id = os.getppid()
    print("coding_process_parent_id:", coding_process_parent_id)
    for i in range(10):
        print("coding...")
        time.sleep(0.5)


def debugging():
    # 获取当前进程（子进程）的编号
    debugging_process_id = os.getpid()#debugging_process_id: 15689
    print("debugging_process_id:", debugging_process_id)#debugging_process_parent_id: 15687

    # 获取当前进程（子进程）的父进程的编号
    debugging_process_parent_id = os.getppid()
    print("debugging_process_parent_id:", debugging_process_parent_id, multiprocessing.current_process())
    for i in range(10):
        print("debugging...")
        time.sleep(0.5)


#2。创建子进程（手动创建的进程是子进程，在Process类的__init__）
# group：指定进程组，目前只能使用None
# target：执行的目标任务名
# name：进程名字

coding_process = multiprocessing.Process(target=coding, name="coding_process")
debugging_process = multiprocessing.Process(target=debugging, name="debugging_process")

#3。启动进程执行对应的任务
coding_process.start()
debugging_process.start()

#4.注意事项：进程执行是无序的，具体哪个进程先执行是由操作系统来决定的