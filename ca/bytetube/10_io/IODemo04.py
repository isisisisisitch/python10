# 需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能(备份文件名为xx_backup后缀，例如：sound_backup.mp3)
#1.获取用户输入的要备份的文件名:sound.mp3
file_name = input("plz enter the file you want to backup:")
#2.规划备份文件的名称
#2.1 获取后缀名
index = file_name.rfind('.')

#判断文件的有效性

if index > 0:
    surffix = file_name[index:]#后缀名

#2.2 组装备份文件名称

new_file_name = file_name[:index]+'_backup' + surffix
print(new_file_name)

#3.备份文件 （先读入，再写出）
file_reader = open(file_name, 'rb')
file_writer = open(new_file_name, 'wb')

while True:
    res = file_reader.read(1024)
    if len(res) == 0:
        break

    file_writer.write(res)

file_reader.close()
file_writer.close()