#Password Manager

#holds the blueprints to store password strength
class Vault:
    #initialises the storage for the data, takes variable master_password as input
    def __init__(self, master_password):
          #the shelf for the strength of the password
          self._password = []
          #stores the password to the vault
          self.__master_password = master_password

    #function for checking the strength of the password
    def check_password_strength(self, password):
        return len(password) >= 8

    def add_password(self, password):
         #checks the strength of the password and adds it to the vault if it is strong enough
         if self.check_password_strength(password):
              #adds the password to the vault list
              self._password.append(password)

    def get_passwords(self, master_password_attempt):
        #checks if the master password attempt is correct
        if master_password_attempt == self.__master_password:
            #when true, returns the list of passwords stored in the vault
            return self._password
        else:
            return "Access denied. Incorrect master password."

class AdminVault(Vault):
    def __init__(self, master_password, admin_id):
          super().__init__(master_password)
          self.admin_id = admin_id
          self.audit_log = []

    def log_event(self, action):
        #adds an entry to the audit log with the admin ID and the action performed, inside brackets tells python to format the string with the values of self.admin_id and action
        self.audit_log.append(f"Admin {self.admin_id}: {action}")

    def force_add_password(self, password):
        #forces the addition of a password to the vault without checking its strength
        self._password.append(password)
        self.log_event(f"Forced addition of password: {password}")



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
print(my_vault._password)
#test to access the private attribute directly
# print(my_vault.__master_password) #this will throw an error because the attribute is private

#instantiating the child class
admin = AdminVault(master_password="AdminMaster123", admin_id="SEC_OPS_01")
#test forced addition (bypassing length checks)
admin.force_add_password("123")
#retrieve passwords using inherited Vault method
print("Admin Vault Contents:", admin.get_passwords("AdminMaster123"))
#check administrative audit log
print("Audit Log:", admin.audit_log)

