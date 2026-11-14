# def 函数名(参数列表):
#     函数体
    # ........
    # return 返回值
# 参数列表和返回值可有可无
# 调用:函数名(参数)

def out_line():
    print('--------------')

def circle_area(r):
    """
    该函数用来根据圆的半径
    计算圆的面积和周长
    """
    area=3.14 * r ** 2
    long=2 * r * 3.14
    return area,long#多个返回值封装到元组里
c_area=circle_area(2.4)
print(c_area)
# 定义时用的参数是形参只在函数内部使用
area,long=circle_area(2.43)
print(area)
print(long)
#也可ctrl加左键打开说明
help(circle_area)

#函数调用遵循栈结构,后进先出
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")
def function_b():
    print("b ... before")
    function_c()
    print("b ... after")
def function_c():
    print("c...")
function_a()

# ===== 以下补充 P57–62 里稿子没体现的关键规则（不含函数进阶 P63–70）=====

# P59: return 有两个作用 —— ① 带出结果 ② 立刻结束函数
def check_age(age):
    if age < 0:
        return "年龄不合法"      # 提前 return，下面的 print 这次不会执行
    print("校验通过")            # 只有 age >= 0 时才会走到
    return "合法"
print(check_age(-5))            # 只输出"年龄不合法"
print(check_age(18))            # 输出"校验通过"再输出"合法"

# P59: 没有 return 的函数，返回值固定是 None（不是"什么都没有"）
def say_hi():
    print("hi")
x = say_hi()
print(x)                        # None
print(x is None)                # True

# P59: 多个返回值实际是一个元组，可以直接当元组用
print(type(circle_area(2.4)))   # <class 'tuple'>
print(circle_area(2.4)[0])      # 也能按下标取，但解包更清楚

# P58: 函数必须先定义、后调用；形参和实参个数必须对齐
# say_hi(1)              # 多传 → TypeError
# circle_area(2.4, 3)    # 多传 → TypeError
# circle_area()          # 少传 → TypeError
# 上面三行只作示范，取消注释就会报错，所以保持注释状态

