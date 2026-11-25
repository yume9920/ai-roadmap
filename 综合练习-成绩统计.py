# 综合练习：成绩统计小程序
# 语法范围：P1–68（变量、分支、循环、列表、字典、函数、f-string、推导式）
# 刻意不用：文件读写、csv、类、模块导入 —— 这些都还没学，留到后面
# 运行：python 综合练习-成绩统计.py

students = [
    {"姓名": "张三", "语文": 88, "数学": 92, "英语": 79},
    {"姓名": "李四", "语文": 75, "数学": 83, "英语": 90},
    {"姓名": "王五", "语文": 91, "数学": 68, "英语": 85},
    {"姓名": "赵六", "语文": 62, "数学": 77, "英语": 71},
]

SUBJECTS = ("语文", "数学", "英语")


def average(stu):
    """算一个学生的平均分。"""
    scores = [stu[s] for s in SUBJECTS]   # 列表推导式，P42 学过
    return sum(scores) / len(scores)


def show_all():
    """列出全部学生。"""
    print("姓名    语文  数学  英语  平均")
    for stu in students:
        print(stu["姓名"], stu["语文"], stu["数学"], stu["英语"], f"{average(stu):.1f}")


def find_student(name):
    """按姓名查找，找到返回字典，没找到返回 None。"""
    for stu in students:
        if stu["姓名"] == name:
            return stu
    return None


def ranking():
    """按平均分从高到低排名。"""
    items = []
    for stu in students:
        items.append([average(stu), stu["姓名"]])
    items.sort(reverse=True)              # 二元列表默认按第一个元素排，即平均分
    i = 1
    for avg, name in items:               # 解包，P41 学过
        print(i, name, f"{avg:.1f}")
        i += 1


def subject_stats():
    """统计每科的最高、最低、平均。"""
    for s in SUBJECTS:
        vals = [stu[s] for stu in students]
        print(s, "最高", max(vals), "最低", min(vals), "平均", f"{sum(vals) / len(vals):.1f}")


def add_student():
    """从键盘录入一个新学生。"""
    name = input("姓名：")
    new = {"姓名": name}
    for s in SUBJECTS:
        new[s] = int(input(s + "："))
    students.append(new)
    print("已添加", name)


def delete_student():
    """按姓名删除学生，用 find_student 的返回值判空。"""
    name = input("要删除的姓名：")
    stu = find_student(name)
    if stu is None:
        print("没找到", name)
    else:
        students.remove(stu)
        print("已删除", name)


def failing():
    """列出有不及格科目的学生。"""
    found = False
    for stu in students:
        bad = []
        for s in SUBJECTS:
            if stu[s] < 60:
                bad.append(s + str(stu[s]))
        if len(bad) > 0:
            print(stu["姓名"], "不及格：", " ".join(bad))
            found = True
    if not found:
        print("没有人不及格")


def menu():
    """菜单循环。"""
    while True:
        print("")
        print("1 全部学生   2 查学生   3 排行榜   4 科目统计")
        print("5 添加学生   6 删除学生   7 不及格名单   0 退出")
        choice = input("选一个数字：")
        if choice == "1":
            show_all()
        elif choice == "2":
            name = input("要查的姓名：")
            stu = find_student(name)
            if stu is None:
                print("没找到", name)
            else:
                print(stu, "平均", f"{average(stu):.1f}")
        elif choice == "3":
            ranking()
        elif choice == "4":
            subject_stats()
        elif choice == "5":
            add_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            failing()
        elif choice == "0":
            print("再见")
            break
        else:
            print("没有这个选项，重新输")


menu()
