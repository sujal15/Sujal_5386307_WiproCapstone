# write a program that uses a for loop to count thr number of vowels in the given string
str = input("EEnter:")
count =0
for ch in str:
    if ch in 'a,e,i,o,u':
        count += 1
print(count)