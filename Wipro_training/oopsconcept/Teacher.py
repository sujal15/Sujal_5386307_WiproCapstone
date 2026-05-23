from oopsconcept import college
class Teacher(college):
    def __init__(self, ccode, cname, ccity, eid , tn, de, bp):
    super().__init__(ccode, cname, ccity)
    self.empid = eid
    self.tname = tn
    self.dept = de
    self.basicpsy = bp

    def calculate_salary(self):
        return self.basicpsy + (self.basicpsy * 0.2) - (self.basicpsy *0.2) - (self.basicpsy * 0.00)