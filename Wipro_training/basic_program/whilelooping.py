# # print the natural number
# num = int(input("Enter the number"))
# value = 1
# while value <= num:
#     print(value)
#     value += 1
num = int(input("Enter the numnber"))
count = len(num)
ni = int(num)
sum =0
comparison = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni//10

if comp == sum:
    print('arm')
else:
    print('na')