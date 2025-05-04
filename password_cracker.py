# Ask the user to set a secret password
real_password = input("Set your secret password: ")

# Open and read th wordlist file
with open("wordlist.txt", "r") as file:
	passwords = file.readlines()


# Try each password
attempts = 0
for guess in passwords:
	guess = guess.strip()    # Remove newline characters
	attempts += 1
	print (f"Trying: {guess}")
	if guess == real_password:
		print(f"Password cracked! it was '{guess}'")
		print(f"Total atempts: {attempts}")
		break

else:
	print("Password not found in wordlist.")
