class car:
    
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("Car stopped")

##INHERITANCE##

class ToyotaCar(car): #single inheritance
    def __init__(self,brand):
        self.brand = brand 

car1 = ToyotaCar("fortuner")
print(car1.brand)
car1.start()

#Multi-Level Inheritance

class fortuner(ToyotaCar):
    def __init__(self, brand , type):
        super().__init__(brand) #Toyota Car ki brand attribute ko use krne ke liye super() method use hoga
        self.type = type
    
car1 = fortuner("Fortuner" , "Diesel")
print(car1.brand)
print(car1.type)
car1.start()
car1.stop()