try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)#name 'num' is not defined