import myBank
import random

# New classes, inheriting from yourBank
class evilBank(myBank.yourBank):
    '''Class to represent a bank that occasionally lies'''

    def inquiry(self):
        '''Overload the inquiry method to lie 50% of the time'''
        if(random.random() > 0.5):
            return self.balance * 1.2   # David M. Beazley, 2009
        else:
            return self.balance

if __name__ == '__main__':
    # Create a bank account instance
    account = myBank.yourBank("Siyuan Li", 500)

    # Call the auto deposit method
    account.auto_deposit()

    # Inquire about the account balance
    balance = account.inquiry()
    print("Current balance:", balance)

    # Create an "evil" bank account instance
    evil_account = evilBank("Jack", 1000)

    # Inquire about the "evil" bank account balance, which may contain false information
    evil_balance = evil_account.inquiry()
    print("Evil bank balance:", evil_balance)
