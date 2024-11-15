# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector :
    
    def __init__(self , x , y ,z) :

        self.x = x
        self.y= y
        self.z = z

    def __add__ (self ,other):
        result = vector(self.x + other.x , self.y + other.y , self.z+ other.z ) #  + Operator Automatically Calls __add__ function
        return result

    def __mul__(self ,other):
        result = vector(self.x*other.x , self.y*other.y , self.z*other.z) # * operator automatically calls the __mul__ operator
        return result
    def __str__(self):
        return f"Vector({self.x}i, {self.y}j, {self.z}k)"

v1 = vector(7,6,2)
v2 = vector(2,5,4)

print(v1+v2) #print() automatically calls the __str__ functions
print(v1*v2)

