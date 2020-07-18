str1 = input('Please enter Main string you are looking into: ')
substr1 = input('Please enter substring you are looking for: ')
count = 0
for i in range(len(str1)):
    tempstr1 = str1[i::]
    if tempstr1.find(substr1) != -1:
        count += 1
    i += 1

print(count)