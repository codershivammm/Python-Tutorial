#Write a program to calculate the factorial of a given number using for loop. 

#5! = 1 X 2 X 3 X 4 X 5
 
n = int(input("Enter the Number:-"))

product = 1 

for i in range (2, n+1):
    product = product * i

print(f'The factorial of {n} is {product}')
