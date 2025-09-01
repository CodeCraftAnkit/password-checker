# password strength checker
# password strength conditions :
# min 8 chars, digit, uppercase, lowercase, special char



import re

def check_password_strength(password):
    if len(password) < 8:
        return "weak: password must be at least 8 characters"

    if not any(char.isdigit() for char in password):
        return "weak: password must be contain a digit"

    if not any(char.isupper() for char in password):
        return "weak: password must be contain an uppercase letter"


    if not any(char.islower() for char in password):
        return "weak: password must be contain a lowercase letter"

    if not re.search(r'[!@#$%&^*()?<>]' , password):
        return "medium: password must contain a special character"

    return "strong: your password is secuerd!"


def password_checker():
    print("welcome to password checker")


    while True:
        password = input("enter your password (or type 'exit to quit):")

        if password.lower() == 'exit':
            print("THANK YOU FOR USING PASSWORD CHECKER")
            break

        result = check_password_strength(password)
        print(result)

# RUN THE PASSWORD CHECKER TOOL

if __name__ == "__main__":
    password_checker()

