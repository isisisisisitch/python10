#3.5.2. 列表数据按字典key的值排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

students.sort(key=lambda n: n['name'])
print(students)#[{'name': 'Jack', 'age': 22}, {'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}]


students.sort(key=lambda n: n['name'],reverse=True)
print(students)#[{'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}, {'name': 'Jack', 'age': 22}]


students.sort(key=lambda n: n['age'])
print(students)#[{'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}, {'name': 'Jack', 'age': 22}]