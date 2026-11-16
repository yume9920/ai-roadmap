#参数类型
# 普通参数:数字,布尔,字符串,列表,元组,集合,字典/
# def add (x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(1,2,add))

# 匿名函数
# lamba 参数列表:函数体
# 声明比较简单的函数
lambda:print("--------")
lambda x,y:x+y
#函数体只能是单行的表达式
#无法直接调用
# 赋值给变量调用
out_line=lambda:print("--------")
edd=lambda x,y:x+y
#函数简单且只在一个地方使用,常作为高阶函数的参数使用

# ==========================================================
# 以下补充：把上面的注释变成能跑的代码（P67–68，你已经看到）
# 递归 P69–70 还没看，不在这里，等看完视频再写
# ==========================================================

# P67 函数作参数：calc 自己不决定做什么，由传进来的函数决定
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def calc(x, y, oper):
    return oper(x, y)

print(calc(1, 2, add))        # 3
print(calc(1, 2, subtract))   # -1
print(calc(1, 2, multiply))   # 2
# 同一个 calc，只换第三个参数就换一种运算，这就是把函数当参数的价值

# P68 lambda：上面那种只有一行的函数，可以不起名字直接写
# 你原稿第 17、18 行的裸 lambda 不赋值也不调用，等于白写，不会有任何输出
# 正确用法 1：赋值给变量，之后和 def 定义的函数一样用
f = lambda x, y: x + y
print(f(3, 4))                # 7

# 正确用法 2：直接当实参传进去，这才是 lambda 的主场
print(calc(3, 4, lambda x, y: x ** y))   # 81

# lambda 的函数体只能是一个表达式，不能有 if / for / 赋值语句
# 下面这样是 SyntaxError，保持注释：
# g = lambda x: if x > 0: return x

# 什么时候用 def：逻辑多行、要复用、要写 docstring
# 什么时候用 lambda：只用一次、就一个表达式、懒得起名字

