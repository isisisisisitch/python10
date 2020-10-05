
import multiprocessing




#1.创建任务
def show_info(name,age):
    print(name,age)


#2.创建子进程
# info_process = multiprocessing.Process(target=show_info, args=("bytetube",4))
# info_process = multiprocessing.Process(target=show_info, kwargs={"name":"bytetube", "age": 4})

#win 出现递归调用：mac或者linux不会出现进程拷贝，win操作在创建子进程的时候，会进行拷贝，

if __name__ == '__main__':

    info_process = multiprocessing.Process(target=show_info, args=("bytetube",), kwargs={"age": 4})
    #3.开启进程
    info_process.start()