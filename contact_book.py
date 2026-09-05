import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\nYour contact book is empty!")
        return
    print("\nYour Contacts:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")


def search_contact(contacts):
    if not contacts:
        print("\nYour contact book is empty!")
        return
    keyword = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
    if not found:
        print("No matching contact found.")


def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave a field blank to keep it unchanged.")
            name = input(f"New name ({contacts[index]['name']}): ").strip()
            phone = input(f"New phone ({contacts[index]['phone']}): ").strip()
            email = input(f"New email ({contacts[index]['email']}): ").strip()
            address = input(f"New address ({contacts[index]['address']}): ").strip()

            if name:
                contacts[index]["name"] = name
            if phone:
                contacts[index]["phone"] = phone
            if email:
                contacts[index]["email"] = email
            if address:
                contacts[index]["address"] = address

            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    contacts = load_contacts()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye! Your contacts are saved.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
  
