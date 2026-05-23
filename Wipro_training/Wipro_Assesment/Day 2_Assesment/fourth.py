# create a dictionary and add your name , age , and hobby into it and print
self = {'name': 'Ananya', 'age': 34 , 'hobby': 'gym'}
print(self)
# access and print the value associted with your name in the disctionary
print(self["name"])
# add new key value as your fav food then update the values for the favv hobby  then update it
self['food'] = 'pizza'
self['hobby'] = 'Badminton'
# print all the keys and all the values saperatly
print(self.keys())
print(self.values())
# remove the age key paair value and print
self.pop('age')
print(self)