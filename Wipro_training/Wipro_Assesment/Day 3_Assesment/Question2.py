from struct import pack_into


def factorial(n):
    if n < 0:
        print("The given number is negitive")
        return
    result = 1
    for i in range(1 , n+1):
        result = result * i
    return result


num1 = int(input("Enter the number"))
print(factorial(num1))
