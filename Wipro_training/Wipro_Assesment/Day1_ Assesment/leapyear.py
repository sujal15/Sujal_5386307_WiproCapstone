# write a program that takes a year as a input and check if it is a loeap year or not ?
year = int(input("Enter the year: "))
if year % 400 ==0:
    print("It is a leap year")
elif year %100 == 0:
    print("It is Not a leap year")
elif year % 4 == 0:
    print("It is a leap Year")
else:
    print("It is not a leap year ")