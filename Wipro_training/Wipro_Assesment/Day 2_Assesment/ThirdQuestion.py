# # create a set of 5 unique colors print the set
# color = {'black' , 'yellow', 'green'}
# print(color)
# # Add a new color to the set , then try removing an existing color. Print the update
# color.add('red')
# color.remove('yellow')
# print(color)
# # create another set with 3 different color . Find the interaction , union, and difference btween them
# color2 = {'brown','black', 'grey'}
# print(color & color2)
# print(color - color2)
# print(color | color2)
# # check the specific color in the set and print the result
# sp = input('Enter the color you want: ')
# if sp == color:
#     print('Found:', sp)
# else:
#     print('Not found')
# convert a list of fruits (with some duplicates) into a set and print the unique once
fruits = ['apple','banana','orange', 'apple', 'mango', 'banana']
result = []
for i in fruits:
    if i not in result:
        result.append(i)
print(result)