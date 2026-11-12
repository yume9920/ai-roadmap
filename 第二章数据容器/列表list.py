# # 变量只能存储一个数据
# # 容器用来大量存储
# # 每个数据称之为一个元素,可以是任意类型
# # 列表名称=[元素1,2,3,4,5,......]

# s=[True,14.2,56,76,56,"hallo"]#可存储不同类型元素,元素有序,可重复,可修改
# # 下标索引从0开始
# # s[0],s[1],s[2],s[3]
# # 反向索引从-1开始(最后一个元素)
# # s[-1],s[-2],s[-3],s[-4]
# # 这样的容器类型可以称为序列
# print(type(s))
# print(type(s[0]))
#
# #获取
# # s[0]==s[-6]
# print(s[0])
# print(s[-6])
#
# #修改
# s[2]="abd"
# print(s[2])
# print(s)
# # 指定的索引超出范围会报错
# # s[9]="meiyou"
# # print(s)
#
# #删除
# del s[3]
# del s[1]
# del s[0]
# print(s)
#
# #遍历
# for i in s:
#     print(i)
# #与存储顺序一致
#
# #切片:截取列表一部分进行操作
# # 序列数据[开始索引:结束索引:步长]
# # 包含开始不包含结束,开始默认为0,结束默认为列表长度,步长默认为1
# # 可正向和反向索引
#
# print(s[0:3:1])
# print(s[0:3:2])
# print(s[:3:2])
# print(s[0:2])
# print(s[::2])
# print(s[0:-2:1])#正反都行,也可混用

# 方法(功能)----对象
# append()#在列表尾部添加元素s.append(100)
# insert()#在指定索引之前插入元素s.insert(0,92)
# remove()#移除列表中第一个匹配到的元素s.remove(88)
# pop()#删除指定索引位置的元素,未指定默认删最后一个s.pop(2)/s.pop()
# sort#对列表进行排序(需要数据类型一致)s.sort()
# reverse()#反转列表元素(最后一个变成第一个)s.reverse()
# s=[1,2,3,4,5,6,7,8,9,10]
# s.append(111)
# print(s)
#
# s.insert(0,90)
# print(s)
#
# s.remove(7)
# print(s)
#
# s.pop(3)
# print(s)
#
# s.reverse()
# print(s)
#
# s.sort()
# print(s)

# num_list=[]#定义空列表
# for i in range(10):
#     num=int(input("请输入一个有效数字: "))
#     num_list.append(num)

# print("数字列表为:",num_list)
# num_list.sort()
# print("排序后的数字列表:",num_list)

# print("最小值为:",num_list[0])
# print("最大值为:",num_list[-1])
# print("平均值为:",sum(num_list)/len(num_list))#sum求和,len获取列表长度(个数)


# numlist1=[19,23,54,64,875,20,109,232,123,54]
# numlist2=[55,80,72,60,123,54,29,91]
# #合并列表
# for i in numlist2:
#     numlist1.append(i)
#简化代码:
    # 解包:将容器解成独立元素用*号
        # numlist=[*numlist2,*numlist1]
    # 组包:多个值合并到一个容器
            # numlist = numlist2+numlist1
# print(numlist1)
# #去除重复元素
# new_list=[]
# for s in numlist1:
#     if s not in new_list:
#             new_list.append(s)
# print(new_list)

numlist=[]
for i in range(1,21):
    numlist.append(i**2)
print(numlist)#生成1-20的平方列表,秒了

#从下面列表提取所有偶数并计算平方组成新的列表
numll=[19,23,54,64,87,20,109,232,123,43,26,55,72]
num=[]
for s in numll:
    if s%2==0:
        num.append(s**2)
num.sort()
print(num)#自己完成,可运行

# =================补充:黑马P36-42里有,但我原稿没写到的=================
# 1.P39 常用方法里没用到四个:index / count / clear / extend
# index()#查找指定元素的下标,只找第一个,找不到直接报错 s.index(元素)
# count()#统计指定元素出现几次 s.count(元素)
# clear()#清空整个列表 s.clear()
# extend()#把另一个容器的元素逐个取出,加到尾部 s.extend(另一个列表)
s=[1,2,3,2,4,2]
print(s.index(2))#1,只找第一个
print(s.count(2))#3
#print(s.index(99))#ValueError: 99 is not in list  找不到是报错,不是返回-1
a=[1,2,3]
b=[4,5]
a.extend(b)
print(a)#[1,2,3,4,5]  元素被逐个拆开加进去
c=[1,2,3]
c.append(b)
print(c)#[1,2,3,[4,5]]  对比:append把b整个当一个元素塞进去
s.clear()
print(s)#[]
#
# 2.P37 嵌套列表:列表里套列表,下标连续取 s[外层][内层]
n=[[1,2,3],[4,5,6],[7,8,9]]
print(n[1])#[4,5,6]
print(n[1][2])#6
print(n[-1][-2])#8  反向索引同理
#
# 3.while遍历列表(P40案例):靠下标走,必须有i+=1
s=[10,20,30]
i=0
while i<len(s):
    print(s[i])
    i+=1
#
# 4.解包组包(P41案例),原稿只有注释,补上能跑的
numlist1=[19,23,54,64,875,20,109,232,123,54]
numlist2=[55,80,72,60,123,54,29,91]
numlist=[*numlist1,*numlist2]#解包:两个列表打散成一个
print(numlist)
#
# 5.列表推导式(P42案例):[表达式 for 变量 in 容器 if 条件]
# 一行代替"空列表+for+append"三步
num2=[x**2 for x in numll if x%2==0]#就是上面偶数平方那题
num2.sort()
print(num2)
sq=[i**2 for i in range(1,21)]#1-20平方列表也一行
print(sq)




