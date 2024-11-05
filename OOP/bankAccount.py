class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f"Account Holder Name: {self.Name}")
        print(f"Current Balance: {self.Amount}")

    def Deposit(self, amount):
        self.Amount += amount
        print(f"Deposited {amount}. Updated Balance: {self.Amount}")

    def Withdraw(self, amount):
        self.Amount >= amount
        self.Amount -= amount
        print(f"Withdrew {amount}. Updated Balance: {self.Amount}")
        

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current balance: {interest}")

def main():

    account1 = BankAccount("Suchitra Dhakane",1000)
    account1.Display()
    account1.Deposit(500)
    account1.Withdraw(300)
    account1.CalculateInterest()

    print()

    account2 = BankAccount("Satyam Dhakane",2000)
    account2.Display()
    account2.Deposit(5000)
    account2.Withdraw(2000) 
    account2.CalculateInterest()

if __name__=="__main__":
    main()