class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.d = {}
        for i in range(1, self.n + 1):
            self.d[i] = balance[i - 1]
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.n < account1 or self.n < account2 or self.d[account1] < money:
            return False
        self.d[account1] -= money
        self.d[account2] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if self.n < account:
            return False
        self.d[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if self.n < account or self.d[account] < money:
            return False
        self.d[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)