"""
CECS 277 Lab 5 
Classes & Objects (Rolodex)
Authors: Phan Ngo - Lucas Seitz
Date: 09/24/2025
Description:
  Console Rolodex that reads contacts from 'addresses.txt', allows display,
  add, search (by last name or zip), modify, and save-back-to-file on quit.
"""

from contact import Contact
import check_input

FILENAME = "addresses.txt"

def read_file():
    contacts = []                   #Start with an empty Python list that will hold Contact objects.
    with open(FILENAME, "r") as f:  #guarantees the file is closed automatically, even if something goes wrong.
        for line in f:              #Loop over the file line by line
            line = line.strip()     #Remove leading or whitespace, including the newline at the end of the line.
            if not line:            #If the line is now empty  skip it and move to the next one.         
                continue
            """
            Split the line into (at most) 6 pieces using commas as separators.
            maxsplit=5 ensures you never get more than 6 fields
            """
            parts = [p.strip() for p in line.split(",", maxsplit=5)]    
            if len(parts) != 6:         # If didn’t get exactly 6 fields, the line is considered malformed and is skipped.
                # Skip malformed lines simplicity
                continue
            fn, ln, ph, addr, city, zip_code = parts                    #Unpack the six fields into readable variable names.
            contacts.append(Contact(fn, ln, ph, addr, city, zip_code))  #Construct a Contact object with those fields and add it to the contacts list.
    return contacts


def write_file(contacts):
    with open(FILENAME, "w") as f:
        for c in contacts:
            f.write(repr(c) + "\n")


def get_menu_choice():
    print("Rolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")
    return check_input.get_int_range("> ",1, 5)


def _print_contacts_enumerated(contacts):
    print(f"Number of contacts: {len(contacts)}")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c}")


def _search_submenu():
    #Show the search submenu and return 1 (by last name) or 2 (by zip).
    print("Search:")
    print("1. Search by last name")
    print("2. Search by zip")
    return check_input.get_int_range("> ",1, 2)


def _find_matches_by_lastname(contacts, last_name):
    #Return all contacts whose last name matches (case-insensitive).
    ln = last_name.strip().lower()
    return [c for c in contacts if c.last_name.lower() == ln]


def _find_matches_by_zip(contacts, zip_code):
    #Return all contacts whose zip matches exactly (string compare)
    z = zip_code.strip()
    return [c for c in contacts if c.zip == z]


def modify_contact(cont):
    while True:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")
        choice = check_input.get_int_range("> ", 1, 7)

        if choice == 1:
            cont.first_name = input("Enter first name: ").strip()
        elif choice == 2:
            cont.last_name = input("Enter last name: ").strip()
        elif choice == 3:
            cont.phone = input("Enter phone #: ").strip()
        elif choice == 4:
            cont.address = input("Enter address: ").strip()
        elif choice == 5:
            cont.city = input("Enter city: ").strip()
        elif choice == 6:
            cont.zip = input("Enter zip: ").strip()
        elif choice == 7:
            # End modify loop
            break


def main():
    contacts = read_file()

    while True:
        choice = get_menu_choice()

        if choice == 1:
            # Display Contacts
            ordered = sorted(contacts,key=lambda c: (c.last_name.lower()))
            _print_contacts_enumerated(ordered)

        elif choice == 2:
            # Add Contact
            print("Enter new contact:")
            fn = input("First name: ").strip()
            ln = input("Last name: ").strip()
            ph = input("Phone #: ").strip()
            addr = input("Address: ").strip()
            city = input("City: ").strip()
            zip_code = input("Zip: ").strip()
            contacts.append(Contact(fn, ln, ph, addr, city, zip_code))
            contacts.sort()

        elif choice == 3:
            # Search Contacts
            sub = _search_submenu()
            if sub == 1:
                ln = input("Enter last name: ").strip()
                matches = _find_matches_by_lastname(contacts, ln)
            else:
                z = input("Enter zip code: ").strip()
                matches = _find_matches_by_zip(contacts, z)

            if matches:
                for m in matches:
                    print(m)
                    print()
            else:
                print("No matches found.")

        elif choice == 4:
            # Modify Contact
            fn = input("Enter first name: ").strip()
            ln = input("Enter last name: ").strip()

            # Find exact first + last match(es)
            candidates = [c for c in contacts
                          if c.first_name.lower() == fn.lower()
                          and c.last_name.lower() == ln.lower()]

            if not candidates:
                print("Contact not found.")
            else:
                cont = candidates[0]  # If multiple, modify the first match.
                print(cont)
                print()
                modify_contact(cont)
                contacts.sort()  # Resort after modifications

        elif choice == 5:
            # Save and Quit
            print("Saving File...")
            ordered = sorted(contacts,key=lambda c: (c.last_name.lower()))
            write_file(ordered)
            print("Ending Program")
            break


if __name__ == "__main__":
    main()
