import json

# Path to the JSON file where contacts are saved
FILE_PATH = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_PATH, 'r') as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_PATH, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
    print("-" * 30)

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print_contact(contact)
    else:
        print("No contact found with that name or phone number.")

# Print contact details
def print_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")
    print("-" * 30)

# Update an existing contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the contact number to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print("Leave blank to keep current value.")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            deleted_contact = contacts.pop(contact_index)
            print(f"Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the Contact Manager application
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()