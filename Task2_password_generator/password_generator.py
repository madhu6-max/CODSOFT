import random
import string
print("===== Password Generator =====")

# Input for length of the password

length = int(input("Length of password: "))
print("\nSelect password type:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")
choice = input("What option do you want to choose( 1/2/3) : ")

# Characters definition based on user choice

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = (string.ascii_letters + string.digits + string.punctuation)
else:
    print("Invalid option selected.")
    exit()

# Generate random password

password = " "
for i in range(length):
    password += random.choice(characters)
print("\nGenerated Password:")
print(password)