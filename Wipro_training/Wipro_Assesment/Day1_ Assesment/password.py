# write a program that takes password as an input and check if the password is strong or not and give him a messsage
password = input("Enter the password")
if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
