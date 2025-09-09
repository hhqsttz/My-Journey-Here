import json


class Employee(object):
    """员工类"""
    def __init__(self, name, gender, age, mobile_number, is_leave = False):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = is_leave
        self.leave = "离职" if self.is_leave else "在职"
    def __str__(self):
        return "-"*60+"\n"+f"姓名:{self.name}\n年龄:{self.age}\n性别:{self.gender}\n电话号码:{self.mobile_number}\n在职情况:{self.leave}"+"\n"+"-"*60

if __name__ == '__main__':
    a = Employee("gbk","男","18","13409136983",is_leave =True)
    # print(a.__dict__)
    # print(vars(a))
    print(a)
    c=[1,2]
    print(str(c))
    print(json.dumps(c, ensure_ascii=False))
