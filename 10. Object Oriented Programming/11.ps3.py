 #Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class demo:
    a =4

q = demo()
print(q.a) # Prints the class attribute because instance attribute is not present
q.a = 24  # Instance attribute is set
print(q.a)  # Prints the instance attribute because instance attribute is present
print(demo.a)  # Prints the class attribute
