#2.Write a Python program to count the elements in a list until an element is a tuple.
#在python中。容器支持相互嵌套

list1 = [1,2,3,4,(5,6,7),8]
count = 0
for i in list1:
    if isinstance(i, tuple):
        break

    count += 1

print(count)
