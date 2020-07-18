age = int(input('plz input your age：'))
# if age < 18:
#     print(f'your age is {age},illegal')
# elif (age >= 18) and (age <= 60):
#     print(f'your age is {age},legal')
# else:
#     print(f'your age is {age},retied')

if age >= 60:
    print("You are supposed to be retired.")
if age >= 18:
    print("You are able to work legally.")
else:
    print("You are too young to work!")