class Bank:
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def info(self):
        print(f"Client: {self.client} , Saldo: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

def main():
    balance = int(input("Wat is uw saldo?"))
    milo_account = Bank("Milo", balance)
    wajih_account = Bank("Wajih", 20000)


    milo_account.info()
    milo_account.deposit(50)
    milo_account.info()
    milo_account.withdraw(100)
    milo_account.info()

if __name__ == "__main__":
    main()