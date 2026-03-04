contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("a - Add New Contact")
    print("d - Delete Contact")
    print("v - View all Contacts")
    print("s - Search by Name")
    print("q - Quit")

    choice = input("\n Your Choice: ").strip().lower()

    if choice == "a":
        print("\n--- Add New Contact ---")

        while True:
            name = input("Enter name: ").strip()
            if name:
                name = name.title()
                break
            print("Name cannot be empty.")

        while True:
            phone= input("Enter phone number: ").strip()
            if phone.isdigit():
                break
            print("Phone must only contain digits.")

        contacts[name] = phone
        print("Contact added successfully!")
        print(f" {name}: {phone}")

        print("-" * 40)

    elif choice == "v":
        print("\nAll Contacts")

        if not contacts:
            print("Your contact book is empty.")
        else:
            for name, phone in contacts.items():
                print(f"{name:<18} : {phone}")

        print("-" * 40)

    elif choice == "s":
        name_search = input("Name of contact: ").strip().title()

        if name_search in contacts:
            print(f"{name_search}: {contacts[name_search]}")
        else:
            print(f"No contact named '{name_search}' was found.")
        
        print("-" * 40)

    elif choice == "d":
        name_search = input("Name of contact: ").strip().title()

        if name_search in contacts:
            del contacts[name_search]
            print(f"Contact  '{name_search}' deleted successfully.")
        else:
            print(f"No contact named '{name_search}' was found.")


    elif choice == "q":
        print("\nGoodbye!")
        break
    else:
        print("Invalid Choice. Please use a, v, s or q.")

    print("-" * 30)