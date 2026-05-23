from oopsconcept.Teacher import Teacher
from oopsconcept.student import Student
from oopsconcept.studentgrade import StudentGrade

cc = int(input("C Code: "))
cn = input('C Name: ')
ci = input("City: ")
rno = int(input())
sn = int(input())
m1 =int(input())
m2 = int(input())
m3 = int(input())
eid = int(input())
tn = input()
dpt = input()
bp = float(input())

# project = College(ccode=cc , cname = cn , ccity = ci)
# project.welcome_message()
# project.display_college_details()

project = StudentGrade(ccode = cc, cname = cn, ccity = cc,
                  rno =rno, sname =sn, m1 =m1, m2=m2 , m3=m3)

print(f'Roll No: {project.rollno} \t '
      f'Name: {project.stuname}'
      f'total: {project.calculate_total()}'
      f' Average: {project.calculate_average()}')
print(f'Result: {project.result} \t Grade : {project.grade}')
teach = Teacher(cc, cn, ci, eid, tn, dpt, bp)
print(f'eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')