print("before")
try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')


print("after")