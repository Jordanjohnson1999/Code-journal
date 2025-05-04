import time

# Step 1: Set the target password
password = "1234"

# Step 2: Start counting attempts
attempts = 0

# Step 3: Brute-force loop from 0000 to 9999
for guess in range(10000):
	guess_str = str(guess).zfill(4)   #ensures it's 4 digits (e.g., '0007')
	print(f"Trying: {guess_str}")
	time.sleep(0.01) # slows it down so you can watch
	attempts += 1
	if guess_str == password:
		print(f"Password found: {guess_str}")
		print(f"Total attempts: {attempts}")
		break
