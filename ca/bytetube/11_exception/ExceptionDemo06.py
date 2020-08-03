try:
    print(1/0)
except Exception as result:
    print(result)
else:
    print('this is else, the code executes when there is no exception')

print("after")