import os

DIARY_FILE = "diary.txt"

def add_entry():
    print("Enter your diary entry (type 'done' on a new line to finish):")
    
    entry_content = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        entry_content.append(line)
    
    entry = "\n".join(entry_content) + "\n" + "-"*50 + "\n"
    
    try:
        with open(DIARY_FILE, 'a') as file:
            file.write(entry)
        print("Diary entry saved successfully.")
    except PermissionError:
        print("Error: You don't have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_entries():
    if not os.path.exists(DIARY_FILE):
        print("No diary entries found.")
        return
    
    try:
        with open(DIARY_FILE, 'r') as file:
            content = file.read()
            print(content)
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Add a new entry")
        print("2. View previous entries")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
