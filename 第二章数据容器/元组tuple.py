# tuple用来存储只能查询不能修改的元素(区别于列表)
# 创建后不可变
# 可以存储不同类型的元素.可重复,有序

# 定义
# 名称=()

# count()查次数
# index()匹配第一次出现的索引位置

# t=(21,True,2.1)
# t2=()
# print(t[2])
# print(type(t))
# (print(type(t2)))

# # 切片
# print(t[::2])
# print(t.count(21))
# print(t.index(21))

# #定义单元素元组
# t3=(100,)
#没逗号不行


#组包
t=(1,2,34,22)
# 解包
a,b,c,d=t
#扩展解包
# *会收集剩余元素
a1,*b1,c1=t
print(b1)
# a,b=b,a相当于进行了组包操作

student=(
    ("s001","王琳",85,92,88),
    ("s002","xiaomin",23,45,67)

)
for s in student:
    total=s[2]+s[3]+s[4]
    print(f"{s[0]},{total}")#原稿写f"s{0}"只会打s0,{0}不是占位符,要写{s[0]}

chinese_score=[s[2] for s in student]

# =========补充:P49案例的优化写法=========
# sum()+切片:总分不用一个一个加
for s in student:
    print(f"{s[0]}的总分:{sum(s[2:])}")#s[2:]从下标2取到末尾
# 推导式取一列,再求平均
print(f"语文平均分:{sum(chinese_score)/len(chinese_score)}")
