# 2. 列表
aa = [10, 20]
bb = aa

print(id(aa))#4525072264
print(id(bb))#4525072264

aa.append(30)
print(bb)  #[10, 20, 30]

print(id(aa))#4525072264
print(id(bb))#4525072264