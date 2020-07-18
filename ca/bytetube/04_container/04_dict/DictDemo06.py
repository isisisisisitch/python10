#3.Write a Python program to sort a dictionary by key.
color_dict = {'red':'#FF0000','white':'#FFFFFF','black':'#000000','green':'#00FF00'}
for key in sorted(color_dict):
    print(f'{key} : {color_dict[key]}')


