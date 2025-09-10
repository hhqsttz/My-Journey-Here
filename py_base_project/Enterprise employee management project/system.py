import json
import os
import sys
from employee import Employee


class EmployeeManagerSystem(object):
    #创建单例类
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(EmployeeManagerSystem,cls).__new__(cls)
        return cls._instance

    #初始化
    def __init__(self):
        self.employees_file = "employees.json"
        self.employees_backup_file = "employees_backup.json"
        self.load_employee_from_file()

    def main(self):
        """员工管理系统入口"""
        while True:
            self.show()
    # 返回到界面窗口
    @staticmethod
    def stop():
        input("返回到视图窗口，请按回车键。")
    # 1.显示系统欢迎界面
    def show(self):
        print("欢迎来到企业管理项目窗口")
        print("-"*60)
        print('1.增加员工')
        print('2.删除员工')
        print('3.修改员工')
        print('4.查看员工')
        print('5.展示所有员工')
        print('6保存员工数据')
        print('7.退出系统')
        print("-" * 60)
        a = int(input('请输入你想选择的业务:'))
        match a:
            case 1 :
                self.add_emp()
                self.stop()

            case 2 :
                self.del_emp()
                self.stop()

            case 3:
                self.update_emp()
                self.stop()

            case 4:
                self.find_emp()
                self.stop()

            case 5:
                for emp in self.employee_list:
                    print(emp)
                self.stop()

            case 6:
                self.save_emp()
                self.stop()

            case 7:
                sys.exit()
            case _:
                print("输入错误！")
    # 2.增加员工
    def add_emp(self):
        print("请输入员工的信息")
        name = str(input("名字："))
        gender = str(input("性别："))
        age = int(input("年龄："))
        mobile_number = int(input("手机号："))
        is_leave = input("是否离职（True/False）：").lower() == "true"
        emp = Employee(name, gender, age, mobile_number, is_leave)
        self.employee_list.append(emp)
        print(emp)
    # 3.删除员工
    def del_emp(self):
        del_name = input("请输入删除的员工名字：")
        for emp in self.employee_list:
            if emp.name == del_name:
                self.employee_list.remove(emp)
                print(f"{del_name},此员工已删除")
                break
        else:
            print("没有找到当前员工")
    # 4.修改员工信息
    def update_emp(self):
        update_name = input("请输入修改的员工名字：")
        for emp in self.employee_list:
            if emp.name == update_name:
                new_name = input('请输入新的姓名（不修改直接回车）：').strip()
                emp.name = new_name if new_name else emp.name

                new_age = input('请输入新的年龄（不修改直接回车）：').strip()
                emp.age = int(new_age) if new_age else emp.age

                new_gender = input('请输入新的性别（不修改直接回车）：').strip()
                emp.gender = new_gender if new_gender else emp.gender

                new_mobile_number = int(input('请输入新的电话号（不修改直接回车）：').strip())
                emp.mobile_number = new_mobile_number if new_mobile_number else emp.mobile_number

                new_is_leave = input('请输入是否离职（False/True）：').lower()=="true"
                emp.is_leave = new_is_leave
                print(f"{update_name},此员工信息已修改")
                break
        else:
            print("没有找到当前员工")
    # 5.查看员工信息
    def find_emp(self):
        find_name = input("请输入查找的员工名字：")
        for emp in self.employee_list:
            if emp.name == find_name:
                print(emp)
            else:
                print("未找到员工信息，是否要创建：")
                a=int(input("是否要创建员工信息：\n是：1\n否：0\n"))
                if a :
                    self.add_emp()
    # 6.保存员工信息
    def save_emp(self):
        # 1.判断备份文件是否存在
        if  os.path.exists(self.employees_backup_file):
            os.remove(self.employees_backup_file)
            print("备份文件以删除")
        if os.path.exists(self.employees_file):
            os.rename(self.employees_file,self.employees_backup_file)
            print("已重新生成备份文件")
        with open(self.employees_file, "w",encoding="utf-8") as f:
            new_list = []
            for emp in self.employee_list:
                new_list.append(vars(emp))
            json.dump(new_list,f, ensure_ascii=False,indent=4)
    #拿取文件对象数据
    def load_employee_from_file(self):

        #
        # 读取员工文件，并且放到一个列表当中
        # :return:
        #文件是否存在
        if not os.path.exists(self.employees_file):
            self.employee_list = []
            return
        try:
            f = open(self.employees_file, "r", encoding="utf-8")
            content = f.read().strip()
            self.employee_list = []
            if not content:
                return
            a = json.loads(content)
            for dict in a:
                self.employee_list.append(Employee(dict["name"], dict['gender'], dict['age'], dict['mobile_number']))
        except Exception as e:
            print(f"加载文件时出错: {e}")
            self.employee_list = []
if __name__ == '__main__':
    mm = EmployeeManagerSystem()
    mm.main()


"""
案例思路：
1.实现单例类

2.从文件中获取对象信息，最终返回一个列表
先判断文件存在不，再判断文件中有没有数据，最后都要返回一个列表用来接下来对数据对象的存储

3.使用match函数来匹配业务

4.增删改查操作

5.文件的保存与跟新


案例重要内容
1.实现单例类
2.掌握了文件与json的操作
将对象字典化 vars(py)

json文件数据与python对象的转化
    json数据->py 
        1.文件 json.load(f) 
        2.json字符串 json.loads(json字符串)
    py -> json数据
        1.文件 json.dump(py,f,ensure_ascii=False,indent=4)
        2.字符串 json.dumps(py,ensure_ascii=False,indent=4)
3.输入bool数值可以直接与"true"来进行匹配

"""





