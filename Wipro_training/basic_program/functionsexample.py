# first will come the functions
# then dirver (driver is like a main in java)
# function
# def add(n1 , n2):
#     return n1 + n2
#
# def sub(n1 , n2):
#     return n1 - n2
#
# def mul(n1 , n2):
#     return n1 * n2
#
# def div():
#     pass
#
# # driver
# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
# result = add(num1 , num2)
# print(result)
# result = sub(num1 , num2)
# print(result)
# result = mul(num1 , num2)
# print(result)


# def sub(n1 , n2):
#     print('n1', n1)
#     print('n2' , n2)
#     return n1 - n2
#
# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
# result = sub(n2 =num2 ,n1 =  num1)
# print(result)

# def add(nums):
#     sum =0
#     for n in nums:
#         sum += n
#     return sum
#
# number = list()
# count = int(input("How many numbers "))
# for _ in range(1 , count+1):
#     number.append(int(input("no: ")))
# print(add(number))
#
# def add(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#         retrun sum
#
# print(add(5,6,9))
# print(add(5,6,9))

# def add(n1 , n2, n3=10):
#     return n1 + n2 + n3
#
# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
# print(add(num1 , num2))
# print(add(num1 , num2 , n3= 100))

# lambda funnction

#
# num1 = int(input("Enter the number"))
# num2 = int(input("Enter the number"))
#
# add = lambda n1 , n2 : n1 + n2
# print(add(num1 , num2))
#
# number = [1,2,3,4,5]
#
# sq = lambda nums : [num * num    for num in nums]
# print(sq(number))
#
#
# number = [1,2,3,4,5]
#
# sq = lambda nums : [num * num    for num in nums]
# print(tuple(sq(number)))


# number = [1,2,3,4,5,6,7,8,9,10]
#
# sq = lambda nums : [num * num    for num in nums if num%2 ==0]
# print(sq(number))

