# create a list with 5 different types of fruits
fruits = ['apple' , 'banana' , 'mango' , 'orange' , 'watermalon']
print(fruits)
# now add two fruits in the list and remove one from it print the updated
fruits.append('strawberries')
fruits.append('kiwi')
fruits.remove('apple')
print(fruits)
# Access the second and third fruit from the list and print them
print(fruits[1], fruits[3])
# Slice the list to get the first three fruits and print the result
print(fruits[0:3])
# find amd print the length of the list
print(len(fruits))

