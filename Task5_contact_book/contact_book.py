import json
import os

# Store contacts
contacts = []

# Load saved contacts from JSON file
def load_contacts():
    global contacts

    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except:
            contacts = []


# Save contacts to JSON file
def save_contacts():
    with open("contacts.json", "w") as file:json.dump(contacts,file,indent=4)


# Load existing contacts
load_contacts()
print("===== ADVANCED CONTACT BOOK =====")

while True:
    print("""
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Total Contacts
7. Sort Contacts (A-Z)
8. Exit """)

    choice = input("Enter choice: ")


    # Add new contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        duplicate = False

        for c in contacts:
            if c["phone"] == phone:
                duplicate = True

        if duplicate:
            print("Phone number already exists.")

        else:
            contact = {
                "name": name,
                "phone": phone,
                "favorite": False}
            contacts.append(contact)
            save_contacts()
            print("Contact added successfully.")


    # View all contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")

        else:
            print("\n===== CONTACT LIST =====")

            for c in contacts:
                print(f"""
Name     : {c['name']}
Phone    : {c['phone']}
Favorite : {c['favorite']}
--------------------------""")


    # Search contact
    elif choice == "3":
        search = input("Enter name to search: ").lower()

        found = False
        for c in contacts:

            if search in c["name"].lower():
                print(f"""Contact Found
Name     : {c['name']}
Phone    : {c['phone']}
Favorite : {c['favorite']}""")

                found = True

        if not found:
            print("Contact not found.")

    # Update contact
    elif choice == "4":
        name = input("Enter name to update: ")
        updated = False

        for c in contacts:

            if c["name"].lower() == name.lower():
                c["phone"] = input("Enter new phone: ")
                favorite = input("Favorite (yes/no): ").lower()
                c["favorite"] = (True if favorite == "yes" else False)

                save_contacts()
                print("Contact updated.")
                updated = True

        if not updated:
            print("Contact not found.")

    # Delete contact
    elif choice == "5":
        name = input("Enter name to delete: ")

        deleted = False

        for c in contacts:
            if c["name"].lower() == name.lower():
                contacts.remove(c)
                save_contacts()
                print("Contact deleted.")
                deleted = True

        if not deleted:
            print("Contact not found.")


    # Total contacts
    elif choice == "6":
        print("\nTotal Contacts:",len(contacts))


    # Sort contacts alphabetically
    elif choice == "7":
        contacts.sort(key=lambda x:x["name"])
        save_contacts()
        print("Contacts sorted A-Z.")


    # Exit application
    elif choice == "8":
        print("\nExiting Contact Book...")
        break


    # Invalid choice
    else:
        print("Invalid choice. Try again.")