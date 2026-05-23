from unittest import result

from oopsconcept.student import Student


class StudentGrade(Student):

     def calculate_result(self):
            if super().mark1 > 40 and super().mark2 > 40 and super().mark3 > 40:
                self.result= 'Pass'
            else:
                self.result = 'Fail'
     def calculate_grade(self):
         self.calculate_result()
        if result == 'Pass':
            avg =super().calculate_average()


            if avg >= 80.0:
                self.grade = 'A'
            elif avg >= 60.0:
                self.grade = 'B'
            elif avg>=40.0:
                self.grade = 'C'
            else:
                self.grade = 'NA'
