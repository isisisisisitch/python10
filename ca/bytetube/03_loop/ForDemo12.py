# str1 = 'bytetube'
# for i in str1:
#     print(i)
# else:
#     print('code after loop...')

str1 = 'bytetube'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print('code after loop...')