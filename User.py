class User:
    def __init__(self,name,email):
        self.name = name
        self.account_balance = 0
        self.email = email

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance ${self.account_balance}")  
        
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} transferred ${amount} to {other_user.name}")

larry = User("larry", "larry@3stooges.com")
curly = User("curly", " curly@3stooges.com")
moe = User("moe", "moe@3stooges.com")

larry.make_deposit(500)
larry.make_deposit(300)
larry.make_deposit(100)
larry.make_withdrawl(200)
larry.transfer_money(moe,50)

curly.make_deposit(500)
curly.make_deposit(1000)
curly.make_withdrawl(100)
curly.make_withdrawl(200)

moe.make_deposit(5000)
moe.make_withdrawl(1000)
moe.make_withdrawl(100)
moe.make_withdrawl(200)

larry.display_user_balance()
curly.display_user_balance()
moe.display_user_balance()
