#Write a program to find whether a given username contains less than 10 characters or not.

user_name= input('Create a user name :- ')

size = len(user_name)

if size>10 :
    print('Username is greater than 10')
else : print('Perfect')