#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train :

    def __init__(self , trainnum):
        self.trainnum = trainnum

    def getstatus(self):
        print(f"Seat Availability in Train Number {self.trainnum} is {randint(10 , 20)}.")
    
    def getfare(self , fro , to):
        print(f"The fare from {fro} to {to} is {randint(1222,1250)}rs. ")

    def book(self , fro , to):
        print(f'Your Ticket is Booked from {fro} to {to} in train number {self.trainnum}.')
        print("Thank You ! Happy Journey !")


t = Train(130016)
t.getstatus()
t.getfare('Raipur' , "Chennai")
t.book("Raipur" , "Chennai")
    