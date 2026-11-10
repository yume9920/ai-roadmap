# a=input("请输入第一个数:")
# b=input("请输入第二个数:")
# a,b=b,a
# print(f"两个数分别是{a}和{b}")


# r=float(input("请输入圆的半径:"))
# l=2*3.14*r
# s=3.14*r**2
# print(f"圆的周长为{l:.2f},面积为{s:.2f}")

# be=int(input("请输入秒数:"))
# x=be//3600
# xe=be%3600
# y=xe//60
# z=xe%60
# print(f"时间为{x}时{y}分{z}秒")


# while True:
#     score = int(input("请输入你的分数:"))
#     if 100>=score>=75:
#         print("你是优秀")
#         break
#     elif 75>score>=60:
#         print("你是良好")
#         break
#     elif 60>score>=0:
#         print("你是差")
#         break
#     else:
#         print("输入分数错误请重新输入:")

# a=int(input("请输入第一个数"))
# b=int(input("请输入第二个数"))
# c=int(input("请输入第三个数"))
# if a>b and a>c:
#     print(f"{a}最大")
# elif b>a and b>c:
#     print(f"{b}最大")
# else:
#     print(f"{c}最大")

# use=input("请输入运算符")
# a=int(input("请输入第一个数"))
# b=int(input("请输入第二个数"))
# match use:
#     case"+":
#         print(f"{a}+{b}={a+b}")
#     case"-":
#         print(f"{a}-{b}={a - b}")
#     case"*":
#         print(f"{a}*{b}={a * b}")
#     case"/":
#         if b==0:
#             print("除数不能为零")
#         else:
#             print(f"{a}/{b}={a / b}")

# total=0
# for i in range(0,100):
#     if i%2==0:
#         total+=i
# print(f"一到一百偶数和为:{total}")
#
# s=0
# for q in range(0,100,2):
#     s+=q
# print(f"一到一百偶数和为{s}")

# n=int(input("请输入数n:"))
# total=1
# for i in range (1,n+1):
#     total*=i
# print(f"{n}的阶乘为{total}")

# for i in range(1,10):
#     for s in range(1,i+1):
#         print(f"{s}x{i}={i*s}",end="\t")
#      print()

# n = 4
# for i in range(1, n + 1):              # 上半部分 + 中线
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):          # 下半部分，倒着来
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n=4
# for i in range(1,n+1):
#     print("*"*i)

# n=4
# for s in range(1,n+1):
#     print(" "*(n-s)+"*"*s+" "*(n-s))

# a=1
# b=1
# c=1
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             num = 100 * a + 10 * b + c
#             if (a**3+b**3+c**3)==num:
#                 print(f"{num}为水仙花数")

# i=int(input("请输入一个数来判断:"))
# for s in range(2,i):
#     if i%s==0:
#         print("这个数不是素数")
#         break
# else:
#     print("这个数是素数")

# a,b=1,1
# for i in range(20):
#     print(f'{a}')
#     a,b=b,a+b

# n = int(input("输入一个正整数："))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10     # 左移一格，把末位接上去
#     n = n // 10                 # 丢掉已经用过的末位
#
# print(rev)

# day=1
# for i in range(1,10):
#     day=(day+1)*2
# print(f"第一天有{day}个桃子")


# for i in range(20):
#     for s in range(33):
#         c=(100-i-s)
#         if (5*i+3*s+c/3)==100 and (i+s+c==100):
#             print(f"公鸡{i}只,母鸡{s}只,小鸡{c}只")

