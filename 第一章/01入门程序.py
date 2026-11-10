
print("hallo world")
print("hallo python")
# ctrl加/可以快速注释
# shift加alt加逗号是缩小,句号是放大
# 俩代码写到一行要加分号
print("hallo python");print("hallo world")
print("------------------")
# .venv是环境信息.idea是配置信息
# --------------------------------------------------------------------------------------------

print(3.1415926)
print(True)
print("遥遥领先")
print(None)
# 整数类型int
# 浮点数(小数float)
# bool类型(True False 1和0,其实也算int)
# str字符串,用""
# None空值
print(True+4-False)


# 变量是存储单个数据的容器,一般吧经常变化的数据存在变量
num=111#变量名=变量值
播放量=23.1
print(播放量)
播放量=播放量+10
print(播放量)
num="ok"
print(num)
num=True
print(num)
# 项目中一般只用变量存储一种数据类型

base=20.7
new=50
print("未来的播放数量",base+2*new)
# ctrl+d快速复制一行

base,new=1,2
print(base,new)
# 一个变量存储一个值且必须赋值后才能使用

# 标识符是函数,变量,类,的名字,字母数字下划线构成,不能数字开头,区分大小写
a=1
b=2
a,b=b,a
print(a,b)

# type()查看数据类型
print(type(播放量))
print(type("nihao"))
print(type(True))
print(type(None))
print(type(2))

# isinstance(播放量,int)判断是否是指定的数据类型
print(isinstance(播放量,int))

#字符串定义
# 单双三引号定义三引号为多行字符串
s1="""
一个标点,字母
或者汉字都是一个字符
是这样的"""
print(s1)

s2='啦啦啦'
print(s2)
# 字符串内要出现需要转义字符\'是单引号,\"是双引号,\n是换行,\t是制表符,缩进一个tab的大小
msg='it\'s very good'
print(msg)
print("欢迎大家来到这里\n\t那简直是太搞笑了")

print("哈利波特"+s1+","+s2)
#字符串的拼接
s3="nis"   "yige" "zhutou"
print(s3)

str(播放量)
# 将其转化为字符串类型

# 占位符%s,可以自动转为字符串
print("大家好,我是%s,今年%s岁了"%(name,age))
# 也可以用f"内容{变量/表达式}"来完成快速格式化
print(f"大家好,我是{name}")
