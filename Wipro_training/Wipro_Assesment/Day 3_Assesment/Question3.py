def largest(a , b , c):
    m = max(a , b , c)
    if a ==  b == c:
        return "All the values are equal"
    elif m == a:
        return "a is greater"
    elif m == b :
        return 'b is greater'
    else:
        return "c is greater"

num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number: '))
num3 = int(input('Enter the number: '))
print(largest(num1 , num2 , num3))
