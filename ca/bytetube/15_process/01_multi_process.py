import multiprocessing
import time




#1.指定任务

def coding():
    for i in range(10):
        print("coding...")
        time.sleep(0.5)


def debugging():
    for i in range(10):
        print("debugging...")
        time.sleep(0.5)


#2。创建子进程（手动创建的进程是子进程，在Process类的__init__）
# group：指定进程组，目前只能使用None
# target：执行的目标任务名
# name：进程名字

coding_process = multiprocessing.Process(target=coding)
debugging_process = multiprocessing.Process(target=debugging)

#3。启动进程执行对应的任务
coding_process.start()
debugging_process.start()

#4.注意事项：进程执行是无序的，具体哪个进程先执行是由操作系统来决定的