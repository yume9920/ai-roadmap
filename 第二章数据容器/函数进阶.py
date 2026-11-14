# 函数外定义的是全局变量,在函数内外都能访问
# 局部变量只能在函数内使用
# global关键字可以在函数内使用全局变量
# num=100
# def i (e):
#     global num
#     num=10000
# c=i(1)
# print(num)#global生效num被改成10000
#global主要用在程序状态,配置,计数器等


# 传参方式:
# 位置传参:调用函数时参数的顺序与定义时完全一致
# 关键字传参:键=值的方式
# 若要混用,关键字参数必须在位置参数之后

 #默认参数:定义函数时为参数提供默认值
 # def where(name,age,city='北京'):
     # 默认要放在其他的后面,不赋值就输出默认值


#不定长参数(可变参数)(参数数量不确定时使用)
# 形参前面加个*,基于位置传递的不定长参数
# 会封装带一个元组里面(位置传入)
# def calc_data(*args,**kwargs):
#     mini_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return mini_data,max_data,round(avg_data,1)
# print(calc_data(1,2,33,45,43453,78,99))
# 关键字传递的用**,封装在一个字典里面

def calc_data(*args,**kwargs):
    mini_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    # print(kwargs)
    if kwargs.get("round") is not None:
        avg_data=round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值是:{mini_data},最大值是{max_data},平均值是{avg_data}")
    return mini_data,max_data,avg_data
print(calc_data(1,2,33,45,43453,78,99,round=3,print=True))

# ==========================================================
# 以下补充：把上面的注释变成能跑的代码（P63–P66，你已经看过）
# ==========================================================

# --- P63 变量作用域 ---
num = 100
def change_global():
    global num
    num = 10000
change_global()
print(num)                       # 10000，global 才真的改了外面那个

num = 100
def shadow():
    num = 10000                  # 没写 global：这只是新建的局部变量
    return num
print(shadow(), num)             # 10000 100  外面那个没变

# --- P64 传参方式 ---
def where(name, age, city):
    return f"{name} {age}岁 {city}"
print(where("小明", 18, "北京"))                  # 位置传参：按顺序对号入座
print(where(city="上海", name="小红", age=20))     # 关键字传参：顺序随便
print(where("小刚", 20, city="深圳"))             # 混用：位置必须排在关键字前面
# print(where(name="小A", 20, "北京"))            # SyntaxError，整份文件都编译不过，保持注释

# --- P65 默认参数 ---
def where_default(name, age, city="北京"):
    return f"{name} {age}岁 {city}"
print(where_default("小A", 18))                  # 不传 city，用默认值
print(where_default("小B", 19, "广州"))           # 传了就覆盖
# 默认值必须写在最后：def f(city="北京", name) 是 SyntaxError

# --- P66 不定长参数 ---
def show_args(*args, **kwargs):
    print(type(args), args)      # <class 'tuple'> (1, 2, 3)
    print(type(kwargs), kwargs)  # <class 'dict'> {'name': '小A', 'age': 18}
show_args(1, 2, 3, name="小A", age=18)

# 你 calc_data 里两种判断方式不一样，这里看差别
print(calc_data(1, 2, 3, round=0))   # round=0 时 is not None 成立 → 照样取整
# 若写成 if kwargs.get("round")，0 会被当成假，这一轮就跳过取整了

# *args 一个都不传时，min() 会 ValueError、除法会除零，加一层防护
def calc_data_safe(*args, **kwargs):
    if not args:
        return "没有数据"
    mini_data, max_data = min(args), max(args)
    avg_data = sum(args) / len(args)
    digits = kwargs.get("round")
    if digits is not None:
        avg_data = round(avg_data, digits)
    return mini_data, max_data, avg_data
print(calc_data_safe(1, 2, 3, 4, round=2))
print(calc_data_safe(round=2))

# ==========================================================
# 以下 P67–P70 你还没看，属于提前整理：看完视频再回来看，现在不用做
# ==========================================================

# P67 函数本身也能当参数传
def apply(func, x, y):
    return func(x, y)
def add(a, b):
    return a + b
print(apply(add, 3, 5))                  # 8

# P68 lambda：一行的小函数，不用起名字
print(apply(lambda a, b: a * b, 3, 5))  # 15

# P69 递归：函数自己调自己，必须有出口
def factorial(n):
    if n <= 1:                           # 出口
        return 1
    return n * factorial(n - 1)
print(factorial(5))                      # 120

# P70 案例2：看完视频再补
