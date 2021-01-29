from random import randint
import random


class BankAccount():
    # attributes
    def __init__(self, name):
        # to assign account_number with a random 8-digit number
        def random_8_digit_num(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        
        self.full_name = name
        self.account_number = random_8_digit_num(8)
        self.routing_number = 987654321
        self.balance = 0

        
    
    # METHODS

    # deposit
    def deposite(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}')

    # withdraw
    def withdraw(self, amount):
        self.balance -= amount
        print(f'Amount withdrawed: ${amount}')
        if amount > self.balance:
            print("Insufficient funds.")
            # and charge them with an overdraft fee of $10?

    # get_balance
    # add_interest
    # print_reciet

my_account = BankAccount( "Alberto")

my_account.deposite(666)
print(my_account.balance)
