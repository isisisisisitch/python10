# 定义类
class Washer():
    def print_info(self):
        # 类里面获取实例属性
       print(f'LG width is {self.width}')
       print(f'LG height is {self.height}')
       print(f'LG height is {self.length}')#AttributeError: 'Washer' object has no attribute 'length'

# 创建对象
LG = Washer()

# 添加实例属性
LG.width = 500
LG.height = 800

LG.print_info()