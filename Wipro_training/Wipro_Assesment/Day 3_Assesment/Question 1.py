# take a list of numbers as input and print the largest and the smallest numbers in the list
num = list(map(int,input("Enter the number").split()))
largest = num[0]
smallest = num[0]
for n in num:
     if n>largest:
         largest = n
     if n < smallest:
         smallest = n

print(largest)
print(smallest)
#  take a list of names as input and print them in alphabetical order
names = input("Enter string: ")
print("length", len(names))
# take a list of names as input 