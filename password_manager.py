#Password Manager

#holds the blueprints to store password strength
class Vault:
    #initialises the storage for the data, takes variable master_password as input
    def __init__(self, master_password):
          #the shelf for the strength of the password
          self.__password = []
          #stores the password to the vault
          self.__master_password = master_password

    #function for checking the strength of the password
    def check_password_strength(self, password):
        return len(password) >= 8

    def add_password(self, password):
         #checks the strength of the password and adds it to the vault if it is strong enough
         if self.check_password_strength(password):
              #adds the password to the vault list
              self.__password.append(password)

    def get_passwords(self, master_password_attempt):
        #checks if the master password attempt is correct
        if master_password_attempt == self.__master_password:
            #when true, returns the list of passwords stored in the vault
            return self.__password
        else:
            return "Access denied. Incorrect master password."

#input of master password and store in variable
master_password = input("What is your master password? ")

#input of password and store in variable
password = input("What is your password? ")

#input of master password attempt
master_password_attempt = input("Please enter your master password to access the vault: ")

#creates vault to store info
my_vault = Vault(master_password)
#check to see if code works
    #uses password input
print(my_vault.check_password_strength(password))
    #uses password input
print(my_vault.add_password(password))
    #uses the master_password_attempt input
print(my_vault.get_passwords(master_password_attempt))
#test to access the private attribute directly
print(my_vault.__password) #this will throw an error because the attribute is private
print(my_vault.__master_password) #this will throw an error because the attribute is private

