import random
import string

def generatePassword(len):
    digits = string.digits                   # all the digits (0,1,2,3,4,5,6,7,8,9)
    lower = string.ascii_lowercase           # all alphabets in lowercase
    upper = string.ascii_uppercase           # all alphabets in uppercase
    special = string.punctuation             # all the special characters

    password = [random.choice(digits),
                random.choice(lower),
                random.choice(upper),
                random.choice(special)]
        
    unshuffledPassword = digits + lower + upper + special

    extra = len - 4
    password += random.choices(unshuffledPassword, k = extra)
    random.shuffle(password)

    return "".join(password)

def main():
    print("\n----------------------------------------------------------------")
    print("             P A S S W O R D   G E N E R A T O R")
    print("----------------------------------------------------------------\n")
    try:
       
        length = int(input("Enter the length of the password : "))
        if length < 6:
            print("Password length must be atleast 6 characters.")
            return

        password = generatePassword(length)

        if password:
            print("\nGenerated Password : ", password)

        print("\n----------------------------------------------------------------")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")

main()