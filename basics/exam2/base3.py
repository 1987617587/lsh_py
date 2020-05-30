# 12、写一个学生类， 设计 6 个成员变量用于表示学生的信息（学号、班级、名字、语文成绩、数学成绩、英语成绩）
# ；然后定义一个容器存储一个班的学生（3人），请依次输入每个学生的成绩，输入完成后，
# 根据学生的3 门功课的成绩进行降序排序（冒泡排序）。（10分）

def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


class Student:

    def __init__(self, stu_num, cls='一班', name=None, c_score=None, m_score=None, e_score=None) -> None:
        super().__init__()
        self.stu_num = stu_num
        self.cls = cls
        self.name = name
        self.c_score = c_score
        self.m_score = m_score
        self.e_score = e_score

    def __str__(self) -> str:
        return f"学号:{self.stu_num}、班级:{self.cls}、名字:{self.name}、" \
            f"语文成绩:{self.c_score}、数学成绩:{self.m_score}、英语成绩:{self.e_score}"

    @classmethod
    def score_sort(cls):
        num = input("请选择排序类型：1.语文成绩、2.数学成绩、3.英语成绩(1-3):")
        if num == "1":
            arr1.sort(key=lambda s: s.c_score)
        if num == "2":
            arr1.sort(key=lambda s: s.m_score)
        if num == "3":
            arr1.sort(key=lambda s: s.e_score)
        for i in arr1:
            print(i)


arr1 = [
    Student("120", "一班", "张三", 99, 88, 55),
    Student("223", "一班", "Task13", 69, 68, 85),
    Student("125", "一班", "王五", 92, 78, 55)

]
if __name__ == '__main__':
    Student.score_sort()
