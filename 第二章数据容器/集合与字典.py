# 集合set存储不重复的数据,因为会自动去重
# 无序,不可重复,可修改
# s1={"a","s","s","d"}
# s2=set()
# s=tuple()
# #定义空

# print(s1)
# print(s2)

# add添加
# remove删除指定
# pop随机删除并返回
# clear清空
# difference求差集
# union求并集
# intersection求交集

# s1.add(120)
# print(s1)
# s1.remove("s")
# s1.pop()
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)

# 差集有先后顺序,其他两个没有

# 求交集也可以使用&
# 减号可以求差集
# 集合推导式:{for s in set1 if 条件}


# 字典dict根据字或词找到对应解释
# 存储的是键值对(key:value)
dict1={"王琳":100,"艾琳":129,}
# key不能重复,可修改
# 名称=dict()#空
# dict={}
# value可以是任何类型,key不能是可变类型,如list,set,dict
# key如果重复,后面的值会覆盖前面的值
# 获取:v=dict["王琳"]

# dict["涛哥"]=454#添加,存在则修改
# 删除:dict1.pop(key)[返回对应value]或del dict1["涛哥"]

# 获取:dict1.get("涛哥")
# dict.keys()
# dict.values()
# dict.items()

# =========补充:让注释里的方法跑起来========
s1={1,2,3}
s2={2,3,4}
print(s1 & s2)#交集 {2,3}
print(s1 | s2)#并集 {1,2,3,4}
print(s1 - s2)#差集 {1}  s1有s2没有,有先后顺序
print({x**2 for x in s1})#集合推导式

dict1={"王琳":100,"艾琳":129}
print(dict1["王琳"])#100  获取
dict1["涛哥"]=454#key不存在,添加
dict1["王琳"]=95#key存在,修改
print(dict1)
print(dict1.pop("艾琳"))#删除并返回对应的value
print(dict1.get("王琳"))#95
print(dict1.get("没人"))#None  get找不到不报错,返回None
print(dict1.keys())#所有键
print(dict1.values())#所有值
print(dict1.items())#所有键值对
for name,score in dict1.items():#遍历字典的标准写法,解包
    print(f"{name}:{score}")

# 案例(P54-55,也是逐日表W1周四的动手任务):词频统计
text="the quick brown fox jumps over the lazy dog the fox"
counts={}
for word in text.split():
    counts[word]=counts.get(word,0)+1#get:有这个词拿次数,没有拿0,再+1
print(counts)
# 顺带:列表去重一行(list顺序会变,set无序)
numlist=[1,2,2,3,3,3]
print(list(set(numlist)))



