from oopsconcept.agecalc import Agecalc
from oopsconcept.myexception import AgeException
age = int(input("Enter the age: "))
age_obj = Agecalc()
try:
    age_obj.voting_age_check(age)
    age_obj.pansion_age_check(age)
except AgeException as e:
    print(e)

else:
    print("Eligible.Move to the next Step!!")