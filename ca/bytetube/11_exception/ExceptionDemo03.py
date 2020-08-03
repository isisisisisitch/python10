try:
    #print(num)
    print(1/0)

except (NameError, ZeroDivisionError):
    print('there is an error')