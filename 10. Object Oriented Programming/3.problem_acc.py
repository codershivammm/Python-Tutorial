class account:
    def __init__(self , bal , acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self , amount):
        self.balance -= amount
        print("Rs", amount, "is Debited from Your Account")
        print("Ramaining balance:- ", self.balance)
    
    def credit(self , amount):
        self.balance += amount
        print('Rs', amount, "Credited To Your Account") 
        print("Remaining Balance is :- ", self.balance)
    
acc1 = account(50000 , 9810027122)
print("Account Number:- " , acc1.account_no)
print("Total balance:- " , acc1.balance)
acc1.credit(10000)
acc1.debit(2000)
        
        