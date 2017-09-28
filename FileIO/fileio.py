import string
import re
from random import *
from datetime import datetime
from Student import Student


class Newstudent(Student):

    def __init__(
        self, nm, sname, bdate, gr,
            gd, spec, cs, lg, passwd):
        super(Newstudent, self).__init__(nm, sname, bdate, gr,
            gd, spec, cs)
        self.__login = lg
        self.__password = passwd

    @staticmethod
    def makeExSt(args):
        args = args.split(':::')
        if args[3] == 'M':
            args[3] = 'Male'
        else:
            args[3] = 'Female'
        args[4] = int(args[4])
        args[6] = int(args[6])
        login = ('' + args[0][0] + args[1]).lower()
        allchar = string.ascii_letters + string.digits
        password = ''.join(choice(allchar) for x in range(randint(6, 9)))
        return Newstudent(args[0], args[1], args[2], args[3], args[4],
                               args[5], args[6], login, password)

    @property
    def password(self):
        return self.__password

    @property
    def login(self):
        return self.__login

    def __str__(self):
        res = "Student: "
        res += self.name + ' ' + self.surname + ' | ' + self.birthdate + ' | '
        res += self.gender + '  |  ' + str(
            self.grade) + '   |   ' + self.speciality + ' | ' + str(
                self.coursenumber) + ' | ' + self.login + ' | ' + self.password
        return res

file_open = open("students.dat", "r")
student_list = []
for line in file_open.readlines():
    student_list.append(Newstudent.makeExSt(line))
file_open.close()

file_out = open("students0.dat", "a")
for student in student_list:
    file_out.write(str(student) + '\n')
file_out.close()
