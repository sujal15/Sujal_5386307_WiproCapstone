# Write a program that uses loop for to print number from 1-10, but skips printing the number 5(use continue) and stop the loop if the number is reached
for i in range(1,11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)