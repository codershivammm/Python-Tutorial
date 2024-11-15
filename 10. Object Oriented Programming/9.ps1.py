#Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programmer :

    company = "Microsoft"
    def __init__(self , name , salary , pincode):

        self.name = name 
        self.salary = salary
        self.pincode = pincode

p = programmer("shivam" , "50000" , "843329")
print(p.name , p.salary , p.pincode , p.company)

       