from random import randint
import random


class BankAccount():
    # attributes
    def __init__(self, name, routing_number, balance):
        # to assign account_number with a random 8-digit number
        def random_8_digit_num(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        
        self.full_name = name
        self.account_number = random_8_digit_num(8)
        self.routing_number = routing_number
        self.balance = balance

        
    
    # METHODS

    # deposit
    def deposite(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}')

    # withdraw
    # get_balance
    # add_interest
    # print_reciet

my_account = BankAccount( "Alberto", 12, 100  )

my_account.deposite(666)
print(my_account.balance)
