# class EmplopyeeDetails:
#     def __init__(self , empno , ename , basicpay):
#         self.empno = empno
#         self.ename = ename
#         self.basic_pay = basicpay
#         self.da = 20.0
#         self.hra = 10.0
#         self.pf = 5,5
#
#     def calculate_allowance(self):
#         allowance = (self.basic_pay * self.da / 100) + (self.basic_pay * self.hra / 100)
#         return allowance
#     def calculate_deduction(self):
#         deduction = (self.basic_pay * self.da / 100)
#         return deduction
#     def calculate_netsal(self):
#         netsal = self.basic_pay + self.calculate_allowance() - self.calculate_deduction()
#         return netsal
#

# class EmplopyeeDetails:
#     def __init__(self , empno , ename , basicpay):
#         self.__empno = empno
#         self.__ename = ename
#         self.__basic_pay = basicpay
#         self.__da = 20.0
#         self.__hra = 10.0
#         self.__pf = 5,5
#
#
#     def get_empno(self):
#         return self.__empno
#
#     def set_empno(self, eno):
#         self.__empno = eno
#
#     def calculate_allowance(self):
#         allowance = (self.__basic_pay * self.__da / 100) + (self.__basic_pay * self.__hra / 100)
#         return allowance
#     def calculate_deduction(self):
#         deduction = (self.__basic_pay * self.__da / 100)
#         return deduction
#     def calculate_netsal(self):
#         netsal = self.__basic_pay + self.calculate_allowance() - self.calculate_deduction()
#         return netsal
#

class EmplopyeeDetails:

    @property
    def get_empno(self):
        return self.__empno

    @empno.setter
    def set_empno(self, eno):
        self.__empno = eno

    @property
    def ename(self,name):
        return self.__ename

    @ename.setter
    def ename(self,name):
        self.__ename = name

    @property
    def basicpay(self):
        return self.__basicpay
    @basicpay.setter
    def basicpay(self, bp):
        self.__basic_pay = bp

