#x if 条件 else y   <===> if else
a = 1
b = 2

d = 10
e = 100

c = a if a > b else b
c = (d if d > e else e) if a < b else b
print(c)