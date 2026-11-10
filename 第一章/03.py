# match模式匹配
# day = input("请输入现在星期几(1-7):")
# match day:
#     case "1":
#         print("周一工作日")
#     case "2"|"3":
#         print("周二三上学日")
#     case _:
#         print("休息休息都休息")


# num1=float(input("请输入第一个数"))
# num2=float(input("请输入第二个数"))
# oper=input("请输入运算符")
# match oper:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/" if num2!=0:
#         print(f"{num1}/{num2}={num1/num2}")
#     case _:
#         print("错误")

# while 条件表达式:(True时)
    # 循环体语句1
    # 循环体语句2
    # ......
# else:
      # 条件为false时执行的东西

# i=0
# while i<10:
#     print("666")
#     i+=1
# else:
#     print("不6了")

# total=0
# i=1
# while i<=100:
#     if i%2==0:
#         total=total+i#total+=i
#     i+=1
# print(f"一到一百偶数之和为{total}")
# while循环是通过条件判断是否进入下一次循环,而for循环是一种轮询遍历机制,对一批内容进行逐个处理

# for 元素 in 待处理的数据集:
#     循环体代码
# else:
#     循环结束时执行的代码

# msg=input("请输入字符串:")
#
# for s in msg:
#     print(f"元素:{s}")
# else:
#     print("遍历结束")
# # while是条件循环,for主要针对已知元素群

# total=0
# for i in range(1,101):
#     if i%2!=0:
#         total+=i
# print(f"一到一百奇数合为{total}")

# total=0
# for i in range(1,101,2):
#     total+=i
# print(f"一到一百奇数合为{total}")

#嵌套
# m=int(input("请输入长方形的长度"))
# n=int(input("请输入长方形的宽度"))#shift加回车快速创建新的一行
# for i in range(n):
#     for s in range(m):
#         print("*",end="")
#     print()
 #print语句默认自带换行效果 end表示一次输出以什么结束

# 打印九九乘法表

# for i in range(1,10):
#     for s in range (i,10):
#         print(f"{i}x{s}={i*s}",end="  ")
#     print()    自己写的

# for i in range(1,10):
#     for s in range (1,i+1):
#         print(f"{i}x{s}={i*s}",end="\t")
#     print()      答案

# import random
# random_number=random.randint(1,100)#生成随机数
#
# while True:
#     num = int(input("请输入一个数字:"))
#     if num>random_number:
#         print("你猜的数字大了")
#     elif num<random_number:
#         print("你猜的数字小了")
#     else :
#         print("恭喜你你猜对了")
#         break    自己写的
