import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the contact file. Starting with an empty address book.")
        return []


def save_contacts(contacts):
    """Save contacts permanently to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)


def display_contact(contact, number=None):
    """Display one contact in a readable format."""
    if number is not None:
        print(f"\n--- Contact {number} ---")
    else:
        print("\n--- Contact ---")

    print(f"Name           : {contact['name']}")
    print(f"Phone Number   : {contact['phone']}")
    print(f"Email          : {contact['email']}")
    print(f"Postal Address : {contact['address']}")
    print(f"Notes          : {contact['notes']}")


def add_contact(contacts):
    print("\n=== Add Contact ===")
    name = input("Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    address = input("Postal Address: ").strip()
    notes = input("Other Information / Notes: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    print("\n=== All Contacts ===")

    if not contacts:
        print("No contacts found.")
        return

    sorted_contacts = sorted(contacts, key=lambda c: c["name"].lower())

    for number, contact in enumerate(sorted_contacts, start=1):
        display_contact(contact, number)


def search_contacts(contacts):
    print("\n=== Search Contact ===")

    if not contacts:
        print("No contacts found.")
        return

    query = input("Enter name, phone, email, address, or notes to search: ").strip().lower()

    if not query:
        print("Search value cannot be empty.")
        return

    matches = []
    for contact in contacts:
        searchable_text = " ".join([
            contact["name"],
            contact["phone"],
            contact["email"],
            contact["address"],
            contact["notes"]
        ]).lower()

        if query in searchable_text:
            matches.append(contact)

    if not matches:
        print("No matching contacts found.")
        return

    print(f"\nFound {len(matches)} matching contact(s).")
    for number, contact in enumerate(matches, start=1):
        display_contact(contact, number)


def choose_contact(contacts, action):
    """Find a contact by name or phone number."""
    if not contacts:
        print("No contacts available.")
        return None

    key = input(f"Enter contact name or phone number to {action}: ").strip().lower()

    matches = [
        contact for contact in contacts
        if contact["name"].lower() == key or contact["phone"].lower() == key
    ]

    if not matches:
        print("Contact not found.")
        return None

    if len(matches) == 1:
        return matches[0]

    print("Multiple contacts found:")
    for index, contact in enumerate(matches, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

    try:
        choice = int(input("Select contact number: "))
        if 1 <= choice <= len(matches):
            return matches[choice - 1]
    except ValueError:
        pass

    print("Invalid selection.")
    return None


def update_contact(contacts):
    print("\n=== Update Contact ===")
    contact = choose_contact(contacts, "update")

    if contact is None:
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone Number [{contact['phone']}]: ").strip()
    email = input(f"Email Address [{contact['email']}]: ").strip()
    address = input(f"Postal Address [{contact['address']}]: ").strip()
    notes = input(f"Notes [{contact['notes']}]: ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address
    if notes:
        contact["notes"] = notes

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    print("\n=== Delete Contact ===")
    contact = choose_contact(contacts, "delete")

    if contact is None:
        return

    confirm = input(f"Delete '{contact['name']}'? (y/n): ").strip().lower()

    if confirm == "y":
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Delete operation cancelled.")


def main():
    contacts = load_contacts()

    while True:
        print("\n" + "=" * 45)
        print("           ADDRESS BOOK APPLICATION")
        print("=" * 45)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using Address Book Application.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
