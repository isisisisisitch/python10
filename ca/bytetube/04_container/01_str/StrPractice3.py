# 2.Remove the nth index character from a nonempty string
uer_input = input("plz input your word:")
index = int(input("plz input your index:"))

left_part = uer_input[0:index]
right_part = uer_input[index+1:]

after_removed = left_part + right_part

print(after_removed)