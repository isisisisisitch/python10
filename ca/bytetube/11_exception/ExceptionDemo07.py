try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('no exception')
finally:
    print("close stream")
    f.close()