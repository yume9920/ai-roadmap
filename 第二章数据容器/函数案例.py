def t (q,w):
    return q*w/2
print(t(1,3))

def count(s):
    """
    统计元音字母的个数
    :param s:
    :return:
    """
    num=0
    for y in s:
        if y in  "aeiouAEIOU":
            num+=1
    return num

print(count("nishiyigedashabishabibenlingqiang"))

 # py的内置函数是用c写的

# ===== 以下补充 P62 案例的通用套路（不含函数进阶 P63–70）=====

# 套路：函数只负责"算"，打印交给调用方
# 这样同一个函数既能打印、也能存起来再参与别的计算
area = t(3, 4)
print(f"底3高4的三角形面积：{area}")

# P61 嵌套调用在案例里的用法：一个函数里调另一个函数
def describe(s):
    return f"「{s}」里有 {count(s)} 个元音字母"
print(describe("hello world"))
print(describe("nishiyigedashabishabibenlingqiang"))

# 把函数的返回值直接传给另一个函数，不用先存变量
print(f"这句话的元音数加 10 是：{count('hello') + 10}")

# 对照：count() 里 num 是函数内部的变量，外面取不到
# print(num)             # NameError，取消注释就会报错
