class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(f"Duplicated account '{account.account_number}'; nothing to be inserted")

    def delete(self, account_num):
        index = self.__search_private(account_num)
        if index != -1:
            removed_account = self.account_database.pop(index)
            print(f"Account '{removed_account.account_number}' deleted successfully.")
        else:
            print(f"Account '{account_num}' not found. No account deleted.")

    def __search_private(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i
        return -1

    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        print(f"Account '{account_num}' not found.")
        return None

    def __str__(self):
        accounts_str = ', '.join(str(account) for account in self.account_database)
        return f"[{accounts_str}]"


class Account:
    def __init__(self, num, account_type, account_name, balance):
        self.account_number = num
        self.type = account_type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to account '{self.account_number}'. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account '{self.account_number}'. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account '{self.account_number}' to withdraw {amount}.")

    def __str__(self):
        return f"{{Account Number: {self.account_number}, Type: {self.type}, Name: {self.account_name}, Balance: {self.balance}}}"


# Create accounts
account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)

# Initialize AccountDB and insert accounts
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)

# Display account database
print("Initial Account Database:")
print(my_account_DB)

# Test: Deleting an account that exists
print("\nDeleting account '0001':")
my_account_DB.delete("0001")
print("Account Database after deletion:")
print(my_account_DB)

# Test: Attempting to delete a non-existing account
print("\nAttempting to delete non-existing account '0010':")
my_account_DB.delete("0010")

# Test: Verify deletion of '0001' by attempting to search it
print("\nSearching for deleted account '0001':")
deleted_account = my_account_DB.search_public("0001")
