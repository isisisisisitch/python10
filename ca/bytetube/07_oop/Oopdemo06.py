class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):

        return 'LG width is ' + f'{self.width}, ' + 'LG height is ' + f'{self.height}'


LG = Washer(10, 20)

print(LG)#LG width is 10, LG height is 20