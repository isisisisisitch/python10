class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
     print(f'LG width is {self.width}')
     print(f'LG height is {self.height}')


LG = Washer(10, 20)
LG.print_info()


LG2 = Washer(30, 40)
LG2.print_info()