#####################Assignment: User##################################
# #For this assignemnt, we'll add some functionality to the User class:

# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

# //1, Create a file with the User class, including the __init__ and make_deposit methods
class User:
    bank_name = "First National Dojo"

    # __init__ important function that need for making instances. The contructor os the class.
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    # //2, Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.amount -= amount

    # //3, Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.amount}')

    # Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, amount, other_user):
        self.amount -= amount
        other_user.amount += amount
        self.display_user_balance()
        other_user.display_user_balance()


# //4, create 3 instances of the User class
mlay = User("Michael")
nancy18 = User("Nancy")
lolay = User("Levi")

# //5, have the first user to make 3 deposits 1 withraw
mlay.make_deposit(100)
mlay.make_deposit(100000)
mlay.make_deposit(1000000)
mlay.make_withdrawal(50000)
mlay.display_user_balance()

# // 6, have the second user to make 2 deposits and 2 withraws
nancy18.make_deposit(500)
nancy18.make_deposit(1000)
nancy18.make_withdrawal(100)
nancy18.make_withdrawal(200)
nancy18.display_user_balance()

# //7, have the third user to make 1 deposit and 3 withraws
lolay.make_deposit(10)
lolay.make_withdrawal(2)
lolay.make_withdrawal(1)
lolay.make_withdrawal(3)
lolay.display_user_balance()

# //BONUS - Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
mlay.transfer_money(1000000, nancy18)
