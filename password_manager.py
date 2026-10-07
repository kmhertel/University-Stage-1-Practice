#Password Manager

#holds the blueprints to store password strength
class Vault:
    #initialises the storage for the data
    def __init__(self):
          #the shelf for the strength of the password
          self.passwordstrengths = []

    def check_password_strength(self, password):
        return len(password) >= 8

password = input("What is your password? ")

my_vault = Vault()
print(my_vault.check_password_strength(password))

