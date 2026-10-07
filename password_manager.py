#Password Manager

def check_password_strength(password):
    return len(password) >= 8

password = input("What is your password ")

print(check_password_strength(password))