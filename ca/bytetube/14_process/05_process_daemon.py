import multiprocessing
import time



#1.创建任务

def task():
    while True:
        print("task executing...")
        time.sleep(0.5)


if __name__ == '__main__':

    #2.创建子进程
    sub_process = multiprocessing.Process(target=task)
    sub_process.daemon = True

    #3.开启进程
    sub_process.start()

    time.sleep(0.8)

    #sub_process.terminate()
    print("main over")