 #Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twodvector :
    def __init__(self , i , j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2D Vector is {self.i}i + {self.j}j")
    

class threedvector(twodvector):
    def __init__(self, i, j ,k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3D Vector is {self.i}i + {self.j}j + {self.k}k")
    
a = twodvector(2, 4)
a.show()
b = threedvector(2,4,8)
b.show()