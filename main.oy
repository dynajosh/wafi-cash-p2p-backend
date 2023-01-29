# In-Memory Backend for Peer-to-Peer Payment App

# Model for User
class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def send_money(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            return True
        else:
            return False
        
    def check_balance(self):
        return self.balance
    
    def transfer_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

# App class to handle all functionality
class P2PApp:
    def __init__(self):
        self.users = {}
        
    def add_user(self, name):
        user = User(name)
        self.users[name] = user
        return user
        
    def get_user(self, name):
        return self.users.get(name)

