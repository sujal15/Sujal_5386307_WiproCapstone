# create a tuple with the name of 3 different cities you'd like to visit. Print the tuple
city = ('Kedarnath' , 'Vashnodevi' , 'Dwarika')
print(city)
# Access and print the first and last elemnts in the tuple
print(city[0], city[2])
# create another tuple with 2 more cities. Concatenate both the tuples and print the tuple
city2 = ('Banaras' , 'Ujjain')
print(city + city2)
# try changing one elemnt in the tuple and see what happends
# city[1] = 'Haldwani'
# unpack the elemnt in the seprate variables and print them
for i in city:
    print(i)
