def average(nums):
    return sum(nums)

num1 = input('Enter the list').split()
total = 0
for i in num1:
    total = total + int(i)

print(total)