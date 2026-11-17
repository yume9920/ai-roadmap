# name=input("请输入您的姓名:")
# print(f"欢迎您{name}")
# # 输入的全都是字符串

# total=10000
# out=input("请输入取款金额:")
# full=total-int(out)
# print(f"您的余额为:{full}")

 # 算数运算符:*乘法,  /除法 (浮点数),   //整除(整数部分),    %取余(求模),                **幂指数n的x次方
 # 优先级:幂指数大于乘除取余再大于加减
# x=float(input("请输入x:"))
# y=float(input("请输入y:"))
# print("x+y=",(x+y))
# print("x-y=",(x-y))
# #精度出现损失,二进制不能准确表示所有小数,浮点数运算可能损失精度

# # 赋值运算符
# num+=2是num=num+2
# num-2是num=num-2
# num**2是num=num**2
# 其他所有运算符同理

# 比较运算符
# ==等于   !=不等于   >大于    >=大于等于      <小于    <=小于等于,返回值是一个布尔值
# a=1
# b=2
# print(a==b)
# print(a>=b)
# print(a<=b)
# print(a!=b)

# 逻辑运算符
# and 左右两边都为true,结果才为true
# or 两边有一个结果为true,结果为true
# not 取反,true变false,false变true
# num=int(input("请输入一个整数:"))
# print(10<=num and num<=20)
# print(f"{num}在10到20之外",10>=num or num>=20)

# if 要判断的条件:(结果是布尔):
#     条件成立时要执行的操作
# score=699
# if score>670:
#     print("我要上清华")

# score=int(input("你考了多少分:"))
# if score>700:
#     print("我靠你真牛逼")

# if:
#
# else:
#     条件不成立时执行

# year=int(input("请输入年份"))
# if year%100==0 and year%400==0:
#     print("这年是闰年")
# elif year%100!=0 and year%4==0:
#     print("这年是闰年")
# else :
#     print("这年不是闰年")
# 或者
# if (year%100!=0 and year%4==0) or(year%400==0)
# elif可以写多个
# a=int(input("请输入边"))
# b=int(input("请输入边"))
# c=int(input("请输入边"))
# if a+b>c  and a+c>b and b+c>a:
#     if a==b and b==c:# pass #空语句,语法占位
#         print("构成等边三角形")
#     elif a==b or b==c or a==c:
#         print("构成等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print(f"{a} {b} {c}不能构成三角形")

# ==================== 可运行验证版（用固定值，不卡input） ====================
print("=" * 40)
# 算术运算符
x, y = 7, 2
print("算术:", x + y, x - y, x * y, x / y, x // y, x % y, x ** y)
print("优先级:", 2 ** 3 * 2, "=16(幂先算)")
print("精度:", 0.1 + 0.2, "≠0.3")

# 赋值运算符（注意：原稿第20行写的'num-2是num=num-2'漏了等号，正确是 -=）
num = 10
num -= 2          # 等价于 num = num - 2
num **= 2
print("赋值后num:", num)

# 比较运算符，返回布尔值
a, b = 1, 2
print("比较:", a == b, a != b, a >= b, a <= b)

# 逻辑运算符（原稿第39行'10>=num or num>=20'边界会误判，正确写法如下）
num = 25
print("在10-20之外:", num < 10 or num > 20)
print("链式比较:", 10 <= 15 <= 20)
print("not取反:", not (num < 10 or num > 20))

# if / elif / else —— 闰年
for year in (1900, 2000, 2024):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")

# 嵌套 if —— 三角形分类
a, b, c = 3, 3, 4
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不能构成三角形")