from colorama import Fore

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(name, phone):
    contacts[name] = phone
    print(Fore.GREEN + "Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(Fore.GREEN + "Contact updated.")
    else:
        print(Fore.RED + "Contact not found.")

def show_phone(name):
    if name in contacts:
        print(Fore.GREEN + contacts[name])
    else:
        print(Fore.RED + "Contact not found.")

def show_all():
    if contacts:
        for name, phone in contacts.items():
            print(Fore.GREEN + f"{name}: {phone}")
    else:
        print(Fore.RED + "No contacts saved.")

def main():
    print(Fore.CYAN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.CYAN + "Good bye!")
            break

        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")

        elif command == "add":
            if len(args) == 2:
                add_contact(*args)
            else:
                print(Fore.RED + "Invalid number of arguments.")

        elif command == "change":
            if len(args) == 2:
                change_contact(*args)
            else:
                print(Fore.RED + "Invalid number of arguments.")

        elif command == "phone":
            if len(args) == 1:
                show_phone(*args)
            else:
                print(Fore.RED + "Invalid number of arguments.")

        elif command == "all":
            show_all()

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    contacts = {}
    main()
