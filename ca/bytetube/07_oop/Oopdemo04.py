class Washer():

    # 定义初始化功能的函数
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

#在init方法中定义的对象属性，在类的其他成员方法中，可以获取到
    def print_info(self):
        # 类里面调用实例属性
        print(f'LG width is {LG.width}, height is {LG.height}')


LG = Washer()
print(LG)