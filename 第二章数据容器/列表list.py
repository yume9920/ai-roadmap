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




