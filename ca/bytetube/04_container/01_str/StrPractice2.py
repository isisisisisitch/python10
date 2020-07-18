# 1.Add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged
uer_input = input("plz input your word:")

length = len(uer_input)
if length > 2:
    if uer_input[-3:] == 'ing':
        uer_input += 'ly'

    else:
        uer_input += 'ing'

print(uer_input)