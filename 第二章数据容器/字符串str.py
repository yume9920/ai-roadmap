# 字符串存放字符,一个字符串可以存放任意数量的字符,单引号双引号三引号
# 定好后不能改变/有序性/可迭代性(可以用循环遍历出来)
# 每个字符也有对应的下标,通过对应索引找元素
# 切片语法和列表的一样
# 名[开始,结束,步长]

s='nih ao-yum e-99 20'
print(s[4])
print(s[-5])
# s[7]='ww'#会报错,字符串不可变
print(s[-5:-11:-1])#反向切片步长应该是负的
for i in s :
    print(i,end="   ")

# find()查找子串
# count()统计出现次数
# upper()全转为大写
# lower()全转为小写
# split()切割字符串,按指定分隔符分割成列表s.split('' )
# strip()去除空白字符或指定字符s.strip()/s.strip('*')
# replace()替换为新的字符s.replace('h','c')
# startswith()检查是否以子串开头,返回布尔值s.startswith('p')

print()
print(s.find("yume"))
print(s.upper())
s.split('-')
s.strip()
s.replace('m','n')
print(s.startswith('ni'))
print(s.endswith('10'))
print(s)#原始字符串没变,字符串不可变

youxiang=input("请输入你的邮箱地址:")
q=youxiang.count('@')
w=youxiang.count('.')
if q==1 and w>=1:
    print("邮箱地址正确")
else:
    print("邮箱地址错误")

# in 判断子串是否存在字符串中,返回布尔值
if youxiang.count('@')==1 and "."in youxiang:
    print("dizhizhengque")
else:
    print("dizhicuowu")

#练习题,输入一个字符串判断是否回文
zifuchuan=input("请输入一个字符串:")
fanzhuan=zifuchuan[-1::-1]
if fanzhuan==zifuchuan:
    print("这是回文")