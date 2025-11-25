# You have been tasked with writing a program for a popular bank that will automate all 
# its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. 
# The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account 
# having an initial balance of balance[i].

# Execute all the valid transactions. A transaction is valid if:

# The given account number(s) are between 1 and n, and
# The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
# Implement the Bank class:

# Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.

# boolean transfer(int account1, int account2, long money) Transfers money dollars from the account 
# numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.

# boolean deposit(int account, long money) Deposit money dollars into the account numbered account. 
# Return true if the transaction was successful, false otherwise.

# boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. 
# Return true if the transaction was successful, false otherwise.

# -----------------------------

# n=3
# 1,2,3
# balances = [12, ]
from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.num_accounts = len(balance)
    
    def _account_exists(self, account: int) -> bool:
        """Checks if an account number is valid."""
        return 1 <= account <= self.num_accounts
    
    def deposit(self, account: int, money: int) -> bool:
        if not self._account_exists(account):
            return False
        
        # Account numbers are 1-based, list is 0-indexed
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._account_exists(account):
            return False
        
        # Check for sufficient funds
        if self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check if both accounts exist
        if not (self._account_exists(account1) and self._account_exists(account2)):
            return False
        
        # Check if account1 has sufficient funds
        if self.balance[account1 - 1] < money:
            return False
        
        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True