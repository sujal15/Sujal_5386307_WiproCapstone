from  oopsconcept.myexception import AgeException

class Agecalc:
    def voting_age_check(self, age):
        if age < 18:
            raise AgeException("")
        else:
            return  True

    def pansion_age_check(self, age):
        if age < 60:
            raise AgeException("Not eligible to pension")
        else:
            return True

