# 1. 定义类
class Washer():
    def wash(self):#self指的是调用该函数的对象。
        print('wash clothes')

        print(self)


# 2. 创建对象
LG = Washer()

print(LG)#<__main__.Washer object at 0x10d9160b8>

# LG对象调用实例方法
# wash clothes
# <__main__.Washer object at 0x10d9160b8>
LG.wash()


LG.width = 500
LG.height = 800

print(f'LG width is {LG.width}')
print(f'LG height is {LG.height}')