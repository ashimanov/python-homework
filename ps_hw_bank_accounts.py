

import math
import random


class Customer:
  def __init__(self, name: str, address: str):
    self.name = name
    self.address = address
    self.account_number = int

  def __str__(self):
    return f'--- Customer information ---\nCustomer name: {self.name}\nCustomer address: {self.address}\nCustomer account number: {self.account_number}\n'


class Account:
  def __init__(self, customer: Customer, initial_balance: float):
    self.account_number = self._generate_account_number()
    self.customer = customer
    self.customer.account_number = self.account_number
    self.balance = initial_balance

  def _generate_account_number(self) -> int:
        return math.floor(random.random() * 1000000)


class Bank:
  def __init__(self):
    self.accounts = {}

  def create_account(self, customer: Customer, initial_balance: float) -> Account:
    account = Account(customer, initial_balance)
    self.accounts[account.account_number] = account
    print(f'Account opened for client: {customer.name}.\nAccount number: {customer.account_number}.\nInitial balace: {self.accounts[customer.account_number].balance}\n')

  def get_account(self, customer: Customer) -> Account:
    try:
        if customer.account_number in self.accounts:
            print(f'--- Account information ---\nAccount owner: {customer.name}\nAccount number: {customer.account_number}\nAccount balance: {self.accounts[customer.account_number].balance}\n')
        else:
            raise ValueError("Account not found.\n")
    except ValueError as e:
       print(e)
       
    
  def deposit(self, customer: Customer, amount: int):
    try:
        if customer.account_number in self.accounts:
            self.accounts[customer.account_number].balance += amount
            print(f'--- Deposit confirmation ---\nAmount deposited: {amount}\nAccount number: {customer.account_number}\nNew balance: {self.accounts[customer.account_number].balance}\n')
        else:
            raise ValueError("Account not found.\n")
    except ValueError as e:
       print(e)

  def withdraw(self, customer: Customer, amount: int):
    try:
        if customer.account_number in self.accounts:
            try:
                if amount <= self.accounts[customer.account_number].balance:
                    self.accounts[customer.account_number].balance -= amount
                    print(f'--- Withdrawal confirmation ---\nAmount withdrawn: {amount}.\nAccount number: {customer.account_number}.\nNew balance: {self.accounts[customer.account_number].balance}\n')
                else:
                    raise ValueError(f"Cannot withdraw {amount} from bank account {customer.account_number}.\nInsufficient funds.")
            except ValueError as e:
               print(e)
        else:
            raise ValueError("Account not found.\n")
    except ValueError as e:
       print(e)


def banking_scenario():

    NatWest = Bank()
    Customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1")
    Customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5")

    NatWest.create_account(Customer1, 5000) # Alice opens an account
    NatWest.create_account(Customer2, 4000) # Bob opens an account

    print(Customer1) # full customer information
    print(Customer2) # full customer information

    NatWest.get_account(Customer1) # customer account information
    NatWest.get_account(Customer2) # customer account information

    NatWest.deposit(Customer1, 1000) # Alice deposits some money
    NatWest.withdraw(Customer1, 3000) # Alice withdraws some money
    NatWest.withdraw(Customer1, 4000) # Alice tries to withdraw more money than she has in her account




banking_scenario()



