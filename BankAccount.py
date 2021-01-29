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
        self.__balance = 0


    def deposite(self, amount):
        self.__balance += amount
        print(f'Amount deposited: ${amount}')

    def withdraw(self, amount):
        self.__balance -= amount
        print(f'Amount withdrawed: ${amount}')
        if amount > self.__balance:
            print("Insufficient funds.")
            # and charge them with an overdraft fee of $10?

    def get_balance(self):
        print(f'Your balance is: ${self.__balance}')
        return self.__balance

    def add_interest(self):
        interest = self.__balance *  0.00083
        return interest

    def print_reciet(self):
        print(f'''
            {self.full_name}
            Account No.: ${self.account_number}
            Routing No.: ${self.routing_number}
            Balance:     ${self.get_balance()}
            ''')

person_1 = BankAccount("Alberto Dominguez")
person_1.deposite(200)
person_1.withdraw(50)
person_1.get_balance()
person_1.print_reciet()

person_2 = BankAccount("Thomas Jones")
person_2.deposite(5000)
person_2.print_reciet()


person_3 = BankAccount("Alex Chen")
person_3.deposite(500)
person_3.withdraw(600)
person_3.add_interest()
person_3.print_reciet()
