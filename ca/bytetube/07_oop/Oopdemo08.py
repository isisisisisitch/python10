class Furniture():
    #- 家具名称
    #- 家具占地面积
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f' {self.name} takes {self.area} m2'



class Home():
    # - 房子地理位置
    # - 房子占地面积
    # - 房子剩余面积
    # - 房子内家具列表

    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furnitures = []


    def add_furnitures(self,furniture):
        print(f'adding {furniture}' )

        if furniture.area > self.free_area:
            print("there is not enough space to add this furniture in")
            return #当函数运行到这里时，整个函数停止
        self.furnitures.append(furniture)
        self.free_area -= furniture.area
        print(f' remaining area: {self.free_area}')


cando  = Home("trt",60)
bed = Furniture("bed",4)
table = Furniture("table",3)

king = Furniture("king",54)

cando.add_furnitures(bed)
cando.add_furnitures(table)
cando.add_furnitures(king)




