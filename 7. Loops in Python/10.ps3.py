#Write a program to find whether a given number is prime or not.

n = int(input("Enter The Number:- "))

for i in range(2,n):
    if n%i == 0:
        print(f"{n} is Not a Prime Number")
        break
else : print(f"{n} is a Prime Number")        

    
