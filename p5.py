import random
import string

print()
print("------ Welcome to Password Generator -------")
print('1. Generate Password')
print('2. Exit')

while True:
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if choice == 1:
            while True:
                length = input("Length of the password: ")
                character_pool=""
                try:
                    length = int(length)
                    lower_case = input("Include lowercase letters? (y/n):").lower()
                    if lower_case == 'y':
                        character_pool += string.ascii_lowercase
                    upper_case = input("Include uppercase letters? (y/n):").lower()
                    if upper_case == 'y':
                        character_pool += string.ascii_uppercase
                    digits = input("Include numbers? (y/n):").lower()
                    if digits == 'y':
                        character_pool += string.digits
                    symbol = input("Include symbols? (y/n):").lower()
                    if symbol == 'y':
                        character_pool += string.punctuation
                    break
                except:
                    print("Enter a number!")
            password = "".join(random.choice(character_pool) for _ in range(length))
            if not character_pool:
                print("❌ No character types selected. Please try again.")
            else:
                print(f"\n🧪 Generated Password: {password}\n")
            print(password)
            save = input("Do you want to save the file(y/n): ").lower()
            if save == 'y':
                with open("passwords.txt","a") as f:
                    f.write(password + "\n")
                print("Password saved to passwords.txt")
        elif choice == 2:
            print("Exit Successfully")
            break
    except:
        print("Enter a valid input!")