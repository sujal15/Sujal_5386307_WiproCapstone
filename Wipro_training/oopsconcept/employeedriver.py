# #driver
# from oopsconcept.EmployeeDetails import EmplopyeeDetails
#
# eno = int(input("Enter no: "))
# name = input('Emo name: ')
# bp = float(input('basic pay: '))
# employee = EmplopyeeDetails(empno = eno, ename = name , basicpay = bp )
# print('emp no: ' ,employee.empno)
# print('emp name: ' ,employee.ename)
# print('basic pay:' ,employee.basic_pay)
# print('Salary: ' , employee.calculate_netsal())

#driver
# from oopsconcept.EmployeeDetails import EmplopyeeDetails
#
# eno = int(input("Enter no: "))
# name = input('Emo name: ')
# bp = float(input('basic pay: '))
# employee = EmplopyeeDetails(empno = eno, ename = name , basicpay = bp )
# print('emp no: ' ,employee.get_empno())
# print('emp name: ' ,employee.ename)
# print('basic pay:' ,employee.basic_pay)
# print('Salary: ' , employee.calculate_netsal())

from oopsconcept.EmployeeDetails import EmplopyeeDetails

eno = int(input("Enter no: "))
name = input('Emo name: ')
bp = float(input('basic pay: '))
employee = EmplopyeeDetails( eno,  name , bp )
print('emp no: ' ,employee.get_empno())
print('emp name: ' ,employee.ename)
print('basic pay:' ,employee.basic_pay)
print('Salary: ' , employee.calculate_netsal())