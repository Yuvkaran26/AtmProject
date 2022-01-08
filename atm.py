class Atm: 
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def checkBalance(self):
        print("Your current balance is $1000")
    def cashWithdrawal(self, withdrawal):
        self.withdrawal=withdrawal
        newAmount=1000-withdrawal
        print("You have withdrawaled cash $" +str (withdrawal) + " Your remaining balance is $" +str (newAmount))

def transaction():
    cardNumber = int(input("Enter the card number: "))
    pinNumber = int(input("Enter the pin number: "))
    transaction1 = Atm(cardNumber, pinNumber)
    print("Choose your activity")
    print("1 Balance Inquiry, 2 Cash Withdrawal")
    activity = int(input("Enter the activity number: "))
    if(activity == 1):
        transaction1.checkBalance()
    elif(activity == 2):
        withdrawal = int(input("Enter the amount to withdrawal: "))
        transaction1.cashWithdrawal(withdrawal)
    else:
        print("Enter a valid number")

transaction()