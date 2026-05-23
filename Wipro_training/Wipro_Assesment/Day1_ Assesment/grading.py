# Write a program that takes a grade (A,B,C,D,F) as input using match-case to print a message corrospondig to a grade/
marks = (input("Enter the grade: "))
match marks:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')
    case 'c':
        print('Average')
    case 'D':
        print('Below Average')
    case 'E':
        print('Fail')
    case _:
        print("Invalid")