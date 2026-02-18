class Bank:

    def __init__(self, balance: List[int]):
        self.bank = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.bank) or account2 > len(self.bank):
            return False
        if self.withdraw(account1, money):
            return self.deposit(account2, money)
        else:
            return False


    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.bank):
            return False
        self.bank[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.bank):
            return False
        if self.bank[account - 1] - money >= 0:
            self.bank[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)