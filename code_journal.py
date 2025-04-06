from datetime import datetime
def write_entry ():
    today = datetime.now().strftime("%y-%m-%d %H:%M") 
    print(">>>Code Journal Starting...")
    print("/n--- code journal ---")
    print("waiting for your input...")
    entry = input("what did you learn or work on today?/n> ")
    with open("code_journal.txt", "a") as file:
        file.write(f"[{today}]/n{entry}n/n")
        print("entry saved!/n")
        def read_entries():
            print("/n--- Previous Entries ---/n")
            try:
                with open("journal.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No entries yet./n")
def main():
    while True:
        print("1. write new entry")
        print("2. read past entries")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again./n")

if __name__ == "__main__":
    main()
