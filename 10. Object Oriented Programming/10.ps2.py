#Write a class “Calculator” capable of finding square, cube and square root of a number.

class calculator :

    def __init__(self , n):
        self.n =n
    
    def square(self):
        print(f'The square of{self.n} is  {self.n*self.n} ')

    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The Sqaure root of {self.n} is {self.n**1/2}")

    
number = calculator(4)
number.square()
number.cube()
number.squareroot()