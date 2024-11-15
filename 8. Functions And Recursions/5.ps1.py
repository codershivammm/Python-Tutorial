#Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = int(input("Enter the number:- "))
b = int(input("Enter the number:- "))
c = int(input("Enter the number:- "))

gr = greatest(a,b,c)
print(f"The greatest Number among {a} , {b} , {c} is {gr}")