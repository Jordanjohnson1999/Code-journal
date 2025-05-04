import random

flashcards = {
	"git": {
		"What does 'git status' do?": "Shows the state of working directory and staging areas.",
		"What does 'git as .' do?": "Stages all changes in the current directory.",
		"What does 'git commit -m \"msg\"' do?": "Commits staged changes with a message.",
		"What does 'git push' do?": "Uploads local commits to the remote repository.",
		"What does 'git pull' do?": "Fetches and merges changes from the remote repo to local.",

	},
	"python": {
		"What does 'len()' do?": "Returns the number of items in an object.",
		"What is a list comprehension ?": "A compact way to create lists using a single line of code.",
		"What does 'def' do?": "Defines a new function.",
		"What is a directory?": "A collection of key-value pairs.", 
		"What does 'if __name__ \"__main__\"' mean?": "Checks if the script is run directly.",
	},
	"terminal": {
		"What does 'ls' do?": "Lists files in the current directory.",
		"What does 'cd ..' do?": "Moves up one directory level.",
		"What does 'pwd' show you?": "Prints the current working directory.",
		"What does 'mkdir' do?": "Creates a new directory.",
		"What does 'rm filename' do?": "Deletes the file named 'filename'.",
		"What does 'touch file.py' do?": "Creates an empty file named file.py.",
		"What does 'clear' do ?": "Clears the terminal screen.",
		"What does 'man <command>' do?": "Shows the manual for a command.",
	}
}

def run_flashcards(topic):
	cards = flashcards.get(topic)
	if not cards:
		print("Invalid topic selection")
		return
	while True:
		question = random.choice(list(cards.keys()))
		input(f"\n{question} (Press Enter to reveal answer)")
		print("Answer:", cards[question])
		again = input("Do you want another flashcard? (y/n): ").lower()
		if again != 'y':
			print("Good session! Keep practicing.")
			break

def main():
	print("Welcome to Terminal Flashcards!")
	print("Available topics:", ", ".join(flashcards.keys()))
	for topic in flashcards:
		print(f"- {topic}")

	topic = input("Choose a topic to study: ").strip().lower()
	run_flashcards(topic)

if __name__ == "__main__":
	main()

